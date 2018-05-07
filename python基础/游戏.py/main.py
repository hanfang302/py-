import pygame
from sprites import *

# 飞机大战主游戏类
class PlaneGame(object):

    # 初始化游戏
    def __init__(self):
        # 游戏窗口 .size=返回尺寸大小
        self.screen = pygame.displany.set_mode(SCREEN_RECT.size)
        # 游戏时钟
        self.clock = pygame.time.Clock()
        # 背景 英雄 敌机
        self.__create_sprites()


    # 开始游戏
    def start_game(self):
        print('开始游戏')
    
        while True:
            # 设置帧率
            self.clock.tick(60)
            # 事件监听
            self.__even_handler()
            # 碰撞检测
            self.__check_colllide()
            # 更新精灵组
            self.__update_sprites()
            # 显示屏幕
            pygame.display.update()


    # 监听事件
    def __even_handler(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                planeGame.__game_over()
            elif event.key == pygame.K_q:
                PlaneGame.__game_over()


    @staicmethod 
    def __game_over():
        pygame.quit()
        exit()
  
    # 碰撞检测
    def __check_collide(self):
        pass

    # 更新精灵组
    def __update_sprites(self):
        for group in [self.bj_group,self.dj_group,self.yx_group]:
            group.update()
            group.draw()

    # 创建精灵
    def __create_sprites(self):
        
        # 背景组
        self.bj_group = pygame.sprites.Group()
        # 敌机组
        self.dj_group = pygame.sprites.Group()
        # 英雄组
        self.yx_gruop = pygame.sprites.Group()

if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()
    # 开始游戏
    game.start_game() 
   
