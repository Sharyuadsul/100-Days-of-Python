import tkinter

def button_click():
    print("i got clicked")
    user_input = input.get()
    my_label.config(text=f"{user_input}")


window = tkinter.Tk()
window.title("My First GUI")
window.minsize(height=500, width=600)
window.config(padx=30,pady=30)

#label
my_label = tkinter.Label(text="Its a Label", font=("arial", 20, "bold"))
# my_label.pack(side="bottom")
# my_label.pack(expand = True)
my_label["text"] ="new text"
my_label.config(text="new_text")
# my_label.pack()
# my_label.place(x=0, y=0)
my_label.grid(row=0, column =0)
my_label.config(padx=10,pady=10)


#button
button = tkinter.Button(text="click me", command=button_click)
# button.pack()
# button.place(x=100,y=100)
button.grid(row=1,column=1)
button.config(padx=10,pady=10)


new_butt= tkinter.Button(text = "new button")
new_butt.grid(row= 0, column = 2)


#entry

input = tkinter.Entry(width=15)
print(input.get())
# input.pack()
# input.place(x=300,y=0)
input.grid(row = 1, column=3)






window.mainloop()