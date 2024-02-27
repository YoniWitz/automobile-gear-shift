#from data_analysis import avg_speed_by_model
from load_data import load_car_inventory, load_input_car, load_vin_model
from log import populate_logs, print_out_log, change_in_gear_file_name, gear_error_file_name

input_cars = load_input_car('inputCars.json')
car_inventories = load_car_inventory('CAR_MODEL_INVENTORY.json')
vin_models = load_vin_model('vin_model.json')

populate_logs(input_cars, car_inventories, vin_models)

        
#avg_speed_by_model(change_in_gear_file_name)
    
#print_out_log(change_in_gear_file_name)
#print_out_log(gear_error_file_name)

 

