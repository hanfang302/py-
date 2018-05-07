class Car:
    def getCarInfo(self):
        print('车轮个数:%d,颜色:%s'%(self_wheelNum,self_color))

    def move(self):
        print('车在奔跑----')

    def toot(self):
        print('车在鸣笛--嘟嘟嘟--')



BMW = Car()
BMW.color = '黑色'
BMW.wheelNum = 4
BMW.move ()
BMW.toot ()
print(BMW.color)
print(BMW.wheelNum)
