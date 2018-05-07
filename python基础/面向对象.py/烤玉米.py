class Corn:
    def __init__(self):
        self.cookedLever = '0'
        self.cookedString = '生的'
    def cook(self,time):
        self.cookedLever += time
        if self.cookedLever > 3:
            self.cookedString = '半生不熟'
        elif self.cookedLever > 5:
            self.cookedString = '烤好了，正合适'
        elif self.cookedLever > 8:
            self.cookedString = '烤过时了，烤焦了'
        else:
            self.cookedString = '生的'
yumi = Corn()
print('---有一个生玉米，还没有烤---')
print(yumi.cookedLever)
print(yumi.cookedString)
print('接下来进行烤玉米')
yumi.cook(4)
print(yumi)
print('*'*50)
print('玉米又考了3分钟')
yumi.cook(3)
print(yumi)
print('*'*50)
print('玉米又考了3分钟')
yumi.cook(3)
print(yumi)

