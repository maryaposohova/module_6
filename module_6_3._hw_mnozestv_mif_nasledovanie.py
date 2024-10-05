# class Human:
#     def __init__(self, name, groop):
#         self.name = name
#         super().__init__(groop)
#         super().about()
#
#     def info(self):
#         print(f"Привет, меня зовут {self.name}")
#
# class Student_groop:
#     def __init__(self, groop):
#         self.groop = groop
#
#     def about(self):
#         print(f'{self.name} учится в группе {self.groop}')
# class Student(Human, Student_groop):
#     def __init__(self, name, place, groop):
#         super().__init__(name, groop)
#         self.place = place
#         super().info()
#
#
#
# # human = Human('Денис')
# # print(human.name)
# student = Student('Денис', 'Урбан', 'Питон 1')
#
# print(Student.mro())

# class Horse:
#     x_distance = 0
#     sound = 'Frrr'
#
#     def run(self, dx):   # дистанция бега
#         self.dx = dx
#         return self.x_distance + dx
#
# class Eagle:
#     y_distance = 0
#     sound = 'I train, eat, sleep, and repeat'
#
#     def fly(self, dy):
#         self.dy = dy
#         return self.y_distance + dy
#
#
# class Pegasus(Horse, Eagle):
#     def move(self, dx, dy):
#         pass
#
#     def get_pos(self):
#         return  x_distance, y_distance

# class Horse:
#     def __init__(self, x_distance = 0, sound = 'Frrr'):
#         self.x_distance = x_distance
#         self.sound = sound
#         print(x_distance)
#
#     def run(self, dx):
#         return self.x_distance + dx
#
# class Eagle:
#     def __init__(self, y_distance = 0, sound = 'I train, eat, sleep, and repeat'):
#         self.y_distance = y_distance
#         self.sound = sound
#         print(y_distance)
#
#     def fly(self, dy):
#         return self.y_distance + dy
#
#
# h = Horse()
# # print(h.x_distance)
# print(h.run(50), h.sound)
#
# e = Eagle()
# # print(e.y_distance)
# print(e.fly(20), e.sound)

# class Horse:
#     def __init__(self, x_distance = 0, sound = 'Frrr'):
#         self.x_distance = x_distance
#         self.sound = sound
#         print(x_distance)
#
#     def run(self, dx):
#         return self.x_distance == self.x_distance + dx
#
# class Eagle:
#     def __init__(self, y_distance = 0, sound = 'I train, eat, sleep, and repeat'):
#         self.y_distance = y_distance
#         self.sound = sound
#         print(y_distance)
#
#     def fly(self, dy):
#         return self.y_distance == self.y_distance + dy
#
#
# class Pegasus(Horse, Eagle):
#     def __init__(self):
#         super().__init__()
#
#     def move(self, dx, dy):
#         Horse().run(dx)
#         Eagle().fly(dy)
#
#     def get_pos(self):
#         return tuple
#

# h = Horse()
# # print(h.x_distance)
# print(h.run(50), h.sound)
#
# e = Eagle()
# # print(e.y_distance)
# print(e.fly(20), e.sound)
# print()
#
#
#
# class Horse:
#     x_distance = 0
#     sound = 'Frrr'
#
#     def run(self, dx):
#         return self.x_distance + dx
#
# class Eagle:
#     y_distance = 0
#     sound = 'I train, eat, sleep, and repeat'
#
#     def run(self, dy):
#         return self.y_distance + dy
#
#
#
# class Pegasus:
#     pass
#
# # p1 = Pegasus()
# # print(p1.get_pos())
# # p1.move(10, 15)
# # print(p1.get_pos())
# # p1.move(-5, 20)
# # print(p1.get_pos())
# #
# # # p1.voice()
# print(Pegasus.mro())
#
# h = Horse()
# print("Проверка. Лошадь", h.x_distance, h.sound, h.run(50))
# e = Eagle()
# print("Проверка. Птичка", e.y_distance, e.sound, e.run(10))

# class  Horse:
#     x_distance = 0
#     sound = 'Frrr'
#
#     def run(self, dx):
#         self.x_distance += abs(dx)
#         return self.x_distance
#
# class Eagle:
#     y_distance = 0
#     sound = 'I train, eat, sleep, and repeat'
#
#     def fly(self, dy):
#         self.y_distance += abs(dy)
#         return self.y_distance
#
# class Pegasus(Horse, Eagle):
#
#     def move(self, dx, dy) :
#        self.run(dx)
#        self.fly(dy)
#
#     def get_pos(self):
#         return (self.x_distance, self.y_distance)
#
#     def voice(self):
#         print(Eagle().sound)
#
# p1 = Pegasus()
#
# print(p1.get_pos())
# p1.move(10, 15)
# print(p1.get_pos())
# p1.move(-5, 20)
# print(p1.get_pos())
#
# p1.voice()


#  Задача "Мифическое наследование"
class Horse:
    def __init__(self, x_distance=0, sound='Frrr'):
        self.x_distance = x_distance
        self.sound = sound

    def run(self, dx):
        self.x_distance += abs(dx)
        return self.x_distance


class Eagle:
    def __init__(self, y_distance=0, sound='I train, eat, sleep, and repeat'):
        self.y_distance = y_distance
        self.sound = sound

    def fly(self, dy):
        self.y_distance += abs(dy)
        return self.y_distance


class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()
        Eagle.__init__(self)

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(Eagle().sound)  # или self.sound дает саунд от класса Eagle, а не от Horse почему-то


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())

p1.move(-5, 20)
print(p1.get_pos())

p1.voice()

# print(Pegasus.mro())
'''
2023/11/09 00:00|Домашнее задание по теме "Множественное наследование"
Если вы решали старую версию задачи, проверка будет производиться по ней.
Ссылка на старую версию тут.

Цель: закрепить знания множественного наследования в Python.

Задача "Мифическое наследование":
Необходимо написать 3 класса:
Horse - класс описывающий лошадь. Объект этого класса обладает следующими атрибутами:
x_distance = 0 - пройденный путь.
sound = 'Frrr' - звук, который издаёт лошадь.
И методами:
run(self, dx), где dx - изменение дистанции, увеличивает x_distance на dx.

Eagle - класс описывающий орла. Объект этого класса обладает следующими атрибутами:
y_distance = 0 - высота полёта
sound = 'I train, eat, sleep, and repeat' - звук, который издаёт орёл (отсылка)
И методами:
fly(self, dy) где dy - изменение дистанции, увеличивает y_distance на dy.

Pegasus - класс описывающий пегаса. Наследуется от Horse и Eagle в том же порядке.
Объект такого класса должен обладать атрибутами классов родителей в порядке наследования.
Также обладает методами:
move(self, dx, dy) - где dx и dy изменения дистанции. В этом методе должны запускаться наследованные 
методы run и fly 
соответственно.
get_pos(self) возвращает текущее положение пегаса в виде кортежа - (x_distance, y_distance) в том же 
порядке.
voice - который печатает значение унаследованного атрибута sound.
Пункты задачи:
Создайте классы родители: Horse и Eagle с методами из описания.
Создайте класс наследник Pegasus с методами из описания.
Создайте объект класса Pegasus и вызовите каждый из ранее перечисленных методов, проверив их работу.

Пример результата выполнения программы:
Пример работы программы:
p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()

Вывод на консоль:
(0, 0)
(10, 15)
(5, 35)
I train, eat, sleep, and repeat

Примечания:
Будьте внимательней, когда вызываете методы классов родителей в классе наследнике при множественном 
наследовании: при обращении через super() методы будут искаться сначала в первом, потом во втором и т.д. 
классах по mro().
Заметьте, что Pegasus издаёт звук "I train, eat, sleep, and repeat", т.к. по порядку сначала идёт наследование 
от Horse, а после от Eagle.

Файл module_6_3.py и загрузите его на ваш GitHub репозиторий. В решении пришлите ссылку на него.
Успехов!

https://urban-university.ru/members/courses/course999421818026/20231109-0000domasnee-zadanie-po-teme-mnozestvennoe-nasledovanie-290139472637
'''
