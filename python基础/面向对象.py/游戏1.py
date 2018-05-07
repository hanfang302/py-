class People:
    def __init__(self):
        self.name = '人'
        print(self.name)
    def go(self):
        print('走')
    def jump(self):
        print('跳')
    def run(self):
        print('跑')
    def hide(self):
        print('躲')
human = People()
human.go()
human.jump()
human.run()
human.hide()
class Goods:
    def __init__(self,nawName):
        self.name = nawName
    def qiang(self):
        print(self.name,'射杀')
    def zidan(self):
        print(self.name,'射杀')
    def sld(self):
        print(self.name,'爆炸')
    def daozi(self):
        print(self.name,'刺杀')
    def xiangzi(self):
        print(self.name,'储备')
weapon = Goods('枪')
weapon.qiang()
bullet = Goods('子弹')
bullet.zidan()
G = Goods('手榴弹')
G.sld()
knife = Goods('刀子')
knife.daozi()
box = Goods('箱子')
box.xiangzi()

