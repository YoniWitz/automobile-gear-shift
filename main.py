from datetime import date
from data_analysis import avg_speed_by_model
from load_data import load_car_inventory, load_input_car, load_vin_model
from log import Log, log, print_out_log

input_cars = load_input_car('inputCars.json')
car_inventories = load_car_inventory('CAR_MODEL_INVENTORY.json')
vin_models = load_vin_model('vin_model.json')

change_in_gear_file_name = "change_in_gear.json"
gear_error_file_name = "log_error.json"

strftime = "%d/%m/%Y %H:%M:%S"

prevGear = 0
for input_car in input_cars:
    vin = input_car.vin
    model = [item.model for item in vin_models if item.vin == vin][0]

    new_log = Log(model, vin, prevGear, input_car.gear, input_car.speed, date.today().strftime(strftime))

    if input_car.gear != prevGear:
        log(change_in_gear_file_name, new_log)
        prevGear = input_car.gear

    gearAndMaxSpeedForModel = [item.gears_max_speeds for item in car_inventories if item.model == model]
    maxSpeed = [item['max_speed'] for item in gearAndMaxSpeedForModel[0] if item['gear'] == input_car.gear][0]
    
    if(input_car.speed > maxSpeed):
        log(gear_error_file_name, new_log)
        
avg_speed_by_model(change_in_gear_file_name)
    


 

