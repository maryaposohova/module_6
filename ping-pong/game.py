import arcade

# имитация констант, эти данные меняться не будут
SCREEN_WIGTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Pong game'

# добавляем мячик
class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__('мячик.png', 0.1)
        self.change_x = 0.5 # скорость перемещения
    def update(self): # делаем мяч подвижным. метод отвечает за обновление текущего положения х и у
        self.center_x += self.change_x  # изменение значения мячика
        self.center_y += self.change_y


# добавляем ракетку
class Bar(arcade.Sprite):  # класс ракетки наследуется от arcade.sprite
    def __init__(self):
        super().__init__('ракетка.png', 0.2)
        # если мы хотим, чтобы ракетка появилась в игре, то ее надо создать внутри класса Game,
        # а характеристики мы создаем в ините. В классе гейм нам тоженужно преопределить инит. Но передаем туда
        # ширину, высоту и заголовок, 15 и 16 строки



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
        self.ball.update()

if __name__ == "__main__":
    window = Game(SCREEN_WIGTH, SCREEN_HEIGHT, SCREEN_TITLE)  # создание экземпляра класса гейм, передаем парамерты констант
    arcade.run()  # запуск цикла обновлений
# после вызова метода ран мы можем видет окошко и именно сэтим окном мы будем работать
