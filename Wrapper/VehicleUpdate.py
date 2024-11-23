import json

class VehicleUpdate():
    def __init__(self, json_data:dict) -> None:
        self.id = str(json_data["id"]) if json_data["id"] != None else None
        self.customerId = str(json_data["customerId"]) if json_data["customerId"] != None else None

    def json(self) -> dict:
        return {"id": self.id,
                "customerId": self.customerId}