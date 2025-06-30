import abc


class Vehicle(abc.ABC):
    @abc.abstractmethod
    def startEngine(self, fuel):
        pass
    
class car(Vehicle):
    def startEngine(self):
        print(f"starting the car with fuel.")

class electric_car(Vehicle):
    def startEngine(self):
        print(f"starting the car with electric engine.")
        

def start_vehicle(vehicle_type):
    vehicle_type.startEngine()
    

c = car()
t = electric_car()


start_vehicle(c)