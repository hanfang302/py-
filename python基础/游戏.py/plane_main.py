# 使用pygame 导用这个游戏包
import pygame
# 导入这个模块所有的类和方法
from plane_sprites import *

# 定义了一个游戏的类
class PlaneGame(object):
    """飞机大战主游戏"""
    def __init__(self):
        print('游戏初始化')

        # 创建游戏的窗口 pygame.display.set_mode(来自pygame这个游戏包) 创建游戏窗口 需要传入宽和高
        # .size 取宽和高 x取x轴的值 y取y轴的值
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建游戏时钟 pygame.time.Clock() 会给我们返回一个时钟对象
        self.clock = pygame.time.Clock()
        # 调用私有方法 里面创建精灵和精灵组
        self.__create_sprites()
        # 设置定时器事件，每秒创建一架敌机(常量(事件)，1000毫秒=1秒)
        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
        # 每隔 0.5秒发射一颗豆
        pygame.time.set_timer(HERO_FIRE_EVENT,500)


    def star_game(self):
        print('开始游戏')
        # 循环这个游戏
        while True:
            # 设置帧率
            self.clock.tick(60)
            # 事件监听
            self.__event_handler()
            # 碰撞检测
            self.__check_collide()
            # 更新精灵组
            self.__update_sprites()
            # 更新屏幕显示
            pygame.display.update()

    
    def __create_sprites(self):
        """创建精灵和精灵组"""
        # pygame.sprites.Group()可以创建一个精灵组 Group返回一个列表
        # 背景精灵组
        bg1 = Backgroup('/home/hanfang/桌面/python基础/游戏.py/images/background.png')
        bg2 = Backgroup('/home/hanfang/桌面/python基础/游戏.py/images/background.png')
        bg2.rect.y = -bg2.rect.height
        self.back_group = pygame.sprite.Group(bg1,bg2)
        # 敌方精灵组
        self.enemy_group = pygame.sprite.Group()
        # 英雄精灵组
        # 实例化一个精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def __event_handler(self):
        """事件监听方法"""
        # pygame.event.get()获取事件列表
        # 获取完列表以后 写了一个for循环，循环这个pygame包里面的事件列表 
        for event in pygame.event.get():
            # 当列表里面有pygame.QUIT常量
            # 如果这个事件的类形 等于 pygame这个游戏包里面QUIT这个方法，那么退出这个游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            # 如果这个事件类型 等于 （敌机，创建一架敌机）用户事件，那么就在对象调用游戏中相关的方法中操作用户相关的事件（定时器事件发生）
            elif event.type == CREATE_ENEMY_EVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            #elif event.type == pygame.KEYDOWN and event.key == pygame.K
                #print
            #另外一个方案(返回所有的按)
            key_pressed = pygame.key.get_pressed()

            if key_pressed[pygame.K_RIGHT]:
                #print('向右移动')
                self.hero.speed = 2
            elif key_pressed[pygame.K_LEFT]:
                self.hero.speed = -2
                #print('向左移动')
            else:
                self.hero.speed = 0



    def __check_collide(self):
        """碰撞检测"""
        # 子弹摧毁飞机
        pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)
        # 英雄撞到敌机
        enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
        
        # 判断列表是否有内容
        if len(enemies) > 0:
            # 让英雄牺牲
            self.hero.kill()
            # 结束游戏
            PlaneGame.__game_over()


    def __update_sprites(self):
        """更新精灵组""" 
        for group in [self.back_group,self.enemy_group,self.hero_group,self.hero.bullets]:
            # 更新精灵组里面所有精灵所在的位置
            group.update()
            # 绘制到屏幕上
            group.draw(self.screen)
        


    # 静态方法，可以不用传参数
    @staticmethod
    def __game_over():
        """游戏结束"""
        print('游戏结束')
        pygame.quit()
        exit()
        pass



# 一般情况下，在场景下进行测试 具体内容只有自己能看到
if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()
    # 调用游戏开始的方法
    game.star_game()
