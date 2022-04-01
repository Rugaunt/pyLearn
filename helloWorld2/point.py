class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        print('move')
        self.x += x
        self.y += y

    def draw(self):
        print('draw')


thePoint = Point()
thePoint.draw()
thePoint.move()
thePoint.x = 10
thePoint.y = 10



