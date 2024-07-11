# import another
# print(another.another_var)
#
#
# from turtle import Turtle, Screen
#
# tim = Turtle()
# my_sc = Screen()
# print(tim)
# tim.forward(100)
# tim.color("pink")
# tim.shape("turtle")
#
# print(my_sc.canvheight)
# my_sc.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.fields_names =["pokemon name", "group"]
table.add_row(["sjhjhcbscj", "schsh"])
table.align="l"
print(table)



