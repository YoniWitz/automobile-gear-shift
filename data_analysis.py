import json
from log import Log

def avg_speed_by_model(fileName):
    with open(fileName) as logger:
        data = json.load(logger)

        for log in data:
            print(type(log))
            if log.from_gear == 3 and log.to_gear == 4:
                print(log)