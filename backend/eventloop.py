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
            d = distance(v.coordX, v.coordY, customer.coordX, customer.coordY)
            if d < closestDistance:
                closestCustomer = customer
                closestDistance = d
        matchings[v] = closestCustomer
        v.assign(closestCustomer)
        # logging.info("[Remaining Customers] %s", [c.id for c in customers])
        # logging.info("[closestCustomer] %s", closestCustomer.json())
        customers.remove(closestCustomer)
    return matchings


def allocateFreeVehicles(scenario: Scenario):
    # filter for the customers who are awaiting service
    remainingCustomers: list[Customer] = [
        customer for customer in scenario.customers if customer.awaitingService
    ]
    freeVehicles: list[Vehicle] = [v for v in scenario.vehicles if v.isAvailable]
    # logging.info("[Remaining Customers]", remainingCustomers[0].json())
    vehicleToCustomerMap = calculateVehicleToCustomerMapping(
        freeVehicles, remainingCustomers
    )
    logging.info("[Vehicle to Customer Map] %s", vehicleToCustomerMap)
    if len(freeVehicles) > 0 and len(remainingCustomers) > 0:
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
        logging.info("[EVENT LOOP] %s", scenario.json())
        num_customers_awaiting = numberCustomersAwaitingService(scenario)

        if num_customers_awaiting == 0:
            # all customers have been serviced
            break

        # logging.info(f"Number of customers awaiting service: {num_customers_awaiting}")

        allocateFreeVehicles(scenario)
        time.sleep(1)


scenarioId = "6099a36d-0238-46cd-b711-fb91a6eab8df"
logging.info(
    "[Initialising Scenario:] %s",
    Runner.initScenarioById(scenarioId),
)
logging.info(
    "[Launching Scenario:] %s",
    Runner.launchScenario(scenarioId, 0.005),
)
eventLoop(scenarioId)
