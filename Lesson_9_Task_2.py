class Road:

    def __init__(self, length, whidth):
        self._length = length
        self._width = whidth
        self.weight = 25
        self.thickness = 4

    def calculate_mass(self):
        result = self._length * self._width * self.weight * self.thickness / 1000
        print(f'Масса асфальта, необходимого для покрытия дороги, длиной {self._length}м и шириной {self._width}м, равна {result}т')

m = Road(6832, 4)
m.calculate_mass()
