import json

class Customer():
    def __init__(self, json_data:dict) -> None:
        self.id = str(json_data["id"]) if json_data["id"] != None else None
        self.coordX = float(json_data["coordX"]) if json_data["coordX"] != None else None
        self.coordY = float(json_data["coordY"]) if json_data["coordY"] != None else None
        self.destinationX = float(json_data["destinationX"]) if json_data["destinationX"] != None else None
        self.destinationY = float(json_data["destinationY"]) if json_data["destinationY"] != None else None
        self.awaitingService = bool(json_data["awaitingService"]) if json_data["awaitingService"] != None else None

    def getPos(self) -> tuple[int, int]:
        return (self.coordX, self.coordY)
    
    def getDestination(self) -> tuple[int, int]:
        return (self.destinationX, self.destinationY)
    
    def json(self) -> dict:
        return {"id": self.id,
                "coordX": self.coordX,
                "coordY": self.coordY,
                "destinationX": self.destinationX,
                "destinationY": self.destinationY,
                "awaitingService": self.awaitingService}