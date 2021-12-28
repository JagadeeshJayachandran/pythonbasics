from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)

# label

# Entry
input = Entry(width=10)
input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 12, "bold"))
miles_label.grid(column=2, row=0)
miles_label.config(padx=20, pady=5)

equals_label = Label(text="is equal to", font=("Arial", 12, "bold"))
equals_label.grid(column=0, row=1)
equals_label.config(padx=20, pady=5)

result = Label(font=("Arial", 12, "bold"))
result.grid(column=1, row=1)
result.config(padx=20, pady=5)

km_label = Label(text="KM", font=("Arial", 12, "bold"))
km_label.grid(column=2, row=1)
km_label.config(padx=20, pady=5)
#
def button_clicked():
    result.config(text="{:.2f}".format(float(input.get())*1.609))

# button two
button = Button(text="calculate", command=button_clicked, font=("Arial", 12, "bold"))
button.grid(column=1, row=2)



window.mainloop()