class Car:
    def __inint__(self):
        self.name = newName
        self.price = '100000'
    def move(self):
        print('车正在移动')
    def toot(self):
        print('车子鸣笛警示')
red_car = Car()
red_car.move()
red_car.toot()
red_car.color = 'red'
print('内存地址:',id(red_car),red_car.color)
print('-'*50)

blue_car = Car()
blue_car.newName = '宝马'
blue_car.color = '蓝色'
blue_car.move()
blue_car.toot()
print('内存地址:',id(blue_car),blue_car.newName,blue_car.color)
print('-'*50)

white_car = Car()
white_car.newName = '奥迪'
white_car.color = '白色'
white_car.move()
white_car.toot()
print('内存地址:',id(white_car),white_car.newName,white_car.color)
