class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} is moving.'

    def stop(self):
        return f'{self.name} stopped.'

    def turn(self, direction):
        return f'{self.name} turned {direction}.'

    def show_speed(self):
        return f'Driving speed {self.speed} km/h.'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'Speed limit exceeded on {self.speed - 60} km/h! Your speed is {self.speed} km/h.'
        else:
            return f'Driving speed is {self.speed} km/h.'


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'Speed limit exceeded on {self.speed - 40} km/h! Your speed is {self.speed} km/h.'
        else:
            return f'Driving speed is {self.speed} km/h.'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        return f'Driving speed is {self.speed} km/h.'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'Driving speed is {self.speed} km/h.'


hyundai = TownCar(60, 'grey', 'Hyundai Solaris', False)
print(hyundai.go(), hyundai.show_speed())

gazelle = WorkCar(47, 'white', 'Gazelle', False)
print(gazelle.go(), gazelle.show_speed())

ferrari = SportCar(90, 'red', 'Ferrari', False)
print(ferrari.go(), ferrari.show_speed())

police = PoliceCar(80, 'blue', 'Patrol car', True)
print(police.go(), police.turn('left'), police.turn('right'), police.stop())