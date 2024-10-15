# class Figure:
#     sides_count = 0  # счет сторон
#
#     def __init__(self, __sides, __color, filled: bool):
#         self.__sides = []  # (список сторон(целые числа))
#         self.__color = []  # (список цветов в RGB)
#         self.filled = filled  # (закрашенный, bool)
#
#     # def get_color(self, r, g, b):  # должен возвращать список RGB цветов
#     #     self.__is_valid_color(r, g, b)
#     #     var = self.__color
#     #     return var
#     #
#     # # def __is_valid_color(self, r, g, b):
#     # #     if (not isinstance(r, int) or r < 0 or r > 255 and not isinstance(g, int) or g < 0 or g > 255
#     # #             and not isinstance(b, int) or b < 0 or b > 255):
#     # #         raise ValueError("Значение должно быть целым положительным числом в диапазоне от 0 до 255")
#     # #     self.values = r
#     # #     self.values = g
#     # #     self.values = b
#     #
#     # def __is_valid_color(self, r, g, b):
#     #     if not all(isinstance(x, int) and x > 0 or x > 255 for x in (r, g, b)):
#     #         raise ValueError("Значение должно быть целым положительным числом в диапазоне от 0 до 255")
#     #
#     #
#     #
#     #  def set_color(self, r, g, b):
#     #     self.__is_valid_color()
#     #     pass
#
# d = Figure()
# print(1, d.get_color(25, 7, 8))
# #
# # circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
# # cube1 = Cube((222, 35, 130), 6)
# #
# # # Проверка на изменение цветов:
# # circle1.set_color(55, 66, 77) # Изменится
# # print(circle1.get_color())
# # cube1.set_color(300, 70, 15) # Не изменится
# # print(cube1.get_color())
# #
# # # Проверка на изменение сторон:
# # cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
# # print(cube1.get_sides())
# # circle1.set_sides(15) # Изменится
# # print(circle1.get_sides())
# #
# # # Проверка периметра (круга), это и есть длина:
# # print(len(circle1))
# #
# # # Проверка объёма (куба):
# # print(cube1.get_volume())

# from math import pi
#
#
# class Figure:
#     sides_count = 0  # счет сторон , для фигур будем переопределять
#
#     def __init__(self, __sides: int, __color, filled: bool):
#         self.new_sides = None
#         self.__sides = []  # (список сторон(целые числа))
#         self.__color = []  # (список цветов в RGB)
#         self.filled = filled  # (закрашенный, bool)
#
#     def get_color(self):  # геттер - возврат списа цветов
#         return self.__color
#
#     def __is_valid_color(self, r, g, b):
#         return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))
#
#     def set_color(self, r, g, b):  # сеттер цвет (меняем)
#         if self.__is_valid_color(r, g, b):
#             self.__color = (r, g, b)
#         else:
#             raise ValueError("Значение должно быть целым положительным числом в диапазоне от 0 до 255")
#
#     def get__sides(self):  # геттер cписка сторон (возвращаем)
#         return self.__sides
#
#     def __is_valid_sides(self, *__sides: int):
#         return all(isinstance(side, int) and side > 0 for side in __sides)
#
#     def set_sides(self, *new_sides):  # сеттер списка сторон (изменяем)
#         if self.__is_valid_sides(*new_sides):
#             self.__sides = list(new_sides)
#         else:
#             raise ValueError("Все стороны должны быть положительными целыми числами")
#
#
#     def __str__(self):
#         return f"Геометрическая фигура с {self.sides_count} сторонами"
#
#     def __len__(self):  # периметр фигуры
#         return sum(self.__sides)
#
#
#
# class Circle(Figure):
#     sides_count = 1
#
#     # def __init__(self, color=(0, 0, 0), radius=1, filled: bool = False):
#     #     super().__init__(self.sides_count, color, filled)
#     #     self.radius = radius
#
#     def __init__(self, color=(0, 0, 0), radius=None, filled: bool = None):
#         super().__init__(self.sides_count, color, filled)
#         self.radius = self.sides_count
#         self.radius = radius
#         self.filled = self.filled = False
#
#     def get_square(self):
#         return pi * self.radius ** 2
#
#     # d = Figure(3, 2, True)
#
#
# # print(d.get__sides(), d.get_color(), d.filled)
#
#
# #
# circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
#
# # cube1 = Cube((222, 35, 130), 6)
# #
# # # Проверка на изменение цветов:
# # circle1.set_color(55, 66, 77) # Изменится
# print(circle1.get_color())
# # cube1.set_color(300, 70, 15) # Не изменится
# # print(cube1.get_color())
# #
# # # Проверка на изменение сторон:
# # cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
# # print(cube1.get_sides())
# # circle1.set_sides(15) # Изменится
# # print(circle1.get_sides())
# #
# # # Проверка периметра (круга), это и есть длина:
# print(len(circle1))
# #
# # # Проверка объёма (куба):
# # print(cube1.get_volume())

""" Классы фигуры и круг"""

# from math import pi
# import math
#
# class Figure:
#     sides_count = 0  # счет сторон , для фигур будем переопределять
#
#     def __init__(self, __sides: int, __color, filled: bool):
#         self.new_sides = None
#         self.__sides = []  # (список сторон(целые числа))
#         self.__color = []  # (список цветов в RGB)
#         self.filled = filled  # (закрашенный, bool)
#
#     def get_color(self):  # геттер - возврат списkа цветов
#         return self.__color
#
#     def __is_valid_color(self, r, g, b):
#         return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))
#
#     def set_color(self, r, g, b):  # сеттер цвет (меняем)
#         if self.__is_valid_color(r, g, b):
#             self.__color = (r, g, b)
#         # else:
#         #     raise ValueError("Значение должно быть целым положительным числом в диапазоне от 0 до 255")
#
#
#     def get_sides(self):  # геттер cписка сторон (возвращаем)
#         return self.__sides
#
#     def __is_valid_sides(self, *__sides: int):
#         return all(isinstance(side, int) and side > 0 for side in __sides)
#
#     def set_sides(self, *new_sides):  # сеттер списка сторон (изменяем)
#         if self.__is_valid_sides(*new_sides):
#             self.__sides = list(new_sides)
#         else:
#             raise ValueError("Все стороны должны быть положительными целыми числами")
#
#
#     def __str__(self):
#         return f"Геометрическая фигура с {self.sides_count} сторонами"
#
#     def __len__(self):  # периметр фигуры
#         return sum(self.__sides)
#
#
#
# class Circle(Figure):
#     sides_count = 1
#
#     def __init__(self, color=(200, 200, 100), radius=None, filled: bool = False):
#         super().__init__(self.sides_count, color, filled)
#         self.radius = radius
#         self.set_sides(int(2 * pi * radius))  # длина круга
#
#
#     def get_square(self):
#         return [pi * self.radius ** 2]
#
#
# class Cube(Figure):
#     sides_count = 12
#
#
#     def __init__(self, color=(222, 70, 130), sides=None, filled: bool = False):
#         super().__init__(self.sides_count, color, filled)
#         self.sides = sides
#         s = (sides + sides + sides) / 2
#         self.set_sides(int(self.sides**(self.sides_count/(self.sides_count/2)/2+1)))  # объем куба
#
#     def get_volume(self):
#         return [int(self.sides**(self.sides_count/4))]
#
#
# circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
#
# cube1 = Cube((222, 35, 130), 6)
# #
# # Проверка на изменение цветов:
# circle1.set_color(55, 66, 77) # Изменится
# print(1, circle1.get_color())
# cube1.set_color(300, 70, 15)  # Не изменится
# print(2, cube1.get_color())
# #
# # # Проверка на изменение сторон:
# cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
# print(3, cube1.get_sides())
# print(4, cube1.set_sides())
# circle1.set_sides(15) # Изменится
# print(5,circle1.get_sides())
# #
# # Проверка периметра (круга), это и есть длина:
# print(6,len(circle1))
#
# # # Проверка объёма (куба):
# print(7,cube1.get_volume())

""" Готово по уроку , но только для круга и куба"""

# from math import pi
#
# class Figure:
#     sides_count = 0
#
#     def __init__(self, sides: int, color, filled: bool):
#         self.__sides = []
#         self.__color = (0, 0, 0)
#         self.filled = filled
#         self.new_sides = None
#     def get_color(self):
#         return self.__color
#
#     def __is_valid_color(self, r, g, b):
#         return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))
#
#     def set_color(self, r, g, b):
#         if self.__is_valid_color(r, g, b):
#             self.__color = (r, g, b)
#
#     def get_sides(self):
#         return self.__sides
#
#     def __is_valid_sides(self, *__sides: int):
#         return all(isinstance(side, int) and side > 0 for side in __sides)
#
#     # def valid_count_sides(self, *_sides):
#     #     return self.sides_count != self.
#
#     # def set_sides(self, *new_sides):
#     #     if self.__is_valid_sides(*new_sides):
#     #         self.__sides = list(new_sides)
#     #         if self.__sides != self.sides_count:
#     #             return [self.sides_count]
#     #     # else:
#     #     #     raise ValueError("Все стороны должны быть положительными целыми числами")
#
#     # def set_sides(self, *new_sides):
#     #     self.new_sides = new_sides
#     #     if self.__is_valid_sides(*new_sides) and len(self.new_sides) != self.sides_count:
#     #         self.__sides = list([1] * self.sides_count)
#     #     self.__sides = list(new_sides)
#     #     # else:
#     #     #     raise ValueError("Все стороны должны быть положительными целыми числами")
#
#     def set_sides(self, *new_sides):
#         if self.__is_valid_sides(*new_sides):
#             # Проверка на количество сторон
#             if len(new_sides) != self.sides_count:
#                 self.__sides = [self.sides] * self.sides_count
#             else:
#                 self.__sides = list(new_sides)
#         else:
#             raise ValueError("Все стороны должны быть положительными целыми числами")
#
#     def __str__(self):
#         return f"Геометрическая фигура с {self.sides_count} сторонами"
#
#     def __len__(self):
#         return sum(self.__sides)
#
#
# class Circle(Figure):
#     sides_count = 1
#
#     def __init__(self, color=(200, 200, 100), radius=None, filled: bool = False):
#         super().__init__(self.sides_count, color, filled)
#         self.set_color(*color)
#         self.radius = radius
#         self.set_sides(int(2 * pi * radius))
#
#     def get_square(self):
#         return pi * self.radius ** 2
#
#
# class Cube(Figure):
#     sides_count = 12
#
#     def __init__(self, color=(222, 70, 130), sides=None, filled: bool = False):
#         super().__init__(self.sides_count, color, filled)
#         self.set_color(*color)
#         self.sides = sides
#         self.set_sides(sides, sides, sides, sides, sides, sides, sides, sides, sides, sides, sides, sides)
#
#     def get_volume(self):
#         return self.sides ** 3
#
#
# circle1 = Circle((200, 200, 100), 10)
#
# cube1 = Cube((222, 35, 130), 6)
#
# circle1.set_color(55, 66, 77)
# print(1, circle1.get_color())
#
# cube1.set_color(300, 70, 15)
# print(2, cube1.get_color())
#
# cube1.set_sides(5, 3, 12, 4, 5)
# print(3, cube1.get_sides())
#
# circle1.set_sides(15)
# print(5, circle1.get_sides())
#
# print(6, len(circle1))
#
# print(7, cube1.get_volume())


""" Классы фигуры, круг, куб и треугольник"""
from math import pi, sqrt


class Figure:
    sides_count = 0

    def __init__(self, sides: int, color, filled: bool):
        self.__sides = [0] * sides
        self.__color = [0, 0, 0]
        self.filled = filled
        self.new_sides = None

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, *__sides: int):
        return all(isinstance(side, int) and side > 0 for side in __sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            # Проверка на количество сторон
            if len(new_sides) != self.sides_count:
                self.__sides = [self.sides] * self.sides_count
            else:
                self.__sides = list(new_sides)
        else:
            raise ValueError("Все стороны должны быть положительными целыми числами")

    def __str__(self):
        return f"Геометрическая фигура с {self.sides_count} сторонами"

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color=(200, 200, 100), radius=None, filled: bool = False):
        super().__init__(self.sides_count, color, filled)
        self.set_color(*color)
        self.radius = radius
        self.set_sides(int(2 * pi * radius))

    def get_square(self):
        return pi * self.radius ** 2


class Cube(Figure):
    sides_count = 12

    def __init__(self, color=(222, 70, 130), sides=None, filled: bool = False):
        super().__init__(self.sides_count, color, filled)
        self.set_color(*color)
        self.sides = sides
        self.set_sides(sides, sides, sides, sides, sides, sides, sides, sides, sides, sides, sides, sides)

    def get_volume(self):
        return self.sides ** 3


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color=(250, 170, 2), sides=(1, 1, 1), filled: bool = False):
        super().__init__(self.sides_count, color, filled)
        self.set_color(*color)
        self.sides = sides
        self.set_sides(*sides)

    # def get_square(self, a, b, c):
    #
    #     self.a = a
    #     self.b = b
    #     self.c = c
    #     # Полупериметр
    #     self.p = (self.a + self.b + self.c) / 2
    #     # Площадь по формуле Герона
    #     s = sqrt(self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c))
    #     return s

    def get_square(self):
        a, b, c = self.get_sides()
        p = (a + b + c) / 2
        if a + b > c and a + c > b and b + c > a:
            return round((sqrt(p * (p - a) * (p - b) * (p - c))), 2)
        else:
            print("У треугольника одна из сторон должна быть > суммы двух других, либо все стороны равны")


print('Круг и куб')
circle1 = Circle([200, 200, 100], 10)  # цвет пыльно-желтый
cube1 = Cube([222, 35, 130], 6)  # цвет фуксия

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

print("Треугольник")
triangle1 = Triangle([250, 170, 2], [6, 6, 14], True)  # цвет яичного желтка

# Проверка на изменение цветов:
triangle1.set_color(300, 70, 15)  # Не изменится
print(triangle1.get_color())

# Проверка на изменение сторон:
triangle1.set_sides(7, 7, 7)  # стороны равны
print(triangle1.get_sides())
# triangle1.set_sides(15, 4, 7)   # одна сторона > суммы двух других сторон
# print(triangle1.get_sides())
# triangle1.set_sides(2, 2, 5)   # треугольник невозможен
# print(triangle1.get_sides())

# Проверка объёма (треугольника):
print(triangle1.get_square())  # Площадь треугольника
