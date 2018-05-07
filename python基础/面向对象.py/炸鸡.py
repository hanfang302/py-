class Zha_ji:
    def __init__(self):
        self.sheng_shu = 0
        self.sheng_shu_du = '生的'
    def fride(self,time):
        self.sheng_shu += time
        if self.sheng_shu > 3:
            self.sheng_shu_du ='半生不生'
        elif self.sheng_shu > 5:
            self.sheng_shu_du ='刚刚好，口味最佳'
        elif self.sheng_shu > 10:
            self.sheng_shu_du ='炸鸡炸焦了'
        else:
            self.sheng_shu_du ='生的'

zj = Zha_ji()
print('---------炸鸡----------')
print(zj.sheng_shu_du)
print('---已经炸了两分钟---')
zj.fride(2)
print(zj.sheng_shu_du)
print('---炸了五分钟---')
zj.fride(5)
print(zj.sheng_shu_du)
print('----又炸了五分钟----')
zj.fride(5)
print(zj.sheng_shu_du)
