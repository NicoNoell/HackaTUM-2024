from Wrapper.Scenario import Scenario
from TelcAPI import Runner
import time
from TelcAPI import Backend, Runner
from Wrapper.Scenario import Scenario
from Wrapper.Vehicle import Vehicle
from Wrapper.Customer import Customer
from Wrapper.UpdateScenario import UpdateScenario
from Wrapper.VehicleUpdate import VehicleUpdate
import json


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
        # find the closest customer
        closestCustomer = None
        closestDistance = float("inf")
        for customer in customers:
            d = distance(v.x, v.y, customer.x, customer.y)
            if d < closestDistance:
                closestCustomer = customer
                closestDistance = d
            customers.remove(closestCustomer)
        matchings[v] = closestCustomer
        v.assign(closestCustomer)
    return matchings


def allocateFreeVehicles(scenario: Scenario):
    # filter for the customers who are awaiting service
    remainingCustomers = [
        scenario.customers
        for customer in scenario.customers
        if customer.awaitingService
    ]
    vehicleToCustomerMap = calculateVehicleToCustomerMapping(
        scenario.vehicles, remainingCustomers
    )
    Runner.updateScenario(
        scenario.id,
        UpdateScenario(
            vehicleUpdates=[
                VehicleUpdate(vehicle.id, customer.id)
                for vehicle, customer in vehicleToCustomerMap.items()
            ]
        ),
    )


def eventLoop(scenario_id: str):

    while True:
        scenario = Runner.getScenario(scenario_id)
        num_customers_awaiting = numberCustomersAwaitingService(scenario)

        if num_customers_awaiting == 0:
            # all customers have been serviced
            break

        # TODO: update logic
        time.sleep(1)


Runner.initScenario()
Runner.launchScenario("120937bb-4779-4d57-a180-dbbba5c08b7f")
eventLoop("120937bb-4779-4d57-a180-dbbba5c08b7f")
