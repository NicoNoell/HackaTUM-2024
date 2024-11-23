from backend.Wrapper.Vehicle import Vehicle
from backend.Wrapper.Customer import Customer
import json


class Scenario:
    def __init__(self, json_data: dict) -> None:
        self.id = str(json_data["id"]) if json_data["id"] != None else None
        self.startTime = (
            str(json_data["startTime"]) if json_data["startTime"] != None else None
        )
        self.endTime = (
            str(json_data["endTime"]) if json_data["endTime"] != None else None
        )
        self.status = str(json_data["status"]) if json_data["status"] != None else None

        self.vehicles = []
        for vehicleData in json_data["vehicles"]:
            self.vehicles.append(Vehicle(vehicleData))

        self.customers = []
        for customerData in json_data["customers"]:
            self.customers.append(Customer(customerData))

    def json(self) -> dict:
        return {
            "id": self.id,
            "startTime": self.startTime,
            "endTime": self.endTime,
            "status": self.status,
            "vehicles": [v.json() for v in self.vehicles],
            "customers": [c.json() for c in self.customers],
        }
