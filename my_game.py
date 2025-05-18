import sys

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
        if keys [pygame.K_UP]: # если нажата клавиша вниз
            self.rect.y -= 5
        if keys [pygame.K_DOWN]: # если нажата клавиша вниз
            self.rect.y += 5

    def move_monster(self):
        self.rect.y += 5




fon = Sprites("Лес.png", 0, 0)# создание фона

window_size = (1000, 750)  # размеры окна
screen = pygame.display.set_mode(window_size)  # создание экрана с размерами
Rendel = Sprites("Rendel1.png", 200, 240)  # создание объекта класса Sprites
Hunter = Sprites( "Hunter1.png", 450, 550) # создание объекта класса Sprites
Salivan = Sprites( "Salivan1.png", 500, 0) # создание объекта класса Sprites
Crystal = Sprites( "Crystal.png", 450, 0) # создание объекта класса Sprites
speed_Rendel = -5
speed_Salivan = 5

clock = pygame.time.Clock()  # создание игрового таймера

while True:  # игровой цикл
    fon.draw_image()
    Rendel.rect.x += speed_Rendel
    if Rendel.rect.x >= 750 or Rendel.rect.x <= 0:
        speed_Rendel *= (-1)

    Salivan.rect.x += speed_Salivan
    if Salivan.rect.x >= 750 or Salivan.rect.x <= 0:
        speed_Salivan *= (-1)

    if Hunter.rect.colliderect(Rendel.rect) or Hunter.rect.colliderect(Salivan.rect):
        Hunter.rect.x = 450
        Hunter.rect.y = 550

    if Hunter.rect.colliderect(Crystal.rect):
        fon = Sprites("УРА1.jpg", 100, 0)  # создание фона
        Rendel.rect.x = -450
        Rendel.rect.y = -550
        Salivan.rect.x = -450
        Salivan.rect.y = -550
        speed_Rendel=0
        speed_Salivan=0
        Hunter.rect.y = -100

    clock.tick(40)  # 40фпс\с

    Crystal.draw_image()
    Rendel.draw_image()
    Salivan.draw_image()
    Hunter.draw_image()
    Hunter.move_Hunter()
    pygame.display.update()  # обновление содержимого экрана
    for event in pygame.event.get():  # проходимся по событиям
        if event.type == pygame.QUIT:  # если нажали на крестик
            sys.exit()  # выход из игры
