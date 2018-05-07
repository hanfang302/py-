class Zombie:
    def __init__(self,newName):
        self.name = newName
    def go(self):
        print(self.name,'走')
    def run(self):
        print(self.name,'跑')
    def eat(self):
        print(self.name,'吃')
js = Zombie('僵尸')
js.go()
js.run()
js.eat()
print('内存地址:',id(js))
print('-'*50)
class Botany:
    def __init__(self,newName):
        self.name = newName
    def sun(self):
        print(self.name,'放阳光')
    def gun(self):
        print(self.name,'发炮，摇头')
    def stop(self):
        print(self.name,'阻挡')

xrk = Botany('向日葵')
xrk.sun()
wd = Botany('豌豆')
wd.color = '绿色'
wd.point = '血量'
wd.gun()
print(wd.color,wd.point)
print('内存地址:',id(wd))
print('-'*50)
jg = Botany('坚果')
jg.point = '血量'
jg.stop()
print('内存地址:',id(jg),jg.point)
print('-'*50)
