from Wrapper.VehicleUpdate import VehicleUpdate
import json

class UpdateScenario():
    def __init__(self, json_data:dict) -> None:
        self.id = str(json_data["id"]) if json_data["id"] != None else None
        self.vehicleUpdate = VehicleUpdate(json_data["VehicleUpdate"]) if json_data["VehicleUpdate"] != None else None

    def json(self) -> dict:
        return {"id": self.id,
                "vehicleUpdate": self.vehicleUpdate.json()}