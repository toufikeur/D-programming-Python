class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def moev(self):
        print("move")
    def draw(self):
        print("draw")

point = Point(10, 20)
point.x = 10
print(point.x,point.y)