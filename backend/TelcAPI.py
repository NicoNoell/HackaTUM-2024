import requests
from backend.Wrapper.Scenario import Scenario
from backend.Wrapper.Customer import Customer
from backend.Wrapper.Vehicle import Vehicle
from backend.Wrapper.UpdateScenario import UpdateScenario

# NOTE: Um ein Scenario im Runner zu nutzen, muss es zuerst mit get_scenario vom Backend abgefragt bzw.
#       anderweitig erstellt werden und dann mit Runner.init_scenario dem Runner übergeben werden.

PAYLOAD_HEADER = {"Content-Type": "application/json"}


class Runner:
    def getScenario(scenarioId: str) -> Scenario:
        try:
            return Scenario(
                requests.get(
                    f"http://localhost:8090/Scenarios/get_scenario/{scenarioId}"
                ).json()
            )
        except:
            print("Response ist None oder ungültig")

    def initScenario(scenario: Scenario) -> None:
        try:
            requests.post(
                f"http://localhost:8090/Scenarios/initialize_scenario",
                json=scenario.json(),
                headers=PAYLOAD_HEADER,
            ).json()
        except:
            print("Response ist None oder ungültig")

    def updateScenario(scenarioId: str, payload: UpdateScenario) -> None:
        try:
            requests.put(
                f"http://localhost:8090/Scenarios/update_scenario/{scenarioId}",
                json=payload.json(),
                headers=PAYLOAD_HEADER,
            ).json()
        except:
            print("Response ist None oder ungültig")

    def launchScenario(scenarioId) -> None:
        try:
            requests.post(
                f"http://localhost:8090/Runner/launch_scenario/{scenarioId}"
            ).json()
        except:
            print("Response ist None oder ungültig")


class Backend:
    def getCustomer(customerId: str) -> Customer:
        try:
            return Customer(
                requests.get(f"http://localhost:8080/customers/{customerId}").json()
            )
        except:
            print("Response ist None oder ungültig")

    def getAllCustomers(scenarioId: str) -> list[Customer]:
        try:
            return [
                Customer(c)
                for c in requests.get(
                    f"http://localhost:8080/scenarios/{scenarioId}/customers"
                ).json()
            ]
        except:
            print("Response ist None oder ungültig")

    # TODO: Add Metadata Response
    def getScenarioMetadata(scenarioId: str) -> None:
        try:
            return requests.get(
                f"http://localhost:8080/scenario/{scenarioId}/metadata"
            ).json()
        except:
            print("Response ist None oder ungültig")

    def createScenario(
        numberOfVehicles: int = 5, numberOfCustomers: int = 5
    ) -> Scenario:
        try:
            return Scenario(
                requests.post(
                    f"http://localhost:8080/scenario/create?numberOfVehicles={numberOfVehicles}&numberOfCustomers={numberOfCustomers}"
                ).json()
            )
        except:
            print("Response ist None oder ungültig")

    def getAllScenarios() -> list[Scenario]:
        try:
            return [
                Scenario(s)
                for s in requests.get(f"http://localhost:8080/scenarios").json()
            ]
        except:
            print("Response ist None oder ungültig")

    def deleteScenario(scenarioId) -> None:
        try:
            requests.delete(f"http://localhost:8080/scenarios/{scenarioId}").json()
        except:
            print("Response ist None oder ungültig")

    def getScenario(scenarioId: str) -> Scenario:
        try:
            return Scenario(
                requests.get(f"http://localhost:8080/scenarios/{scenarioId}").json()
            )
        except:
            print("Response ist None oder ungültig")

    def getAllVehicles(scenarioId: str) -> list[Vehicle]:
        try:
            return [
                Vehicle(v)
                for v in requests.get(
                    f"http://localhost:8080/scenarios/{scenarioId}/vehicles"
                ).json()
            ]
        except:
            print("Response ist None oder ungültig")

    def getVehicle(vehicleId: str) -> Vehicle:
        try:
            return Vehicle(
                requests.get(f"http://localhost:8080/vehicles/{vehicleId}").json()
            )
        except:
            print("Response ist None oder ungültig")
