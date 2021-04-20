# Реализуйте класс MoneyBox, для работы с виртуальной копилкой.

# Каждая копилка имеет ограниченную вместимость, которая выражается целым числом – количеством монет, 
# которые можно положить в копилку. Класс должен поддерживать информацию о количестве монет в копилке, 
# предоставлять возможность добавлять монеты в копилку и узнавать, 
# можно ли добавить в копилку ещё какое-то количество монет, не превышая ее вместимость.

# Класс должен иметь следующий вид

# class MoneyBox:
#     def __init__(self, capacity):
#         # конструктор с аргументом – вместимость копилки

#     def can_add(self, v):
#         # True, если можно добавить v монет, False иначе

#     def add(self, v):
#         # положить v монет в копилку
# При создании копилки, число монет в ней равно 0.
# Примечание:
# Гарантируется, что метод add(self, v) будет вызываться только если can_add(self, v) – True﻿.

# Создаем наш класс
class MoneyBox:
    # функция, которая инициируется, при создании экземпляра класса
    def __init__(self, capacity):
        # задаем вместимость и первоначальное заполнение копилке (0 монет)
        self.capacity = capacity
        self.fullness = 0

    # в этом методе определяем способна ли копилка вместить еще v монет
    def can_add(self, v):
        return self.fullness + v <= self.capacity

    # метод, предназначенный для добавления в копилку v монет
    def add(self, v):
        # проверяем, влезут ли наши монеты в копилку
        # обратить внимание, что при вызове метода внутри метода
        # мы не передаем self, в качестве аргумента
        if self.can_add(v):
            # если монеты помещаются, добавляем их к существующему количеству
            self.fullness += v