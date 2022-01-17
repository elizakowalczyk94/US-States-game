import pandas
from turtle import Turtle

CSV_NAME = "50_states.csv"
ALIGNMENT = "center"
FONT = ("Courier", 10, "normal")


class State(Turtle):

    def __init__(self, state_name):
        super().__init__()
        self.state_name = state_name
        self.states_file = pandas.read_csv(CSV_NAME)
        self.penup()
        self.hideturtle()
        self.color("black")

    def is_name_ok(self):
        states_list = self.states_file.state.to_list()
        if self.state_name in states_list:
            return True
        else:
            return False

    def get_coordinates(self):
        if self.is_name_ok():
            state_cor = self.states_file[self.states_file.state == self.state_name]
            x_cor = state_cor.x
            y_cor = state_cor.y
            return x_cor, y_cor
        else:
            return False

    def put_name_in_place(self):
        x, y = self.get_coordinates()
        self.goto(x, y)
        self.write(arg=self.state_name,
                   move=False,
                   align=ALIGNMENT,
                   font=FONT)
