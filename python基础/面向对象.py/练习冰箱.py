class wangwu:
    def __init__(self,newName,animal):
        self.name = newName
        self.animal = animal
    def buyWangwu(self):
        print(self.name,'准备了一只%s'%self.animal)
    def open_bingXiang(self):
        print(self.name,'打开冰箱')
    def Zhuang_jin(self):
        print('把%s装进冰箱'%self.animal,)
    def close_bingXiang(self):
        print('关闭冰箱')
game = wangwu('王五','鹦鹉')
game.buyWangwu()
game.open_bingXiang()
game.Zhuang_jin()
game.close_bingXiang()
print('-'*50)
xx = wangwu('小雪','小狗')
xx.buyWangwu()
xx.Zhuang_jin()
xx.close_bingXiang()
