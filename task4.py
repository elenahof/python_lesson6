class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"The {self.color} car {self.name} is driving")

    def stop(self):
        print(f"The car {self.name} has stopped")

    def turn(self, direction):
        print(f"The car {self.name} turned {direction}")

    def shown_speed(self):
        print(f"The current speed of {self.name} is {self.speed}")

class TownCar(Car):
    def shown_speed(self):
        if self.speed > 60:
            print("You drive too fast! Slow down!")
        else:
            print("Your speed is okay")

class SportCar(Car):
    pass

class WorkCar(Car):
    def shown_speed(self):
        if self.speed > 40:
            print("You drive too fast! Slow down!")
        else:
            print("Your speed is okay")

class PoliceCar(Car):
    pass

town_car = Car(85, "white", "Volkswagen", False)
print("\n", town_car.go(), town_car.shown_speed(), town_car.turn('left'), town_car.stop())

sport_car = Car(120, "black", "Audi", False)
print("\n", sport_car.go(), sport_car.shown_speed(), sport_car.turn('left'), sport_car.turn('right'), sport_car.turn('left'),
      sport_car.stop())

work_car = Car(63, "gray", "Nissan", False)
print("\n", work_car.go(), work_car.shown_speed(), work_car.turn('right'), work_car.stop())

police_car = Car(78, "blue", "Ford", True)
print("\n", police_car.go(), police_car.shown_speed(), police_car.turn('right'), police_car.turn('left'), police_car.stop())