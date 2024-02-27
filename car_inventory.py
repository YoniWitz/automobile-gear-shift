class CarInventory:
    def __init__(self, model, gears_max_speeds):
        self.model = model
        self.gears_max_speeds = gears_max_speeds

    def describe(self):
        print("Car model: {}".format(self.model))

        for gear_max_speed in self.gears_max_speeds:
            print("gear: " + gear_max_speed['gear'] + " max speed: " + str(gear_max_speed['max_speed']))
            
    def __repr__(self):
        return (
            f"model: {self.model}\n"
            f"gears_max_speeds: {self.gears_max_speeds}\n"
        )
    
            