import sys

import pygame  # импортируем библиотеку pygame
from random import *

class Food():
    def __init__(self, name_image, x, y):  # конструктор, создание свойств, self - ОБЪЕКТ
        self.image = pygame.image.load(name_image)  # создание картинки, ЭТО СВОЙСТВО
        self.rect = self.image.get_rect()  # создание прямямоугольника по границам картинки, ЭТО СВОЙСТВО
        self.rect.x = x  # координата x для картинки, ЭТО СВОЙСТВО
        self.rect.y = y # координата y для картинки, ЭТО СВОЙСТВО

    def draw_image(self):  # метод отрисовки картинки
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def move_plate(self): #метод движения тарелки
        keys = pygame.key.get_pressed() #получение списка нажатых клавишь
        if keys[pygame.K_LEFT] == True:#если нажата клавиша влево
            self.rect.x -= 10
        if keys[pygame.K_RIGHT]:#если нажата клавиша вправо
            self.rect.x += 10

    def move_food(self):#метод движения eды
         self.rect.y += 9

fon = Food("fon.jpg", 0, 0)#СОЗДАНИЕ ФОНА
pygame.init()  # обязательная команда
window_size = (1420, 780)  # размеры окна
screen = pygame.display.set_mode(window_size)  # создание экрана с размерами
monster1= Food("дверь.png", 300, 650)  # создание объекта класса Food
monster2= Food("монстр1.png", 200, randint(-1000,0))  # создание объекта класса Food
monster3 = Food("монстр2.png", 450, randint(-490,0))  # создание объекта класса Food
monster4 = Food("монстр3.png", 650, randint(-700,0))  # создание объекта класса Food
monster5 = Food("монстр4.png", 850,randint(-250,0) )  # создание объекта класса Food

food_list = [monster2, monster3, monster4, monster5]


clock = pygame.time.Clock()  # создание игрового таймера

while True:  # игровой цикл
    clock.tick(20)  # 40фпс\с
    fon.draw_image()  # применение метода отрисовки к объекту класса Food
    for i in food_list:
        i.draw_image()
        i.move_food()
        if monster1.rect.colliderect(i.rect):
            food_list.remove(i)
        if i.rect.y > 700:
           i.rect.y=0
    if food_list == []:
        fon = Food("ура.jpg", 200, 200)  # СОЗДАНИЕ ФОНА
        monster1.rect.y = -100
        monster1.rect.x = -100
    monster1.draw_image()  # применение метода отрисовки к объекту класса Food
    monster1.move_plate()
    for event in pygame.event.get():  # проходимся по событиям
        if event.type == pygame.QUIT:  # если нажали на крестик
            sys.exit() # выход из игры
    pygame.display.update()# обновление содержимого экрана


