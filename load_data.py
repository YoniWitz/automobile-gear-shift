import json
from car_inventory import CarInventory
from input_car import InputCar
from vin_model import VinModel

def load_car_inventory(file_name):
    car_inventories = []

    with open(file_name) as car_inv:
        data = json.load(car_inv)

    for car_inventory_item in data:
        new_car_inventory = CarInventory(car_inventory_item['model'], car_inventory_item['gears_max_speed'])
        
        car_inventories.append(new_car_inventory)  
    
    return car_inventories

def load_input_car(file_name):
    input_cars = []

    with open(file_name) as inputs:
        data = json.load(inputs)
        
    for input_car in data:
        new_car = InputCar(input_car['vin'], input_car['gear'], input_car['speed'])

        input_cars.append(new_car)
    
    return input_cars

def load_vin_model(file_name):
    vin_models = []

    with open(file_name) as vin_mod:
        data = json.load(vin_mod)

    for vin_model_item in data:
        new_vin_model = VinModel(vin_model_item['vin'], vin_model_item['model'])
        
        vin_models.append(new_vin_model)
    
    return vin_models