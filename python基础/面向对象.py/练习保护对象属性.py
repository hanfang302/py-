class Dog:
    def __init__(self,newname='小土豆'):
        self.__name = newname
        self.color = '棕色'
    def shu_chu(self):
        print(self.__name)
        print(self.color)
    def xiu_gai(self,newmingzi):
        self.__name = newmingzi
    def dang_qian(self):
        return self.__name
    def __del__(self):
        print('不存在了')

gg = Dog()
gg.shu_chu()
gg.__name = '小包子'
gg.color = '灰色'
print('-'*50)
print('换名失败后')
gg.shu_chu()
print('-'*50)
print('重新换名子')
gg.xiu_gai('小包子')
gg.shu_chu()
#gg.dang_qian()

print('-'*50)
idel gg
