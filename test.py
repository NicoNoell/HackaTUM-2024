from TelcAPI import Backend, Runner
import json

scenario = Backend.getScenario("268bdbc6-1e37-4392-ab63-8b4b557bd0b5")
Runner.initScenario(scenario)
Runner.launchScenario(scenario.id)
for i in range(10):
    print(Runner.getScenario("268bdbc6-1e37-4392-ab63-8b4b557bd0b5").vehicles[0].getPos())
    Runner.updateScenario(scenario.id)