class Figure:
    sides_count = 0  # счет сторон

    def __init__(self, __sides: int, __color, filled: bool):
        self.__sides = []  # (список сторон(целые числа))
        self.__color = []
        self.filled = filled  # (закрашенный, bool)

    def get_color(self, r, g, b):  # должен возвращать список RGB цветов
        return self.__color.append()

    def __is_valid_color(self, r, g, b):
        if (not isinstance(r, int) or r < 0 or r > 255 and not isinstance(g, int) or g < 0 or g > 255
                and not isinstance(b, int) or b < 0 or b > 255):
            raise ValueError("Значение должно быть целым положительным числом в диапазоне от 0 до 255")
        self.values = r
        self.values = g
        self.values = b


d = Figure(3, 4,True)
print(d.get_color(-5, 7,8))
#
# circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
# cube1 = Cube((222, 35, 130), 6)
#
# # Проверка на изменение цветов:
# circle1.set_color(55, 66, 77) # Изменится
# print(circle1.get_color())
# cube1.set_color(300, 70, 15) # Не изменится
# print(cube1.get_color())
#
# # Проверка на изменение сторон:
# cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
# print(cube1.get_sides())
# circle1.set_sides(15) # Изменится
# print(circle1.get_sides())
#
# # Проверка периметра (круга), это и есть длина:
# print(len(circle1))
#
# # Проверка объёма (куба):
# print(cube1.get_volume())