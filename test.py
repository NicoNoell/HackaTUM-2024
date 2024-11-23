from backend.TelcAPI import Backend, Runner
from backend.Wrapper.Scenario import Scenario
import json

scenario: Scenario = Backend.getScenario("973dc6f2-2cde-4872-9689-ac7f968790c0")

print(scenario.json())
