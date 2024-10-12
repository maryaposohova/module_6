import arcade

# имитация констант, эти данные меняться не будут
SCREEN_WIGTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Pong game'

# добавляем мячик
class Ball(arcade.Sprite): # класс мячика
    def __init__(self):
        super().__init__('мячик.png', 0.1)
        self.change_x = 3 # горизонтальная скорость перемещения
        self.change_y = 2  # вертикальная скорость перемещения
    def update(self): # делаем мяч подвижным. метод отвечает за обновление текущего положения х и у
        self.center_x += self.change_x  # изменение значения мячика по горизонтали
        self.center_y += self.change_y  # изменение значения мячика по вертикали
        if self.right > SCREEN_WIGTH:  # если мяч переезжает правую, если больше ширины окна
            self.change_x = -self.change_x  # то мы меняем положение на противоположное
        if self.left <= 0:  # если мяч переезжает правую, если больше ширины окна
            self.change_x = -self.change_x  # то мы меняем положение на противоположное
        if self.top > SCREEN_HEIGHT:  # если мяч улетает вверх га границу (больше чем высота окна))
            self.change_y = -self.change_y  # то мы меняем положение на противоположное
        if self.bottom <= 0:  #  если вниз за границу улетает, меньше или равно 0
            self.change_y = -self.change_y  # то мы меняем положение на противоположное

# добавляем ракетку
class Bar(arcade.Sprite):  # класс ракетки наследуется от arcade.sprite
    def __init__(self):
        super().__init__('ракетка.png', 0.5)
        # если мы хотим, чтобы ракетка появилась в игре, то ее надо создать внутри класса Game,
        # а характеристики мы создаем в ините. В классе гейм нам тоженужно преопределить инит. Но передаем туда
        # ширину, высоту и заголовок, 15 и 16 строки

    def update(self):
        self.center_x += self.change_x
        if self.right > SCREEN_WIGTH:  # если ракетка убегает вправо
            self.right = SCREEN_WIGTH  # то приравниваем правую часть ракетки к ширине экрана
            # то же самое делает с левой частью, приравниваем ее к экрану
        if self.left <= 0:
            self.left = 0
class Game(arcade.Window):
    def __init__(self, wigth, height, title):
        super().__init__(wigth, height, title)  # и эти параметры мы передаем классу родителю
        self.bar = Bar()  # сщздаем ракетку
        self.ball = Ball()
        self.setup()

    def setup(self): # ракетка сейчас в левом ни жнем углу, поэтому создаем медот, отвечающий за полодение элементов в игре.
        self.bar.center_x = SCREEN_WIGTH / 2
        self.bar.center_y = SCREEN_HEIGHT / 5
        self.ball.center_x = SCREEN_WIGTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 2
    def on_draw(self):
        self.clear((255, 255, 255))  # этот кортеж из 3 х параметров rgb даст нам белый задний фон
        self.bar.draw()
        self.ball.draw()

    def update(self, delta): # переопределяем метод апдейт, дельту не трогаем, это частота обновления
        if arcade.check_for_collision(self.bar, self.ball):
            self.ball.change_y = -self.ball.change_y
        self.ball.update()
        self.bar.update()

    def on_key_press(self, key, modifiers): # переопределяем метод, чтобы добавлять функционал, который будет реализовываться при нажатии и отпускании кнопки
        if key == arcade.key.RIGHT: # достаем из библиотеки модуль кей.RIGHT - константа в модуле кей, соответствует кнопке на клавиатуре(стрелка )
            self.bar.change_x = 20 # если положительное значение, то движется вправо
        if key == arcade.key.LEFT:
            self.bar.change_x = -20  # если отерицательное значение, то движется влево

    def on_key_release(self, key, modifiers): # останавливаем ракетку при отпускании мышки
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.bar.change_x = 0


if __name__ == "__main__":
    window = Game(SCREEN_WIGTH, SCREEN_HEIGHT, SCREEN_TITLE)  # создание экземпляра класса гейм, передаем парамерты констант
    arcade.run()  # запуск цикла обновлений
# после вызова метода ран мы можем видет окошко и именно сэтим окном мы будем работать
