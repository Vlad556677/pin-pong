#Создай собственный Шутер!

from pygame import *
from random import *
from time import time as timer #импортирую функцию для засикания времени чтобы интерпритатор не искал эту функцию в pygame даем ей новое название сами


window = display.set_mode((700,500))
display.set_caption('Пин понг')

fon = transform.scale(image.load('rrgg.png'),(700,500))

font.init()
font = font.Font(None, 70)


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
    def update_w(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
    def update_s(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_s] and self.rect.y < 480:
            self.rect.y += self.speed
    def update_k_w(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
    def update_k_s(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_DOWN] and self.rect.y < 480:
            self.rect.y += self.speed






hero = Player('wall.png', 25 , 100, 10 , 25, 100)

hero_2 = Player('wall.png', 650 , 100, 10 , 25, 100)

boll = GameSprite('boll.png',50,290,10,50,50)

speed_x = 3
speed_y = 3 



game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False


    lose = font.render('PLAYER 1', True, (255,215,0))
    lose_2 = font.render('PLAYER 2 ', True, (255,215,0))
    lose_g = font.render('GAME OVER', True, (255,215,0))

    if boll.rect.y < 0 or boll.rect.y > 450:
        speed_y *= -1 
    
    if boll.rect.x > 685: 
        finish = True
        window.blit(lose_2,(250,200))
        window.blit(lose_g,(200,300))
    if boll.rect.x < 0:
        finish = True
        window.blit(lose,(250,200))
        window.blit(lose_g,(200,300))
    if sprite.collide_rect (hero, boll):
        speed_x *= -1 

    if sprite.collide_rect (hero_2, boll):
        speed_x *= -1 

        


    if finish != True:
        window.blit(fon,(0,0))
        
        boll.rect.x += speed_x
        boll.rect.y += speed_y

        boll.reset()

        hero.reset()
        hero.update_w()
        hero.update_s()

        hero_2.reset()
        hero_2.update_k_w()
        hero_2.update_k_s()
    
    display.update()
    clock.tick(FPS)
pygame.display.update()
    
