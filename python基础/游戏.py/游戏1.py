import pygame
# 开始
pygame.init()
# display(窗口) 类
# set_mode() 方法 初始化我们的显示窗口
# update()方法 刷新我没们的屏幕
# 屏幕
screen = pygame.display.set_mode((420,700))
# image.load
# 加载图片数据
bg = pygame.image.load('/home/hanfang/桌面/python基础/游戏.py/images/background.png')
# 绘制图片数据
screen.blit(bg,(0,0))
# 更新显示
pygame.display.update()

hero_fly = pygame.image.load('/home/hanfang/桌面/python基础/游戏.py/images/me1.png')
hero_rect = pygame.Rect(200,600,102,126)
screen.blit(hero_fly,hero_rect)
#pygame.display.update()

#创建敌方飞机
enemy1 = GameSprite('/home/hanfang/桌面/python基础/游戏.py/images/enemy1.png')
enemy1.rect.x = 50
enemy1.rect.y = 50

# 把敌机添加到精灵组
enemy_Group = pygame.sprite.Group(enemy1)
enemy_Group.update()
enemy_Group.draw(screen)
pygame.display.update()

# 游戏时钟
clock = pygame.time.Clock()

while True:
          #帧率
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('退出游戏')
            pygame.quit()
            exit()
    if hero_rect.y == 0:
        hero_rect.y = 600
    else:
        hero_rect.y = hero_rect.y - 1

    # 重新设置一下背景
    screen.blit(bg,(0,0))
    # 绘制英雄的坐标
    screen.blit(hero_fly,hero_rect)
    enemy_Group.update()
    enemy_Group.draw(screen)
    # 更新屏幕
    pygame.display.update()
# 结束
pygame.quit()

