from time import sleep

class TrafficLight:
    __color = ["red", "yellow", "green"]

    def running(self):
        i = 0
        while i != 3:
            print(TrafficLight.__color[i])
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(3)
            elif i == 2:
                sleep(10)
            i += 1

light = TrafficLight()
light.running()