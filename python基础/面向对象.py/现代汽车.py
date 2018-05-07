class Car(object):
    def move(self):
        print('车在移动')
    def stop(self):
        print('车子停车')
class CarStore(object):
    def order(self):
        self.car = Car()# 找一辆车
        self.car.move()
        self.car.stop()

