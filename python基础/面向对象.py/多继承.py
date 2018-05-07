class Animal(object):
    def zu_zong(self):
        print('祖宗')

class Ma(Animal):
    def fly(self):
        print('飞')
    def run(self):
        print('跑')
    def carry(self):
        print('运')

class ML(Animal):
    def chew(self):
        print('咀嚼')
    def haha(self):
        print('嘿嘿')
    def swim(self):
        print('游')

class LZ(ML,Ma):
    def haha(self):
        print('哈哈')
    def go(self):
        print('走')

    def __del__(self):
        print('死啦')

骡子 = LZ()
骡子.fly()
骡子.run()
骡子.carry()
骡子.haha()
骡子.go()
#骡子.zu_zong()
del 骡子
