from Wrapper.VehicleUpdate import VehicleUpdate
import json


class UpdateScenario:
    def __init__(self, vehicleUpdates: list[VehicleUpdate]) -> None:
        self.vehicles = vehicleUpdates

    def json(self) -> dict:
        return {"vehicles": [v.json() for v in self.vehicles]}
