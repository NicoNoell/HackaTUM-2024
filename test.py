from backend.TelcAPI import Backend, Runner
from backend.Wrapper.Scenario import Scenario
from backend.Wrapper.VehicleUpdate import VehicleUpdate
from backend.Wrapper.UpdateScenario import UpdateScenario
from backend.eventloop import eventLoop

scenario: Scenario = Backend.getScenario("268bdbc6-1e37-4392-ab63-8b4b557bd0b5")
Runner.initScenario(scenario)
Runner.launchScenario(scenarioId=scenario.id, speed=40)
vehicles = Runner.getScenario(scenario)

vehicleUpdate = VehicleUpdate("7804ce9a-d76f-45c2-bd75-5a321d7f0614", scenario.customers[0].id)
updateScenario = UpdateScenario([vehicleUpdate])
Runner.updateScenario(scenario.id, updateScenario)
print(scenario.vehicles)
