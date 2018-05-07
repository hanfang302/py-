class Kao_di_gua:
    def __init__(self):
        self.Sheng_shu = 0
        self.Sheng_shu_du = '生的'
    def Kao(self,time):
        self.Sheng_shu += time
        if self.Sheng_shu > 8:
            self.Sheng_shu_du = '烤过时了，烤黑了'
        elif self.Sheng_shu > 5:
            self.Sheng_shu_du = '烤好了'
        elif self.Sheng_shu >3:
            self.Sheng_shu_du = '半生不熟'
        else:
            self.Sheng_shu_du = '生的'
kdg = Kao_di_gua()
print('----有了一个地瓜，准备烤地瓜----')
#print(kdg.Sheng_shu)
print(kdg.Sheng_shu_du)
print('----地瓜已经烤2分钟了----')
kdg.Kao(2)
print(kdg.Sheng_shu_du)
print('----地瓜又烤了4分钟----')
kdg.Kao(4)
print(kdg.Sheng_shu_du)
print('----地瓜又烤了4分钟----')
kdg.Kao(4)
iprint(kdg.Sheng_shu_du)
