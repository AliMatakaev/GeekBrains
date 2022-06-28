class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки.'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Отрисовка {self.title}'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Отрисовка {self.title}'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Отрисовка {self.title}'


pen = Pen('шариковой ручкой')
print(pen.draw())

pencil = Pencil('карандашом')
print(pencil.draw())

handle = Handle('маркером')
print(handle.draw())


