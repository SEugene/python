class Road:

    def __init__(self, length, width):
        self._length = float(length)
        self._width = float(width)

    def asphalt_weight(self):
        return self._length * self._width * 25 * 5


weight = Road(20, '75000')
print(f'{weight.asphalt_weight()/1000} т')
