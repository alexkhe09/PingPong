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
    def update(self):#Создаю метод update, отвечающий за передвижение игрока
        keys_pressed = key.get_pressed()#Получаю информацию о состоянии клавиш
        if keys_pressed[K_LEFT] and self.rect.x >= 5:#Проверяю нажатие стрелки влево и положение корабля по координате х
            self.rect.x -= self.speed#Вычитаю скорость из координаты х
        if keys_pressed[K_RIGHT] and self.rect.x <= 660:#Проверяю нажатие стрелки вправо и положение корабля по координате х
            self.rect.x += self.speed#Прибавляю скорость к координате х
