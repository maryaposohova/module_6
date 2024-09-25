# Задача "Изменять нельзя получать"

# class Vehicle: # транспорт
#     _COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
#     def __init__(self, owner, __model, __engine_power, __color):
#         self.owner = owner    # владелец транспорта может меняться
#         self.__model = __model  # модель (марка) транспорта. (мы не можем менять название модели)
#         self.__engine_power = __engine_power #  мощность двигателя. (не можем менять)
#         self.__color = __color  #  название цвета. (мы не можем менять цвет автомобиля своими руками)
#
#     def get_model(self):
#         return f'Модель: {self.__model}'
#
#     def get_horsepower(self):
#         return f"Мощность двигателя: {self.__engine_power}"
#
#     def get_color(self):
#          return f"Цвет: {self.__color}"
#
#     def print_info(self):
#         print(f'{self.__model} \n{self.__engine_power} \n{self._Vehicle__color} \nВладелец: {self.owner}')
#
#     def set_color(self, new_color):
#         if new_color.lower() in (color.lower() for color in Vehicle._COLOR_VARIANTS):
#             color = new_color
#         else:
#             print(f'Нельзя сменить цвет на {new_color}')
#
# class Sedan(Vehicle): # седан
#     __PASSENGERS_LIMIT = 5
#


class Vehicle:  # транспорт
    _COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white', 'cherry red']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner    # владелец транспорта может меняться
        self.__model = __model    # модель (марка) транспорта. (мы не можем менять название модели)
        self.__engine_power = __engine_power   # мощность двигателя. (не можем менять)
        self.__color = __color     # название цвета. (мы не можем менять цвет автомобиля своими руками)

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(
            f'{Vehicle.get_model(self)} \n{Vehicle.get_horsepower(self)} \n{Vehicle.get_color(self)} '
            f'\nВладелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in (color.lower() for color in Vehicle._COLOR_VARIANTS):
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):  # седан
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
# Изначальные свойства
vehicle1.print_info()
# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
# Проверяем что поменялось
vehicle1.print_info()

print()

vehicle2 = Sedan('Елена', 'Фольксваген Джетта 5', 'red', 102)
# Изначальные свойства
vehicle2.print_info()
# Меняем свойства (в т.ч. вызывая методы)
vehicle2.set_color('Pink')
vehicle2.set_color('CHERRY RED')
vehicle2.owner = 'Мария'
# Проверяем что поменялось
vehicle2.print_info()

"""
Практическое задание
2023/11/08 00:00|Домашнее задание по теме "Доступ к свойствам родителя. Переопределение свойств."
Цели: Применить сокрытие атрибутов и повторить наследование. Рассмотреть на примере объекта из реального мира.

Задача "Изменять нельзя получать":
В этой задаче мы реализуем классы транспорта, в которых нельзя будет просто так поменять цвет, мощность двигателя и 
прочие свойства, т.к. в реальной жизни это чаще всего делается не владельцем, а в специальных сервисах. Да, узнать 
значения этих свойств мы сможем, но вот изменить - нет.

Вам необходимо создать 2 класса: Vehicle и Sedan, где Vehicle - это любой транспорт, а Sedan(седан) - наследник класса 
Vehicle.

I. Каждый объект Vehicle должен содержать следующие атрибуты объекта:
Атрибут owner(str) - владелец транспорта. (владелец может меняться)
Атрибут __model(str) - модель (марка) транспорта. (мы не можем менять название модели)
Атрибут __engine_power(int) - мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
Атрибут __color(str) - название цвета. (мы не можем менять цвет автомобиля своими руками)
А так же атрибут класса:
Атрибут класса __COLOR_VARIANTS, в который записан список допустимых цветов для окрашивания. (Цвета написать свои)
Каждый объект Vehicle должен содержать следующий методы:
Метод get_model - возвращает строку: "Модель: <название модели транспорта>"
Метод get_horsepower - возвращает строку: "Мощность двигателя: <мощность>"
Метод get_color - возвращает строку: "Цвет: <цвет транспорта>"
Метод print_info - распечатывает результаты методов (в том же порядке): get_model, get_horsepower, get_color; а так же 
владельца в конце в формате "Владелец: <имя>"
Метод set_color - принимает аргумент new_color(str), меняет цвет __color на new_color, если он есть 
в списке __COLOR_VARIANTS, в противном случае выводит на экран надпись: "Нельзя сменить цвет на <новый цвет>".
Взаимосвязь методов и скрытых атрибутов:
Методы get_model, get_horsepower, get_color находятся в одном классе с соответствующими им атрибутами: 
__model, __engine_power, __color. Поэтому атрибуты будут доступны для методов.
Атрибут класса __COLOR_VARIANTS можно получить обращаясь к нему через объект(self).
Проверка в __COLOR_VARIANTS происходит не учитывая регистр ('BLACK' ~ 'black').
II. Класс Sedan наследуется от класса Vehicle, а так же содержит следующие атрибуты:
Атрибут __PASSENGERS_LIMIT = 5 (в седан может поместиться только 5 пассажиров)

Пункты задачи:
Создайте классы Vehicle и Sedan.
Напишите соответствующие свойства в обоих классах.
Не забудьте сделать Sedan наследником класса Vehicle.
Создайте объект класса Sedan и проверьте, как работают все его методы, взяты из класса Vehicle.

Пример результата выполнения программы:
Исходный код:
# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()

Вывод на консоль:
Модель: Toyota Mark II
Мощность двигателя: 500
Цвет: blue
Владелец: Fedos
Нельзя сменить цвет на Pink
Модель: Toyota Mark II
Мощность двигателя: 500
Цвет: BLACK
Владелец: Vasyok

Примечания:
Обращайте особое внимание на условия задачи: что является атрибутом класса, а что атрибутом объекта.
Методы, где описано получение/перезапись каких-либо атрибутов рекомендуется начинать со слов get и set соответственно. 
Такие методы часто используются для доступа к скрытым атрибутам и позволяют написать дополнительную логику(код) при их 
получении/изменении.
Не забывайте использовать self при обращении к атрибутам объекта.
Константные(постоянные) значения в Python принято писать полностью в верхнем регистре (капсом), как в случае списка 
цветов или количеством пассажиров.

Файл с кодом (module_6_2.py) загрузите в репозиторий GitHub и пришлите ссылку на него.

Успехов!

https://urban-university.ru/members/courses/course999421818026/20231108-0000domasnee-zadanie-po-teme-dostup-k-svojstvam-roditela-pereopredelenie-svojstv-555325942294
"""
