import turtle

screen = turtle.Screen()
screen.title("US States game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")




 



screen.exitonclick()