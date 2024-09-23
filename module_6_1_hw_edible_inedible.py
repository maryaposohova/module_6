# Задача "Съедобное, несъедобное"

# 1 variable

# class Animal:  # родител
#     alive = True  # живой
#     fed = False  # накормленный
#
#     def __init__(self, name):
#         self.name = name
#
#
# class Plant:  # родител
#     edible = False  # съедобность
#
#     def __init__(self, name):
#         self.name = name
#
#
# class Fruit(Plant):
#     edible = True
#
#
# class Flower(Plant):  # edible = False насдледует от класса плант
#     pass
#
#
# class Mammal(Animal, Plant):  # Млекопитающее
#     def eat(self, food):
#         if food.edible == True:
#             print(f'{self.name} съел {food.name}')
#             self.fed = True
#         elif food.edible == False:
#             print(f'{self.name} не стал есть {food.name}')
#             self.alive = False
#
#
# class Predator(Animal, Plant):  # Хищник
#
#     def eat(self, food):
#         if food.edible == True:
#             print(f'{self.name} съел {food.name}')
#             self.fed = True
#         elif food.edible == False:
#             print(f'{self.name} не стал есть {food.name}')
#             self.alive = False
#
#
# a1 = Predator('Волк с Уолл-Стрит')
# a2 = Mammal('Хатико')
# p1 = Flower('Цветик семицветик')
# p2 = Fruit('Заводной апельсин')
#
# print(a1.name)  # Волк с Уолл-Стрит
# print(p1.name)  # Хатико
#
# print(a1.alive)  # волк живой
# print(a2.fed)  # хатико погиб
# a1.eat(p1)
# a2.eat(p2)
# print(a1.alive)
# print(a2.fed)

#
#
#

# 2 variable

# class Animal:  # родител
#     alive = True  # живой
#     fed = False  # накормленный
#
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self, food):
#         if food.edible == True:
#             print(f'{self.name} съел {food.name}')
#             self.fed = True
#         elif food.edible == False:
#             print(f'{self.name} не стал есть {food.name}')
#             self.alive = False
#
# class Plant:  # родител
#     edible = False  # съедобность
#
#     def __init__(self, name):
#         self.name = name
#
#
# class Fruit(Plant):
#     edible = True
#
#
# class Flower(Plant):  # edible = False насдледует от класса плант
#     pass
#
#
# class Mammal(Animal, Plant):  # Млекопитающее
#     '''
#     Наследует def eat(self, food):   из класса Animal
#     '''
#     pass
#
#
# class Predator(Animal, Plant):  # Хищник
#     '''
#     Наследует def eat(self, food):   из класса Animal
#     '''
#     pass
#
#
# a1 = Predator('Волк с Уолл-Стрит')
# a2 = Mammal('Хатико')
# p1 = Flower('Цветик семицветик')
# p2 = Fruit('Заводной апельсин')
#
# print(a1.name)  # Волк с Уолл-Стрит
# print(p1.name)  # Хатико
#
# print(a1.alive)  # волк живой
# print(a2.fed)  # хатико погиб
# a1.eat(p1)
# a2.eat(p2)
# print(a1.alive)
# print(a2.fed)


# 3 variable
class Animal:  # родител
    alive = True  # живой
    fed = False  # накормленный

    def __init__(self, name):
        self.name = name


class Plant:  # родител
    edible = False  # съедобность

    def __init__(self, name):
        self.name = name

class Eat:
    def eat(self, food):
        if food.edible == True:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        elif food.edible == False:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Fruit(Plant):
    edible = True


class Flower(Plant):  # edible = False насдледует от класса плант
    pass


class Mammal(Animal, Plant, Eat):  # Млекопитающее
    '''
    Наследует def eat(self, food):   из класса Eat
    '''
    pass


class Predator(Animal, Plant, Eat):  # Хищник
    '''
    Наследует def eat(self, food):   из класса Eat
    '''
    pass


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)  # Волк с Уолл-Стрит
print(p1.name)  # Хатико

print(a1.alive)  # волк живой
print(a2.fed)  # хатико погиб
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)




'''
2023/11/07 00:00|Домашнее задание по теме "Зачем нужно наследование"
Если вы решали старую версию задачи, проверка будет производиться по ней.
Ссылка на старую версию тут.

Цель: применить базовые знания о наследовании классов для решения задачи

Задача "Съедобное, несъедобное":
Разнообразие животного мира давно будоражит умы человечества. Царства, классы, виды... Почему бы и нам не попробовать выстроить что-то подобное используя наследования классов?

Необходимо описать пример иерархии животного мира, используя классы и принцип наследования.

Создайте:
2 класса родителя: Animal, Plant
Для класса Animal атрибуты alive = True(живой) и fed = False(накормленный), name - индивидуальное название каждого животного.
Для класса Plant атрибут edible = False(съедобность), name - индивидуальное название каждого растения

4 класса наследника:
Mammal, Predator для Animal.
Flower, Fruit для Plant.

У каждого из объектов класса Mammal и Predator должны быть атрибуты и методы:
eat(self, food) - метод, где food - это параметр, принимающий объекты классов растений.

Метод eat должен работать следующим образом:
Если переданное растение (food) съедобное - выводит на экран "<self.name> съел <food.name>", меняется атрибут fed на True.
Если переданное растение (food) не съедобное - выводит на экран "<self.name> не стал есть <food.name>", меняется атрибут alive на False.
Т.е если животному дать съедобное растение, то животное насытится, если не съедобное - погибнет.

У каждого объекта Fruit должен быть атрибут edible = True (переопределить при наследовании)

Создайте объекты классов и проделайте действия затронутые в примере результата работы программы.

Пункты задачи:
Создайте классы Animal и Plant с соответствующими атрибутами и методами
Создайте(+унаследуйте) классы Mammal, Predator, Flower, Fruit с соответствующими атрибутами и методами. При необходимости переопределите значения атрибутов.
Создайте объекты этих классов.

Пример результата выполнения программы:
Выполняемый код(для проверки):
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.

Вывод на консоль:
Волк с Уолл-Стрит
Цветик семицветик
True
False
Волк с Уолл-Стрит не стал есть Цветик семицветик
Хатико съел Заводной апельсин
False
True

Примечания:
Помните, обращаясь к атрибутам объекта текущего класса используйте параметр self.
Передавая объекты классов Fruit и Flower в метод eat, так же можно обращаться к их атрибутам внутри.
Обращайте внимание на то, где атрибут класса, а где атрибут объекта.
Файл module_6_1.py и загрузите его на ваш GitHub репозиторий и пришлите ссылку на него.

Успехов!

https://urban-university.ru/members/courses/course999421818026/20231107-0000domasnee-zadanie-po-teme-zacem-nuzno-nasledovanie-440919122156
'''

