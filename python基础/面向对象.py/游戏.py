class Human:
      #人类
    def __init__(self):
        self.name = '人'
        print(self.name)
    def go(self):
        print('走')
    def jump(self):
        print('跳')
    def crouch(self):
        print('蹲下')
#创建一个对象
person = Human() # person=人
print('-'*45)
person.go()
print('-'*45)
person.jump()
print('-'*45)
person.crouch()
print('*'*45)

class Weapon:
    def __init__(self,nuwname):
        self.name = nuwname
    def shoot(self):
        print(self.name,'射杀')
    def kill(self):
        print(self.name,'杀伤')
    def blast(self):
        print(self.name,'爆炸')
    def cisha(self):
        print(self.name,'刺杀')
    def store(self):
        print(self.name,'存储')
gun = Weapon('枪')
gun.shoot()
print('-'*40)
bullet = Weapon('子弹')
bullet.kill()
print('-'*40)
grenade = Weapon('手榴弹')
grenade.blast()
print('-'*40)
knife = Weapon('刀')
knife.cisha()
print('-'*40)
box = Weapon('箱子')
box.store()
prin t('-'*40)
