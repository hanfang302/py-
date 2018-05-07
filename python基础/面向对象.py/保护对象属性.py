class People:
    def __init__(self,newpifu='黑色'):
        self.__pifu = newpifu
        self.eyes = '蓝色'
    def shuChu(self):
        print(self.__pifu)
        print(self.eyes)
    def xiuGai(self,newColor):
        self.__pifu = newColor
    def duQu(self):
        return self.__pifu

    def __del__(self):
        print('已经死啦')
   
Lisi = People()
Lisi.shuChu()
#Lisi.__pifu = '白色'
Lisi.eyes = '灰色'
print('-'*50)
print('整容失败')
Lisi.shuChu()
print('-'*50)
print('去韩国再次整容')
Lisi.xiuGai('白色')
Lisi.shuChu()
Lisi.duQu()
print('-'*50)
del Lisi
