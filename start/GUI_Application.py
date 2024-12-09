import tkinter as tk

def convert_speed():
    try:
        kph = float(entry_kph.get())
        mph = kph / 1.60934
        label_result.config(text=f"{mph:.2f} mph")
    except ValueError:
        label_result.config(text="Invalid input")

window = tk.Tk()
window.title("Speed Converter")

label_kph = tk.Label(window, text="Kilometers per Hour (KPH):")
label_kph.grid(row=0, column=0)

entry_kph = tk.Entry(window)
entry_kph.grid(row=0, column=1)

button_convert = tk.Button(window, text="Convert", command=convert_speed)
button_convert.grid(row=1, column=0, columnspan=2)

label_result = tk.Label(window, text="")
label_result.grid(row=2, column=0, columnspan=2)

window.mainloop()
