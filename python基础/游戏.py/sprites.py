import pygame

# 游戏屏幕的大小
SCREEN_RECT = pygame.Rect(0,0,480,700)

# 基类
class GameSprite(pygame.sprite.Sprite):
 
    def __init__(self.image_url,speed):
        # 调用父类初始化方法
        super().__init__()

        self.inmage_url = pygame.image.load(image_url)
        self.speed = speed
        self.rect = self.image_url.get_rect()

    def update(self):
        self.rect.y += self.speed


# 英雄类
class Hreo(GameSprites):

    def __init__(self.image_url,speed=0)
        super().__init__(image_url,speed)


    def update(self):
        pass



# 背景类
class Background(GameSprites):
    def __init__(self.image_url,speed=1):
        super().__init__(image_url)

    def update(self):
        pass



