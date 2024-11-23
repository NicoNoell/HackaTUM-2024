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
from geopy import distance
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


def computeDistance(x1, y1, x2, y2):
    return distance.distance((x1, y1), (x2, y2)).m

def calculateNaiveVehicleToCustomerMapping(
    vehicles: list[Vehicle], c: list[Customer]
) -> list[dict[Vehicle, Customer]]:
    matchings: dict[Vehicle, Customer] = dict()
    customers = c.copy()
    for v in vehicles:
        if len(customers) == 0:
            return matchings
        # find the closest customer
        closestCustomer = None
        closestDistance = float("inf")
        for customer in customers:
            d = computeDistance(v.coordX, v.coordY, customer.coordX, customer.coordY)
            if d < closestDistance:
                closestCustomer = customer
                closestDistance = d
        matchings[v] = closestCustomer
        v.assign(closestCustomer)
        # logging.info("[Remaining Customers] %s", [c.id for c in customers])
        # logging.info("[closestCustomer] %s", closestCustomer.json())
        customers.remove(closestCustomer)
    return matchings


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
                    computeDistance(
                        vehicle.coordX, vehicle.coordY, customer.coordX, customer.coordY
                    )
                    / 11
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
                    + computeDistance(
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
    freeVehicles: list[Vehicle] = [v for v in scenario.vehicles if v.isAvailable]
    vehicleToCustomerMap = calculateNaiveVehicleToCustomerMapping(
        freeVehicles, remainingCustomers
    )
    # logging.info("[Remaining Customers]", remainingCustomers[0].json())
    # vehicleToCustomerMap = calculateVehicleToCustomerMapping(
    #     scenario.vehicles, remainingCustomers
    # )
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
    start_time = time.time()
    while True:
        scenario = Runner.getScenario(scenario_id)
        logging.info("[EVENT LOOP] %s", scenario.json())
        num_customers_awaiting = numberCustomersAwaitingService(scenario)

        if num_customers_awaiting == 0:
            # all customers have been serviced
            end_time = time.time()
            break

        # logging.info(f"Number of customers awaiting service: {num_customers_awaiting}")

        allocateFreeVehicles(scenario)
        time.sleep(1)
    
    logging.info(f"Scenario completed in {end_time - start_time} seconds")

