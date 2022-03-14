class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Start rendering")

class Pen(Stationery):
    def draw(self):
        print(f"Draw calligraphic letters with a {self.title}")

class Pencil(Stationery):
    def draw(self):
        print(f"Draw a cat with a {self.title}")

class Handle(Stationery):
    def draw(self):
        print(f"Draw graffiti with a {self.title}")

i_pen = Pen("pen")
i_pencil = Pencil("pencil")
i_handle = Handle("handle")
i_brush = Stationery("brush")

print(i_pen.draw())
print(i_pencil.draw())
print(i_handle.draw())
print(i_brush.draw())