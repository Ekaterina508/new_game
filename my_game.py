import pygame # импортируем библиотеку pygame

pygame.init()
class Sprites():
    def __init__(self, name_image, x, y):  # конструктор, создание свойств
        self.image = pygame.image.load(name_image)  # создание картинки, ЭТО СВОЙСТВО
        self.rect = self.image.get_rect()  # создание прямямоугольника по границам картинки, ЭТО СВОЙСТВО
        self.rect.x = x  # координата x для картинки, ЭТО СВОЙСТВО
        self.rect.y = y  # координата y для картинки, ЭТО СВОЙСТВО

    def draw_image(self):  # метод отрисовки картинки
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def move_Hunter(self):
        keys = pygame.key.get_pressed() # получение списка нажатых клавиш
        if keys[pygame.K_LEFT] == True: # если нажата клавиша влево
            self.rect.x -= 5
        if keys [pygame.K_RIGHT]: # если нажата клавиша вниз
            self.rect.x += 5

    def move_monster(self):
        self.rect.y += 5



fon = Sprites("Лес.png", 0, 0)# создание фона
window_size = (1000, 750)  # размеры окна
screen = pygame.display.set_mode(window_size)  # создание экрана с размерами
Rendel = Sprites("Rendel1.png", 200, 0)  # создание объекта класса Sprites
Hunter = Sprites( "Hunter1.png", 400, 500) # создание объекта класса Sprites
Salivan = Sprites( "Salivan1.png", 500, 0) # создание объекта класса Sprites
Bomb = Sprites( "Bomb1.png", 500, 300) # создание объекта класса Sprites
Sprites_list = [Rendel,Hunter,Salivan,Bomb]

clock = pygame.time.Clock()  # создание игрового таймера

while True:  # игровой цикл
    fon.draw_image()  # применение метода отрисовки к объекту класса Sprites
    clock.tick(40)  # 40фпс\с
    for i in Sprites_list:
        i.draw_image()
        i.move_Hunter()
    Hunter.draw_image()  # применение метода отрисовки к объекту класса Sprites
    Hunter.move_Hunter()
    pygame.display.update()  # обновление содержимого экрана
    for event in pygame.event.get():  # проходимся по событиям
        if event.type == pygame.QUIT:  # если нажали на крестик
            pygame.QUIT()  # выход из игры
    pygame.display.update()