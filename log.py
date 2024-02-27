        
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
        print("log model: {}, vin: {}, fromGear: {}, toGear: {}, speed:{}, timeStamp:{}".format(self.model, self.vin, self.fromGear, self.toGear, self.gear, self.speed, self.timeStamp))

def log(fileName, loggingInfo):
    json_object = json.dumps(loggingInfo, default=vars, indent=4)

    if os.path.exists(fileName):
        if os.stat(fileName).st_size == 0:
            data = []
        else:
            with open(fileName) as logs:
                data = json.load(logs)
        data.append(json_object)
    else:
        data = [json_object]
                
    with open(fileName, "w") as logs:
        json.dump(data, logs)

def print_out_log(fileName):
    with open(fileName) as logger:
        data = json.load(logger)
    
    for log in data:
        print(log)
