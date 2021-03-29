class Car:

    def __init__(self, speed, color, name, is_police, direction='straight'):
        self._speed = int(speed)
        self._color = color
        self._name = name
        self._is_police = is_police
        self._direction = direction

    def go(self):
        if self._speed > 0:
            return f'{self._color} {self._name} is moving'

    def stop(self):
        if self._speed == 0:
            return f'{self._color} {self._name} has stopped'

    def turn(self, direction):
        self._direction = direction
        if self._speed == 0:
            return f'{self._color} {self._name} has stopped'
        return f'{self._color} {self._name} turns to the {self._direction}'

    def show_speed(self):
        return f'the current speed is: {self._speed} km/h'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police, direction='straight'):
        super().__init__(speed, color, name, is_police, direction)
        if self._is_police:
            raise Warning("Town Car can't be a Police Car!")

    def show_speed(self):
        if self._speed > 60:
            violation = ' - OVERSPEED!'
        else:
            violation = ''
        return f'{self._color} {self._name} is a Town Car; the current speed is: {self._speed} km/h {violation}'


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police, direction='straight'):
        super().__init__(speed, color, name, is_police, direction)
        if self._is_police:
            raise Warning("Work Car can't be a Police Car!")

    def show_speed(self):
        if self._speed > 40:
            violation = ' - OVERSPEED!'
        else:
            violation = ''
        return f'{self._color} {self._name} is a Work Car; the current speed is: {self._speed} km/h {violation}'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police, direction='straight'):
        super().__init__(speed, color, name, is_police, direction)
        if self._is_police:
            self._status = 'Police Car'
        else:
            raise Warning("Wrong flag 'is_police' - must be True!")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police, direction='straight'):
        super().__init__(speed, color, name, is_police, direction)
        if self._is_police:
            raise Warning("Sports Car can't be a Police Car!")


car1 = WorkCar(55, 'red', 'Renault', False)
print(f"{car1.turn('right')}; {car1.go()}")
print(car1.show_speed(), '\n')

car2 = TownCar(80, 'grey', 'Toyota', False)
print(f"{car2.turn('left')}; {car2.go()}")
print(car2.show_speed(), '\n')

car3 = SportCar(120, 'yellow', 'Ferrari', False)
print(car3.go())
print(car3.show_speed(), '\n')

car4 = PoliceCar(0, 'blue', 'Ford', True)
print(car4.stop())
print(car4.show_speed(), '\n')

car5 = PoliceCar(50, 'blue', 'Ford', False)
