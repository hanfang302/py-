class Car:
    def __init__(self,newname):
        self.name = newname
    def move(self):
        print(self.name,'车在移动')
    def toot(self):
        print(self.name,'车在鸣笛---')
    def oil(self):
        print(self.name,'车油50')
BMW = Car('宝马')
BMW.color = '白色'
BMW.move()
BMW.toot()
BMW.oil()
print(BMW.color)
print('-'*45)
AUDI = Car('奥迪')
AUDI.color = '黑色'
AUDI.move()
AUDI.toot()
AUDI.oil()
print(AUDI.color)
print('-'*45)
Benz = Car('奔驰')
Benz.color = '黑色'
Benz.move()
Benz.toot()
Benz.oil()
print(Benz.color)
print('-'*45)
