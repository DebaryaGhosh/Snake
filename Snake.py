import turtle as tr

MOVE_DISTANCE = 20
GAP = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.X = 0
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(3):
            self.add_segment((0, 0))

    def extend(self):
        self.add_segment(self.segments[-1].pos())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].pos())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() == DOWN:
            return
        self.head.setheading(90)

    def down(self):
        if self.head.heading() == UP:
            return
        self.head.setheading(270)

    def left(self):
        if self.head.heading() == RIGHT:
            return
        self.head.setheading(180)

    def right(self):
        if self.head.heading() == LEFT:
            return
        self.head.setheading(0)

    def add_segment(self, position):
        new_segment = tr.Turtle()
        new_segment.shape("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.speed("fastest")
        new_segment.goto(position)
        self.segments.append(new_segment)
