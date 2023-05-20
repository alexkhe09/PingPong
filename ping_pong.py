from pygame import *
from math import floor

class GameSprite(sprite.Sprite): #Создаю класс GameSprite(наследник класса Sprite)
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed): #Создаю конструктор класса, передаю картинку спрайта, скорость, ширину, выстоу, x, y
        super().__init__() #Вызываю конструктор суперкласса
        self.image = transform.scale(image.load(player_image), (player_width, player_height))#Создаю и сохраняю картинку в переменной
        self.speed = player_speed #Сохраняю скорость в переменную
        self.rect = self.image.get_rect() #Создаю rect
        self.rect.x = player_x #Сохраняю координату x в переменной
        self.rect.y = player_y #Сохраняю координату y в переменной

    def reset(self):#Создаю метод отрисовк спрайта
        window.blit(self.image, (self.rect.x, self.rect.y))#Отрисовываю спрайт на окне

class Player(GameSprite):#Создаю класс Player
    def update_r(self):#Создаю метод update, отвечающий за передвижение игрока
        keys_pressed = key.get_pressed()#Получаю информацию о состоянии клавиш
        if keys_pressed[K_UP] and self.rect.y >= 0:#Проверяю нажатие стрелки влево и положение корабля по координате х
            self.rect.y -= self.speed#Вычитаю скорость из координаты х
        if keys_pressed[K_DOWN] and self.rect.y <= 425:#Проверяю нажатие стрелки вправо и положение корабля по координате х
            self.rect.y += self.speed#Прибавляю скорость к координате х

    def update_l(self):#Создаю метод update, отвечающий за передвижение игрока
        keys_pressed = key.get_pressed()#Получаю информацию о состоянии клавиш
        if keys_pressed[K_w] and self.rect.y >= 0:#Проверяю нажатие стрелки влево и положение корабля по координате х
            self.rect.y -= self.speed#Вычитаю скорость из координаты х
        if keys_pressed[K_s] and self.rect.y <= 425:#Проверяю нажатие стрелки вправо и положение корабля по координате х
            self.rect.y += self.speed#Прибавляю скорость к координате х
'''
class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed_x, player_speed_y):
        super().__init__(player_image, player_x, player_y, player_width, player_height, player_speed_x)
        self.player_speed_x = player_speed_x
        self.player_speed_y = player_speed_y
    
    def update(self):
        self.rect.x += self.player_speed_x
        self.rect.y += self.player_speed_y
        if self.rect.y <= 0 or self.rect.y >= 445:
            self.player_speed_y *= -1
        if self.rect.x <= 0 or self.rect.x >= 645:
            self.player_speed_x *= -1
'''
window = display.set_mode((700, 500))
display.set_caption('Ping Pong')
background = transform.scale(image.load('background.png'), (700, 500))
ball = GameSprite('4892516.png', 300, 300, 55, 55, 5)
racket_r = Player('racket.png', 655, 200, 25, 75, 7)
racket_l = Player('racket.png', 20, 200, 25, 75, 7)
speed_x = 5
speed_y = 5
font.init()
aaaaaa = font.SysFont('Arial', 48)
win_r = aaaaaa.render('ПРАВЫЙ ИГРОК ПОБЕДИЛ!', True, (255, 150, 0))
win_l = aaaaaa.render('ЛЕВЫЙ ИГРОК ПОБЕДИЛ!', True, (255, 150, 0))
game = True
finish = False
FPS = 30
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False

    if finish != True:
        racket_l.update_l()
        racket_r.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y <= 0 or ball.rect.y >= 445:
            speed_y *= -1
        if sprite.collide_rect(racket_r, ball) or sprite.collide_rect(racket_l, ball):
            speed_x *= -1
            FPS -= 0.5

        window.blit(background, (0, 0))
        ball.reset()
        racket_l.reset()
        racket_r.reset()

        if ball.rect.x <= -55:
            finish = True
            window.blit(win_r, (100, 150))
        if ball.rect.x >= 700:
            finish = True
            window.blit(win_l, (100, 150))

    time.delay(floor(FPS))    
    display.update()