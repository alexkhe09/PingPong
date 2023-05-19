from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y >= 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y <= 420:
            self.rect.y += self.speed

    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y >= 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y <= 420:
            self.rect.y += self.speed

window = display.set_mode((700, 500))
display.set_caption('Ping Pong')
background = transform.scale(image.load('background.png'), (700, 500))
game = True
racket_r = Player('racket.png', 665, 220, 25, 75, 5)
racket_l = Player('racket.png', 10, 220, 25, 75, 5)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    racket_r.update_r()
    racket_l.update_l()

    window.blit(background, (0, 0))
    racket_r.reset()
    racket_l.reset()

    time.delay(50)
    display.update()
