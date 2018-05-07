# 导入 pygame 这个第三方的游戏包
import pygame
# 导入这个模块所有的类和方法
from profile import *

# 定义一个类(飞机游戏)
class PlaneGame(object): 
    """飞机大战的主游戏"""

    def __init__(self):
        print('游戏的初始化')

        # 创建游戏的窗口 pygame.display.set_mode()是pygame自带的一个创建游戏窗口的功能，需要传入值（宽和高）
        # screen = 屏幕 size=取宽和高
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)      
        # 设置游戏的时钟
        self.clock = pygame.time.Clock()
        # 创建精灵和精灵组
        self.__create_sprites()
        # 创建用户事件(常量(事件 创建一架敌机)，时间 1000毫秒=1秒)
        pygame.time.set_timer(ENEMY_EVENT,1000)



        # 开始游戏
    def star_game(self):
        print('开始游戏')

        # 游戏开始后，不会立即退出游戏
        while True:

            # 设置时间的帧率 tick(设置帧率的方法)
            self.clock.tick(60)        
            # 事件监听（按键，鼠标等行为）
            self.__event_handler()
            # 碰撞检测
            self.__check_collide()
            # 更新图像(精灵)的位置 sprites = 精灵
            self.__update_sprites()
            # 更新屏幕的显示 对象在调用完所有的方法以后 最后统一调用pygame这个包里的 屏幕更新方法
            pygame.display.update()

    # 创建精灵和精灵组
    def __create_sprites(self):
        # 创建背景精灵
        bj1 = Backgroup('/home/hanfang/桌面/python基础/游戏.py/images/background.png')
        bj2 = Backgroup('/home/hanfang/桌面/python基础/游戏.py/images/background.png')
        bj2.rect.y = -bj2.rect.height

        self.back_group = pygame.sprite.Group(bj1, bj2)

        # 创建敌机精灵组
        # 敌机组 = pygame这个包里的精灵组
        self.enemy_group = pygame.sprite.Group()

         

    # 事件监听
    def __event_handler(self):
        # pygame.event.get()可以获得当前时刻的所有事件列表 遍历列表
        for event in pygame.event.get():
            # 判断是否退出如果这个事件的类型 等于 这个游戏包里的QUIT 那么就退出
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            # 如果事件的类型 等于 用户这个事件 那么敌机就出场
            elif event.type == ENEMY_EVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)


    # 碰撞检测
    def __check_collide(self):
        pass




    # 精灵组更新和绘制
    def __update_sprites(self):
        for group in [self.back_group,self.enemy_group]:

            # 更新精灵所在的位置
            group.update()
            # 绘制到屏幕上
            group.draw(self.screen)

        


        # 结束游戏
    def game_over():
        print('结束游戏')
        # 在结束游戏之前必须调用
        pygame.quit()
        # 直接退出游戏
        exit()
        pass



# 一般，在场景下进行;只有自己（后台）能看得见，
if __name__ == '__main__':
    # 创建一个对象
    game = PlaneGame()
    # 对象调用游戏开始
    game.star_game()
    #game.end_game()
