from Wrapper.Scenario import Scenario
from TelcAPI import Runner
import time
from TelcAPI import Backend, Runner
from Wrapper.Scenario import Scenario
from Wrapper.Vehicle import Vehicle
from Wrapper.Customer import Customer
from Wrapper.UpdateScenario import UpdateScenario
from Wrapper.VehicleUpdate import VehicleUpdate
import logging
import json

logging.basicConfig(
    filename="event_loop.log",  # Log file name
    level=logging.INFO,  # Log level: DEBUG, INFO, WARNING, ERROR, CRITICAL
    format="%(asctime)s - %(levelname)s - %(message)s",  # Log format
    datefmt="%Y-%m-%d %H:%M:%S",  # Timestamp format
)


def numberCustomersAwaitingService(scenario: Scenario):
    num_customers_awaiting = 0
    for customer in scenario.customers:
        if customer.awaitingService:
            num_customers_awaiting += 1
    return num_customers_awaiting


def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def calculateVehicleToCustomerMapping(
    v: list[Vehicle], c: list[Customer]
) -> list[dict[Vehicle, Customer]]:
    matchings: dict[Vehicle, Customer] = dict()
    # convert list of customers to dict
    customers = {customer.id: customer for customer in c}
    vehicles = v.copy()
    for keys, customer in customers.items():
        fastestVehicle = None
        leastTime = float("inf")
        is_available = True
        for vehicle in vehicles:
            if vehicle.isAvailable or vehicle.customerId not in [
                id for id in customers.keys()
            ]:  # it may happen that the customer was dropped off already (i.e. customer.awaitingService = false),
                # but vehicle.customerId is still set
                t = (
                    distance(
                        vehicle.coordX, vehicle.coordY, customer.coordX, customer.coordY
                    )
                    / 40
                )
                if t < leastTime:
                    logging.info(f"Vehicle {vehicle.id} is available")
                    fastestVehicle = vehicle
                    leastTime = t
                    is_available = True
            else:
                vehicleDestinationX = customers[vehicle.customerId].destinationX
                vehicleDestinationY = customers[vehicle.customerId].destinationY
                t = (
                    vehicle.remainingTravelTime
                    + distance(
                        customer.coordX,
                        customer.coordY,
                        vehicleDestinationX,
                        vehicleDestinationY,
                    )
                    / vehicle.vehicleSpeed
                )
                if t < leastTime:
                    fastestVehicle = vehicle
                    leastTime = t
                    is_available = False

        if is_available and fastestVehicle is not None:
            logging.info("Assigning %s to %s", fastestVehicle.json(), customer.json())
            matchings[fastestVehicle] = customer
            fastestVehicle.assign(customer)

        if fastestVehicle is not None:
            vehicles.remove(fastestVehicle)
    return matchings


def allocateFreeVehicles(scenario: Scenario):
    # filter for the customers who are awaiting service
    remainingCustomers: list[Customer] = [
        customer for customer in scenario.customers if customer.awaitingService
    ]
    # freeVehicles: list[Vehicle] = [v for v in scenario.vehicles if v.isAvailable]
    # logging.info("[Remaining Customers]", remainingCustomers[0].json())
    vehicleToCustomerMap = calculateVehicleToCustomerMapping(
        scenario.vehicles, remainingCustomers
    )
    if len(vehicleToCustomerMap) > 0:
        update = (
            Runner.updateScenario(
                scenario.id,
                UpdateScenario(
                    vehicleUpdates=[
                        VehicleUpdate(vehicle.id, customer.id)
                        for vehicle, customer in vehicleToCustomerMap.items()
                    ]
                ),
            ),
        )
        logging.info("[Assigning...] %s", update)


def eventLoop(scenario_id: str):
    while True:
        scenario = Runner.getScenario(scenario_id)
        num_customers_awaiting = numberCustomersAwaitingService(scenario)

        if num_customers_awaiting == 0:
            # all customers have been serviced
            break

        # logging.info(f"Number of customers awaiting service: {num_customers_awaiting}")

        allocateFreeVehicles(scenario)
        time.sleep(1)
