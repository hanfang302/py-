class play:
    def __init__(self,newName,animale):
        self.name = newName
        self.animale = animale
    def buy(self):
        print('%s'%self.name,'买了一只%s'%self.animale)
    def open(self):
        print('打开冰箱')
    def putin(self):
        print('把动物%s放入冰箱'%self.animale) 
    def close(self):
        print('关闭冰箱')

lisi = play('李四','大象')
lisi.buy()
lisi.open()
lisi.putin()
lisi.close()
print('-'*50)
wangwu = play('王五','狗')
wangwu.buy()
wangwu.open()
wangwu.putin()
wangwu.close()

