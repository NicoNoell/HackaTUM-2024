from Wrapper.Scenario import Scenario
from TelcAPI import Runner
import time

def numberCustomersAwaitingService(scenario: Scenario): 
    num_customers_awaiting = 0
    for customer in scenario.customers:
        if customer.awaitingService:
            num_customers_awaiting += 1
    return num_customers_awaiting

def eventLoop(scenario_id : str):

    while True: 
        scenario = Runner.getScenario(scenario_id)
        num_customers_awaiting = numberCustomersAwaitingService(scenario)

        if num_customers_awaiting == 0:
            # all customers have been serviced
            break
        
        # TODO: update logic
        time.sleep(1)


