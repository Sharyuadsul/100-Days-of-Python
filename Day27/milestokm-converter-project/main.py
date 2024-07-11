from tkinter import *

def miles_to_km():
    num = float(miles_input.get())
    km = 1.609*num
    result_label.config(text = f"{km}")

window = Tk()
window.title("Miles to Kilo Convertor")
# window.minsize(height=200,width=300)
window.config(padx=20, pady=20)

miles_input = Entry(width=15)
miles_input.grid(row=0, column = 1)

miles_label = Label(text="miles")
miles_label.grid(row=0, column=2)

is_equal_label = Label(text="is equal to ")
is_equal_label.grid(row=1, column=0)


result_label = Label(text='0')
result_label.grid(row=1, column=1)


km_label = Label(text="km")
km_label.grid(row=1, column=2)


calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(row=2, column=1)



window.mainloop()