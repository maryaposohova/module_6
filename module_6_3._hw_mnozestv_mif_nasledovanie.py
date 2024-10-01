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



class Horse:
    x_distance = 0
    sound = 'Frrr'

    def run(self, dx):
        return self.x_distance + dx

class Eagle:
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def run(self, dy):
        return self.y_distance + dy



class Pegasus:
    pass

# p1 = Pegasus()
# print(p1.get_pos())
# p1.move(10, 15)
# print(p1.get_pos())
# p1.move(-5, 20)
# print(p1.get_pos())
#
# # p1.voice()
print(Pegasus.mro())

h = Horse()
print("Проверка. Лошадь", h.x_distance, h.sound, h.run(50))
e = Eagle()
print("Проверка. Птичка", e.y_distance, e.sound, e.run(10))