import pandas
from turtle import Turtle

CSV_NAME = "50_states.csv"
ALIGNMENT = "center"
FONT = ("Courier", 8, "normal")


class State(Turtle):

    def __init__(self, state_name):
        super().__init__()
        self.state_name = state_name.lower()
        self.states_file = pandas.read_csv(CSV_NAME)
        self.states_list = self.states_file.state.to_list()
        self.penup()
        self.hideturtle()
        self.color("black")

    def is_name_ok(self):
        states_list_lower = [name.lower() for name in self.states_list]
        if self.state_name in states_list_lower:
            return True
        else:
            return False

    def get_coordinates(self):
        state_cor = self.states_file[self.states_file.state == self.state_name.title()]
        x_cor = int(state_cor.x)
        y_cor = int(state_cor.y)
        return x_cor, y_cor

    def put_name_in_place(self):
        x, y = self.get_coordinates()
        self.goto(x, y)
        self.write(arg=self.state_name.title(),
                   move=False,
                   align=ALIGNMENT,
                   font=FONT)

    def get_missed_states(self, guessed_states):
        states_list_lower = [name.lower() for name in self.states_list]
        missed_states = [item for item in states_list_lower if item not in guessed_states]
        return missed_states
