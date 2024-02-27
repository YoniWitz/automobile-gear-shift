import json
from log import Log
# logs = [
#             {
#                 "Subaru":{
#                     "sum": 100,
#                     "count": 1
#                 }
#             }
#         ]
from_gear = 3
to_gear = 4

def avg_speed_by_model(file_name, model):
    with open(file_name) as logger:
        logs = json.load(logger)
        
    speeds = [log['speed'] for log in logs if log['model'] == model and int(log['from_gear']) == from_gear and int(log['to_gear']) == to_gear]
    
    if(len(speeds) > 0):
        return sum(speeds) / len(speeds)
    
    return 0


        