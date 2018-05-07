# 创建一个类，首字母大写
class Dog():
    
    # 初始化属性（name）
    def __init__(self,name,age):
 
        self.name = name
        self.age = age
    # 功能，方法    
    def sit(self):
        print(self.name.title() + ':is now sitting.')

    def roll_over(self):
        print(self.name.title() + ':rolled over!')

# dog = 对象
dog = Dog('小花',5)
dog.sit()
dog.roll_over()
print('-'*45)
dog1 = Dog('willie',6)
print('my dog name is:' +' ' + dog1.name.title() + '.')
print('my dog is:' +' ' + str(dog1.age) + 'years old.')
print('-'*45)
dog2 = Dog('luck',3)
print('\nyour dog name is' + dog2.name.title() + '.')
print('your dog is' + str(dog2.age) + 'years old.')
dog2.sit() 
print('='*45)


class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.reading = 0

    def name(self):
        name1 = str(self.year) + ' ' + self.make + ' ' + self.model
        return name1.title()

    def read(self):
        print('this car has' + ' ' + str(self.reading) + 'miles on it.')

    def upadte(self,mileage):
        self.reading = mileage

        if mileage >= self.reading:
            self.reading = mileage
        else:
            print('you cat roll back an odometer')

    def odometer(self,miles):
        self.reading += miles

      # 电动汽车
class ElectricCar(Car):

    def __init__(self,make,model,year):
        super().__init__(make,model,year)

new_car = Car('subaru','outback',2018)
print(new_car.name())

#new_car.reading = 25
new_car.update = (23500)
new_car.read()

new_car.update = (100)
new_car.read()
print('-'*45)
tesla =  ElectricCar('tesla','model s',2018)
print(tesla.name())


