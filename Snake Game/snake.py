from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()  # Create a three segments snake at the start_positions
        self.head = self.segments[0]  # This is the head of the snake

    def create_snake(self):
        for position in START_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")  # create an square object
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)  # Set a position of the square object
        self.segments.append(new_segment)  # Add the square object to a list

    def extend(self):
        # add a new section to the snake
        self.add_segment(self.segments[-1].position())

    def move(self):  # this function kep the body together nas moves the body forward
        for seg_num in range(len(self.segments) - 1, 0, -1):  # start the count in the last position
            new_x = self.segments[seg_num - 1].xcor()  # return the x coordinate of my segment
            new_y = self.segments[seg_num - 1].ycor()  # return the y coordinate of my segment
            self.segments[seg_num].goto(new_x, new_y)  # moves the body to the before position
        self.head.forward(MOVE_DISTANCE)  # moves the head ahead

    def up(self):
        if self.head.heading() != DOWN:  # if the head is moving down it don't permit move the head up, the reason,
            # head can't crash with the body
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:  # if the head is moving up it don't permit move the head down
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:  # if the head is moving right don't permit move the head left
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:  # if the head is moving left don't permit move the head right
            self.head.setheading(RIGHT)
