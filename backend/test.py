from TelcAPI import Backend, Runner
from Wrapper.Scenario import Scenario
import json

scenario: Scenario = Backend.getScenario("973dc6f2-2cde-4872-9689-ac7f968790c0")
print(scenario.json())


def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


# filter for the customers who are awaiting service
remainingCustomers = [
    scenario.customers for customer in scenario.customers if customer.awaitingService
]
for v in scenario.vehicles:
    # find the closest customer
    closestCustomer = None
    closestDistance = float("inf")
    for customer in remainingCustomers:
        d = distance(v.x, v.y, customer.x, customer.y)
        if d < closestDistance:
            closestCustomer = customer
            closestDistance = d
    # assign the closest customer to the vehicle
    v.assign(closestCustomer)

    remainingCustomers.remove(closestCustomer)
