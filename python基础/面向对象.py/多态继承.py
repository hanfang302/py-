class Animal(object):
    def zu(self):
        print('我是老祖宗')

class Ma(Animal):
    def __init__(self):
        zi_G = '飞'
    def fly(self):
        print('我会飞')
    def heihei(self):
        print('我会嘿嘿')
    #def zu(self):
       #print('我是新祖宗')

class Lv(Animal):
    def __init__(self):
        mao = '有'
    def swim(self):
        print('游泳')
    def heihei(self):
        print('我会呵呵')

class LZ(Ma,Lv):
    def haha(self):
        print('我会哈哈')
    def heihei(self):
        print('傻子')

luozi = LZ()
luozi.fly()
luozi.swim()
luozi.haha()
luozi.heihei()
luozi.zu()
