# 系统模块
import random
# 第三方模块
import pygame


# 游戏屏幕的大小(描述一个窗口需要四个因素 x轴 y轴 宽 高)
SCREEN_RECT = pygame.Rect(0,0,480,700)

# 敌机的定时器事件常量
EVEMY_EVENT = pygame.USEREVENT



# 创建一个精灵组
class GameSprite(pygame.sprite.Sprite):
    
    def __init__(self,image_name,speed=1):
        # 调用父类的初始化方法
        super().__init__()
    # 属性
        # 加载图像
        self.image = pygame.image.load(image_name)
        # 图像(精灵)大小
        self.rect = self.image.get_rect()
        # 移动的速度        
        self.speed = speed

    # 方法
    def update(self):
        # 图像向下移动
        self.rect.y += self.speed


# 创建一个背景组 继承精灵组
class Backgroup(GameSprite):
    
    def update(self):
        # 直接调用父类的方法
        super().update()
 
        # 判断背景图片是否飞出了区域 如果飞出了矩形区域将图像设置到区域上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


# 创建一个敌机类继承精灵组
class Enemy(GameSprite):

    def __init__(self):
        # 调用父类的方法，创建敌机的精灵 并且指定敌机图像
        super().__init__('/home/hanfang/桌面/python基础/游戏.py/images/enemy1.png')
        # 敌机随机数度 randint(随机)
        self.speed = random.randint(1,3)

        # 敌机的随机位置
        self.rect.bottom = 0
        # 敌机在x轴活动的最大范围
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random,randint(0, max_x) 


    def update(self):

        super().update()
        # 判断是否飞出屏幕外
        if self.rect.y >= SCREEN_RECT.height:
            #print('敌机飞出屏幕')
            # 删除，当敌机飞出屏幕并不是删除，内存中一直存在。当达到一定容量..
            self.kill()

    def __del__(self):
        print('敌机删除%s'%self.rect)




