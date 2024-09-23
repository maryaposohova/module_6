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

