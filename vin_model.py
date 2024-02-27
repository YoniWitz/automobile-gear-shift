class VinModel:
    def __init__(self, vin, model):
        self.vin = vin
        self.model = model

    def describe(self):
        print("vin: {}, model: {}".format(self.vin, self.model))

    def __repr__(self):
        return (
            f"vin: {self.vin}\n"
            f"model: {self.model}\n"
        )
