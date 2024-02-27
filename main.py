#from data_analysis import avg_speed_by_model
from load_data import load_car_inventory, load_input_car, load_vin_model
from log import populate_logs
def main(change_in_gear_file_name, gear_error_file_name):
    print(main)
    input_cars = load_input_car('input_cars.json')
    car_inventories = load_car_inventory('car_inventory.json')
    vin_models = load_vin_model('vin_model.json')

    populate_logs(input_cars, car_inventories, vin_models, change_in_gear_file_name, gear_error_file_name)

 

