class Car():
    def move(self):
        print('车在移动')
    def toot(self):
        print('车在鸣笛')

BMW = Car()
BMW.color = '黑色'
BMW.wheelNum = '4个轮'
BMW.move()
BMW.toot()
print(BMW.color)
print(BMW.wheelNum)
