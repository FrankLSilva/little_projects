import tkinter

def calculate():
    number1 = float(respond.get())
    result = float(number1 * 1.609)
    answer.config(text=result)


window = tkinter.Tk()
window.title("Mile to KM converter")
window.config(padx=30, pady=30)

label0 = tkinter.Label(text="Miles")
label1 = tkinter.Label(text="Is equal to")
label2 = tkinter.Label(text="KM")
answer = tkinter.Label(text="0")

label0.grid(column=3, row=1)
label1.grid(column=1, row=2)
label2.grid(column=3, row=2)
answer.grid(column=2, row=2)

respond = tkinter.Entry()
respond.grid(column=2, row=1)

button = tkinter.Button(text="Calculate", command=calculate)
button.grid(column=2, row=3)
button.config(padx=10, pady=10)


window.mainloop()
