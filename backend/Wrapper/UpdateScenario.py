from Wrapper.VehicleUpdate import VehicleUpdate
import json


class UpdateScenario:
    def __init__(self, json_data: dict) -> None:
        self.vehicles = []
        for vehicle in json_data["vehicles"]:
            self.vehicles.append(VehicleUpdate(vehicle))

    def json(self) -> dict:
        return {"vehicles": [v.json() for v in self.vehicleUpdate.json()]}
