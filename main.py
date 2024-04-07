from tkinter import *


def calculate_bmi():
    kg = entry1.get()
    cm = entry2.get()

    if kg and cm:
        try:
            kg = int(kg)
            cm = int(cm)
        except ValueError:
            result_label.config(text="Enter valid numbers!", fg="red")
            return

        cm2 = int(cm) ** 2
        r = kg / (cm2 / (10 ** 4))

        if 0 < kg < 500 and 0 < cm < 300:
            if r >= 30.0:
                result_label.config(text=f"{r:.2f}: Obesity")
            elif 25 <= r < 30:
                result_label.config(text=f"{r:.2f}: Overweight")
            elif 18.5 <= r < 25:
                result_label.config(text=f"{r:.2f}: Normal weight")
            elif r < 18.5:
                result_label.config(text=f"{r:.2f}: Underweight")
        else:
            result_label.config(text="Invalid input range!", fg="red")
    else:
        result_label.config(text="Enter weight and height!", fg="red")


window = Tk()
window.title("BMI Calculator")
window.minsize(width=150, height=150)


labelKg = Label(text="Enter Your Weight (kg)", font=("Arial", 7, "normal"))
labelKg.pack()
labelKg.update()
labelKg.place(x=24, y=15)
# print(labelKg.winfo_width())
# print(labelKg.winfo_height())

entry1 = Entry(width=11)
entry1.focus()
entry1.pack()
entry1.place(x=40, y=30)



labelCm = Label(text="Enter Your Height (cm)", font=("Arial", 7, "normal"))
labelCm.pack()
labelCm.place(x=24, y=50)

entry2 = Entry(width=11)
entry2.pack()
entry2.place(x=40, y=65)

button = Button(text="Calculate", width=7, height=1, command=calculate_bmi)
button.pack()
button.place(x=45, y=90)

result_label = Label(window, text="", fg="green")
result_label.pack()
result_label.place(y=110)

window.mainloop()