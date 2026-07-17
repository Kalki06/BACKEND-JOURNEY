class Engine:

    def start(self):
        print("Engine Started")

    def stop(self):
        print("Engine stop")

class Car:
    def __init__(self, brandName):
        self.engine = Engine()
        self.brandName = brandName


    def carBrand(self):
        print(f"Car Brand is {self.brandName}")

    def carStart(self):
        self.engine.start()
        print("Car is Moving")

    def carstop(self):
        self.engine.stop()
        print("Car stopped")

car = Car("Suzuki")

car.carBrand()
car.carStart()
car.carstop()