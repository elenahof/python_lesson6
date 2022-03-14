class Road:
    def __init__(self, length, width):
        self._lenth = length
        self._width = width
        self.weigth = 25
        self.depth = 5

    def asphalt(self):
        asphalt = self._lenth * self._width * self.depth * self.weigth / 1000
        print(f"Asphalt weigth: {asphalt} ton")


obj = Road(5000, 45)
obj.asphalt()