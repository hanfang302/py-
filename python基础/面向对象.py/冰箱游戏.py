class Play_zs:
    def __init__(self,newName,animal):
        self.name = newName
        self.animal = animal
    def buyAnimal(self):
        print('%s' % self.name,'买了一个%s' % self.animal)
    def open_bingXiang(self):
        print('打开冰箱')
    def Zhuang_jin(self):
        print('把%s装进冰箱' % self.animal)
    def close_bingXiang(self):
        print('关闭冰箱')

game = Play_zs('张三','大象')
game.buyAnimal()
game.open_bingXiang()
game.Zhuang_jin()
game.close_bingXiang()
print('-'*50)
lisi = Play_zs('李四','王含青')
lisi.buyAnimal()
lisi.open_bingXiang()
lisi.Zhuang_jin()
lisi.close_bingXiang()
print('-'*50)
