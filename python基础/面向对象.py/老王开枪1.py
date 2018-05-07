# 创建一个人类
class Ren:
    def __init__(self,name):
        self.name = name
        self.xue = 100
        self.qiang = None

    def __str__(self):
        return self.name + '现有血量:' + str(self.xue)

    # 方法
    def anzidan(self,danjia,zidan):
        danjia.baocunzidan(zidan)

    def andanjia(self,qiang,danjia):
        qiang.anzhuangdanjia(danjia)

    def naqiang(self,qiang):
        self.qiang = qiang

    def kaiqiang(self,zidan):
        self.qiang.she(zidan)

    def diaoxue(self,shanghaili):
        self.xue = shanghaili

# 创建子弹类
class Zidan:
    def __init__(self,shashangli):
        self.shashangli = shashangli

    def shanghaili(self,diren):
        diren.diaoxue(self.shanghaili)

# 创建弹夹类
class Danjia:
    def __init__(self,rongliang):
        self.rongliang = rongliang
        self.rongliangList = []

    def __str__(self):
        return '当前子弹的数量:' +  str(len(self.rongliangList)) + '/' + str(self.rongliang)

    def baocunzidan(self,zidan):
        if len(self.rongliangList) < self.rongliang:
            self.rongliangList.append(zidan)

    def tanchuzidan(self):
        if len(self.rongliangList) > 0:
            zidan = self.rongliangList[-1]
            self.rongliangList.pop()
            return zidan

# 创建一个枪类
class Qiang:
    def __init__(self):
        self.danjia = None

    def __str__(self)
        if self.danjia:
            return '枪有弹夹'
        else:
            return '枪没有弹夹'

    def lianjiedanjia(self,danjia):
       if not self.danjia:
           self.danjia = danjia

    def shezidan(self,diren):
        zidan = self.dianjia.cunzian
        if zidan:
            zidan.shanghai(zidan)
        else:
            print('没有子弹了') 


# 创建一个人类
laowang = Ren('老王')

# 创建一个弹夹
danjia = Danjia(20)
print(danjia)

i=0
while i<5:
    zidan = Zidan(5)
    laowang.anzidan(danjia,zidan)
    i += 1
print(danjia)          
