#Создай собственный Шутер!

from pygame import *
from random import *
from time import time as timer #импортирую функцию для засикания времени чтобы интерпритатор не искал эту функцию в pygame даем ей новое название сами


window = display.set_mode((700,500))
display.set_caption('Шутер')

back = (135, 206, 250)
window.fill(back)



clock = time.Clock()
FPS = 60

class  GameSprite(sprite.Sprite):
    def __init__(self, player_image,  player_x, player_y, player_speed,x,y):
        super().__init__() #x and y ширена и высота
        self.image = transform.scale(image.load(player_image),(x,y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 645:
            self.rect.x += self.speed
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_s] and self.rect.x < 445:
            self.rect.x += self.speed
        






hero = Player('wall.png', 25 , 50, 10 , 25, 190)

hero_2 = Player('wall.png', 650 , 50, 10 , 25, 190)


game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    


    if finish != True:
       
        hero.reset()
        hero.update()

        hero_2.reset()
        hero_2.update()


    display.update()
    clock.tick(FPS)
    