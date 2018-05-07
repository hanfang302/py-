#定义类
class car:
    #功能
    def move(self):
        print('车正在移动----')
    def toot(self):
        print('车正在--滴滴滴---')

BMW = car()
#添加属性
BMW.color = '黑色'
BMW.wheelnum = '4'
BMW.oil = '50升'
#调用对象
BMW.move()
BMW.toot()
print(BMW.color)
print(BMW.wheelnum)
print(BMW.oil)
