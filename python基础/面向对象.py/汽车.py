# 定义一个类
class Car:
    # 定义功能（方法）
    def move(self):
        print('车在移动')
    def toot(self):
        print('车在鸣笛')
# 创建一个对象
red_Car = Car()
red_Car.move()
red_Car.color = '红色'
print('内存地址1:'id(red_Car),red_Car.color)
print('*'*30)
blue_Car = Car()
blue_Car.toot()
blue_Car.color = '蓝色'
print('内存地2:'id(blue_Car),blue_Car.color)
print('*'*30)
yellow_Car = Car()
yellow_Car.move()
yellow_Car.toot()
yellow_Car.color = '黄色'
print('内存地3:'id(yellow_Car),yellow_Car.color)
print('*'*30)
