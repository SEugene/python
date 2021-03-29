import time
from colorama import Fore


class TrafficLight:

    def __init__(self, colour):
        self.__colour = int(colour)
        if int(colour) > 2:
            raise ValueError(f'Colour state {int(colour)} is not in range 0..2')
        if int(colour) != 0:
            raise ValueError(f'Wrong colour order. The first colour should be "0", not "{int(colour)}"')

    def running(self):
        run = [('red', 7, Fore.RED), ('yellow', 2, Fore.YELLOW), ('green', 5, Fore.GREEN)]
        clrs = [Fore.RED, Fore.YELLOW, Fore.GREEN]
        while self.__colour < 12:
            idx = self.__colour - self.__colour // 3 * 3
            print(f'{run[idx][2]}' + f'{run[idx][0].upper()}')
            time.sleep(run[idx][1])
            self.__colour += 1


state1 = TrafficLight(0)
state1.running()

# state2 = TrafficLight(2)
# state2.running()

state3 = TrafficLight(7)
state3.running()

