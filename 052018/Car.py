class Car(object):

    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

    @staticmethod
    def make_car_sound():
        print("Vrooommm!")

    def init_prices(self):
        inputs = [100]
        self.append_prices(inputs)
        return inputs

    def append_prices(self, ain):
        ain.append(200)
        return ain


mustang = Car('Ford', 'Mustang')

print(mustang.wheels)
print(Car.wheels)

mustang.make_car_sound()
Car.make_car_sound()

inputs = mustang.init_prices()
print(inputs)