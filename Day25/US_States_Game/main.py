import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US State Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

df = pd.read_csv("50_states.csv")
all_states = df.state.to_list()
guessed_list = []
missing_list = []

while len(guessed_list)<50:
    ans = screen.textinput(title=f"{len(guessed_list)}/50 correct states ", prompt="what's the another states name?").title()
    if ans == "Exit":
        #using conditional list comprehension
        missing_list = [state for state in all_states if state not in guessed_list]

        # for states in all_states:
        #     if states not in guessed_list:
        #         missing_list.append(states)
        new_data = pd.DataFrame(missing_list)
        new_data.to_csv("Missing_States.csv")
        break
    if ans in all_states:
        guessed_list.append(ans)
        tim = turtle.Turtle()
        tim.penup()
        tim.hideturtle()
        row = df[df.state == ans]
        x = int(row.x)
        y = int(row.y)
        tim.goto(x, y)
        tim.write(arg=ans, align='center', font=('arial', 10, 'normal'))







# turtle.mainloop()
# screen.exitonclick()