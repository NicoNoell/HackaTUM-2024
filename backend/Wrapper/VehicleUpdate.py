import json


class VehicleUpdate:
    def __init__(self, vehicleId: str, customerId: str) -> None:
        self.id = vehicleId
        self.customerId = customerId

    def json(self) -> dict:
        return {"id": self.id, "customerId": self.customerId}
