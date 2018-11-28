from tkinter import *

window = Tk()


def kg_convert():
    grams = entry1_value.get() * 1000
    pounds = entry1_value.get() * 2.20462
    ounces = entry1_value.get() * 35.274
    text1.delete("1.0", END)
    text1.insert(END, grams)
    text2.delete("1.0", END)
    text2.insert(END, pounds)
    text3.delete("1.0", END)
    text3.insert(END, ounces)


label1 = Label(window, text="Kg")
label1.grid(row=0, column=0)

entry1_value = IntVar()
entry1 = Entry(window, textvariable=entry1_value)
entry1.grid(row=0, column=1)

button1 = Button(window, text="Execute", command=kg_convert)
button1.grid(row=0, column=2)

text1 = Text(window, height=1, width=20)
text1.grid(row=1, column=0)

text2 = Text(window, height=1, width=20)
text2.grid(row=1, column=1)

text3 = Text(window, height=1, width=20)
text3.grid(row=1, column=3)
window.mainloop()
