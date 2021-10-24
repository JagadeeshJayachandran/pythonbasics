from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)



    def is_at_finish_line(self):
        new_y = self.ycor() + MOVE_DISTANCE
        if  new_y == FINISH_LINE_Y:
            return True

    def go_to_start(self):
        self.goto(STARTING_POSITION)

