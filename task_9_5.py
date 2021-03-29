class Stationery:

    def __init__(self, title):
        self._title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Start writing by {self._title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Start drawing by {self._title}')


class Handle(Stationery):
    def draw(self):
        print(f'Start selecting by {self._title}')


s1 = Pen('pen')
s1.draw()

s2 = Pencil('pencil')
s2.draw()

s3 = Handle('handle')
s3.draw()

s4 = Stationery('ink')
s4.draw()
