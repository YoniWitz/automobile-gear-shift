        
from datetime import date
import json
import os

class Log:
    def __init__(self, model, vin, from_gear, to_gear, speed, time_stamp):
        self.model = model
        self.vin = vin
        self.from_gear = from_gear
        self.to_gear = to_gear
        self.speed = speed
        self.time_stamp = time_stamp

    def describe(self):
        print("log model: {}, vin: {}, fromGear: {}, toGear: {}, speed:{}, timeStamp:{}"
              .format(self.model, self.vin, self.fromGear, self.toGear, self.gear, self.speed, self.timeStamp))

def empty_logger(fileName):
    if os.path.exists(fileName):
        data = []
        with open(fileName, "w") as logs:
            json.dump(data, logs)

def log(fileName, loggingInfo):
    loggingInfoJson = json.dumps(loggingInfo, default=vars, indent=4)
    
    if os.path.exists(fileName):
        if os.stat(fileName).st_size == 0:
            data = []
        else:
            with open(fileName) as logs:
                data = json.load(logs)
        data.append(loggingInfoJson)
    else:
        data = [loggingInfoJson]
                
    with open(fileName, "w") as logs:
        json.dump(data, logs)

def print_out_log(fileName):
    with open(fileName) as logger:
        data = json.load(logger)
    
    for log in data:
        print(log)

def populate_logs(input_cars, car_inventories, vin_models, change_in_gear_file_name, gear_error_file_name):
    empty_logger(change_in_gear_file_name)
    empty_logger(gear_error_file_name)

    strftime = "%d/%m/%Y %H:%M:%S"

    prevGear = input_cars[0].gear
    for input_car in input_cars:
        vin = input_car.vin
        model = [vin_model.model for vin_model in vin_models if vin_model.vin == vin][0]
        
        new_log = Log(model, vin, prevGear, input_car.gear, input_car.speed, date.today().strftime(strftime))

        if input_car.gear != prevGear:
            log(change_in_gear_file_name, new_log)
            prevGear = input_car.gear

        gearAndMaxSpeedForModel = [car_inventory.gears_max_speeds for car_inventory in car_inventories if car_inventory.model == model]
        maxSpeed = [gearAndMaxSpeed['max_speed'] for gearAndMaxSpeed in gearAndMaxSpeedForModel[0] if gearAndMaxSpeed['gear'] == input_car.gear][0]
        
        if(input_car.speed > maxSpeed):
            log(gear_error_file_name, new_log)
