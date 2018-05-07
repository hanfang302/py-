class Human:
    def __init__(self,newpifu='黑色'):
        self.__pifu = newpifu
        self.bizi = '扁'
    def Shu_chu(self):
        print(self.__pifu)
        print(self.bizi)
    def Xiu_gai(self,newColor):
        self.__pifu = newColor
    
zhang_Shan = Human()
zhang_Shan.Shu_chu()
zhang_Shan.bizi = '高高的'
print('失败后的整容')
