import turtle
import state

screen = turtle.Screen()
screen.title("US States game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

correct_answers = 0
window_title = f"0/50 States correct"
guessed_states = []
while len(guessed_states) < 50:
    user_guess = screen.textinput(title=window_title, prompt="What's another state's name?")
    state_obj = state.State(user_guess)
    if state_obj.state_name in guessed_states:
        window_title = f"Already on the map."
    elif state_obj.is_name_ok():
        state_obj.put_name_in_place()
        correct_answers += 1
        window_title = f"{correct_answers}/50 States correct"
        guessed_states.append(state_obj.state_name)
    else:
        window_title = f"Wrong! Try again."

screen.exitonclick()
