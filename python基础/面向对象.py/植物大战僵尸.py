# 定义一个类
class Botany:
    def __init__(self,newname):
        self.name = newname

    # 定义方法(功能)
    def sun(self):
        print(self.name,'放阳光')
    def fapao(self):
        print(self.name,'发炮')
    def stop(self):
        print(self.name,'阻挡')

# 定义创建一个对象
xrk = Botany('向日葵')
xrk.energy = '有叶子，笑脸'
xrk.sun()
print(xrk.energy)
print('*'*45)
wd = Botany('豌豆')
wd.color = '蓝色'
wd.life = '血量'
wd.fapao()
print(wd.color,wd.life)
print('*'*45)
jg = Botany('坚果')
jg.life = '血量'
jg.stop()
print(jg.life)
print('*'*45)
class Aggressor:
    def __init__(self):
        self.name = '僵尸'
      # 攻击者
    def go(self):
        #走
        print(self.name,'走')
    def jump(self):
        print('跳')
    def eat(self):
        print('吃')
js = Aggressor()
js.go()
js.jump()
js.eat()

