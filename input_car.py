class InputCar:
    def __init__(self, vin, gear, speed):
        self.vin = vin
        self.gear = gear
        self.speed = speed

    def describe(self):
        print("Car vin: {}, gear: {}, speed:{}".format(self.vin, self.gear, self.speed))