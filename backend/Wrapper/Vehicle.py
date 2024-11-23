import json

class Vehicle():
    def __init__(self, json_data:dict) -> None:
        self.id = str(json_data["id"]) if json_data["id"] != None else None
        self.coordX = float(json_data["coordX"]) if json_data["coordX"] != None else None
        self.coordY = float(json_data["coordY"]) if json_data["coordY"] != None else None
        self.isAvailable = bool(json_data["isAvailable"]) if json_data["isAvailable"] != None else None
        self.vehicleSpeed = float(json_data["vehicleSpeed"]) if json_data["vehicleSpeed"] != None else None
        self.customerId = str(json_data["customerId"]) if json_data["customerId"] != None else None
        self.remainingTravelTime = float(json_data["remainingTravelTime"]) if json_data["remainingTravelTime"] != None else None
        self.distanceTravelled = float(json_data["distanceTravelled"]) if json_data["distanceTravelled"] != None else None
        self.activeTime = float(json_data["activeTime"]) if json_data["activeTime"] != None else None
        self.numberOfTrips = int(json_data["numberOfTrips"]) if json_data["numberOfTrips"] != None else None

    def getPos(self) -> tuple[int, int]:
        return (self.coordX, self.coordY)
    
    def json(self) -> dict:
        return {"id": self.id,
                "coordX": self.coordX,
                "coordY": self.coordY,
                "isAvailable": self.isAvailable,
                "vehicleSpeed": self.vehicleSpeed,
                "customerId": self.customerId,
                "remainingTravelTime": self.remainingTravelTime,
                "distanceTravelled": self.distanceTravelled,
                "activeTime": self.activeTime,
                "numberOfTrips": self.numberOfTrips}