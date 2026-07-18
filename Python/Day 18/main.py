class PetrolEngine:

    def start(self):
        print("Engine Started")

    def stop(self):
        print("Engine stop")

class ElectricEngine:

    def start(self):
        print("Engine Started")

    def stop(self):
        print("Engine stop")

class Car:
    def __init__(self, brandName, engine):
        self.engine = engine
        self.brandName = brandName


    def carBrand(self):
        print(f"Car Brand is {self.brandName}\n")

    def carStart(self):
        self.engine.start()
        print("Car is Moving\n")

    def carstop(self):
        self.engine.start()
        print("Car stopped\n")

petrol_Engine = PetrolEngine()
car = Car("Suzuki", petrol_Engine)

car.carBrand()
car.carStart()
car.carstop()

ele_Engine = ElectricEngine()
elecar = Car("Tesla", ele_Engine)

elecar.carBrand()
elecar.carStart()
elecar.carstop()
