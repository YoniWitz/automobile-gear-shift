import datetime
from datetime import datetime as my_date

import json
from dateutil.relativedelta import relativedelta

from_gear = 3
to_gear = 4
strftime = "%d.%m.%Y"

greater_than_x_months = 1
smaller_than_x_days = 7
def avg_speed_by_model(log_change_in_gear_file_name, model):
    with open(log_change_in_gear_file_name) as logger:
        logs = json.load(logger)
        
    speeds = [log['speed'] for log in logs if log['model'] == model and int(log['from_gear']) == from_gear and int(log['to_gear']) == to_gear]
    
    if(len(speeds) > 0):
        return sum(speeds) / len(speeds)
    
    return 0

def recurring_error(log_error_file_name):
    today = datetime.date.today()
    one_month_ago = today + relativedelta(months=-greater_than_x_months)
    seven_days_ago = today + relativedelta(days=-smaller_than_x_days)
    
    with open(log_error_file_name) as logger:
        logs = json.load(logger)

    error_cars_greater_than_x_months = [log['vin'] for log in logs if (my_date.strptime(log['time_stamp'], strftime)).date() < one_month_ago]
    error_cars_smaller_than_x_days = [log['vin'] for log in logs if (my_date.strptime(log['time_stamp'], strftime)).date() > seven_days_ago]
    intersect_array = list(set(error_cars_greater_than_x_months).intersection(error_cars_smaller_than_x_days))

    return intersect_array



        