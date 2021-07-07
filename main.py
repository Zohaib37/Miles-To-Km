from  tkinter import *
FONT = ("Ariel", 15, "italic")


def convert():
    miles = float(entry.get())
    km = miles * 1.609
    format_km = "{:.2f}".format(km)
    converter_label.config(text=format_km)


window = Tk()
window.title("Miles to Km Converter")
window.config(padx=30, pady=30)

entry = Entry(width=10, bd=3)
entry.grid(row=0, column=1, padx=10)

label1 = Label(text="Miles", font=FONT)
label2 = Label(text="is equal to", font=FONT)
converter_label = Label(text="", font=FONT, fg="medium sea green")
km_label = Label(text="Km", font=FONT)

label1.grid(row=0, column=3)
label2.grid(row=1, column=0)
converter_label.grid(row=1, column=1, pady=10)
km_label.grid(row=1, column=3)

button = Button(text="Convert", command=convert, fg="DodgerBlue2", font=("ariel", 12, "italic"))
button.grid(row=3, column=1)










window.mainloop()
