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
              .format(self.model, self.vin, self.from_gear, self.to_gear, self.gear, self.speed, self.time_stamp))

def empty_logger(file_name):
    if os.path.exists(file_name):
        data = []
        with open(file_name, "w") as logs:
            json.dump(data, logs)

def log(file_name, logging_info):
    existing_json = []

    if os.path.exists(file_name):
        try:
            with open(file_name,'r') as existing_data:
                existing_json = json.load(existing_data)
            existing_data.close()
        except:
            print("Unable to load file %s as JSON" % file_name)

    existing_json.append(logging_info)

    with open(file_name, "w") as logs:
        json.dump(existing_json, logs,  default=vars, indent=4)

def print_out_log(file_name):
    with open(file_name) as logger:
        data = json.load(logger)
    
    for log in data:
        print(log)

def populate_logs(input_cars, car_inventories, vin_models, change_in_gear_file_name, gear_error_file_name):
    empty_logger(change_in_gear_file_name)
    empty_logger(gear_error_file_name)

    strftime = "%d.%m.%Y"

    vins_prev_gear = {}
    for input_car in input_cars:
        vin = input_car.vin
        model = [vin_model.model for vin_model in vin_models if vin_model.vin == vin][0]

        if vin in vins_prev_gear:
            vin_prev_gear = vins_prev_gear[vin]
            
            if input_car.gear != vin_prev_gear:
                new_log = Log(model, vin, vin_prev_gear, input_car.gear, input_car.speed, date.today().strftime(strftime))
                log(change_in_gear_file_name, new_log)
        
        vins_prev_gear[vin] = input_car.gear
        
        gear_max_speed_for_model = [car_inventory.gears_max_speeds for car_inventory in car_inventories if car_inventory.model == model][0]
        max_speed = [gear_max_speed['max_speed'] for gear_max_speed in gear_max_speed_for_model if gear_max_speed['gear'] == input_car.gear][0]
        
        if(input_car.speed > max_speed):
            new_log = Log(model, vin, input_car.gear, input_car.gear, input_car.speed, date.today().strftime(strftime))
            log(gear_error_file_name, new_log)
