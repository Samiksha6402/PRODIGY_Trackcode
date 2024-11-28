import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Conversion functions
def ctf(celsius):
    return (celsius * 9/5) + 32

def ctk(celsius):
    return celsius + 273.15

def ftc(fahrenheit):
    return (fahrenheit - 32) * 5/9

def ftk(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def ktc(kelvin):
    return kelvin - 273.15

def ktf(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature():
    try:
        temp = float(entry_temp.get())
        unit = unit_var.get()
        output_text.delete("1.0", tk.END) 
        if unit == "Celsius":
            fahrenheit = ctf(temp)
            kelvin = ctk(temp)
            display("Fahrenheit", fahrenheit, "Kelvin", kelvin)
        elif unit == "Fahrenheit":
            celsius = ftc(temp)
            kelvin = ftk(temp)
            display("Celsius", celsius, "Kelvin", kelvin)
        elif unit == "Kelvin":
            celsius = ktc(temp)
            fahrenheit = ktf(temp)
            display("Celsius", celsius, "Fahrenheit", fahrenheit)
        else:
            output_text.insert("1.0", "Please select a valid unit.")
    except ValueError:
        output_text.delete("1.0", tk.END)
        output_text.insert("1.0", "Invalid input. Please enter a numeric value.")

def display(unit1, value1, unit2, value2):
    output_text.insert(tk.END, f"{unit1}: ", "blue")
    output_text.insert(tk.END, f"{value1:.2f}\n", "black")
    output_text.insert(tk.END, f"{unit2}: ", "blue")
    output_text.insert(tk.END, f"{value2:.2f}\n", "black")

root = tk.Tk()
root.geometry("400x300")

background_image = Image.open("Mortality Attributed to Anthropogenic Warming.jpg")  
background_image = background_image.resize((400, 300))
bg_image = ImageTk.PhotoImage(background_image)

canvas = tk.Canvas(root, width=400, height=300)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_image, anchor="nw")


canvas.create_text(200, 30, text="Temperature Converter", font=("Arial", 16, "bold"), fill="white")


label_input = ttk.Label(root, text="Enter the temperature value:")
label_input.config(background=root.cget('background'))  
canvas.create_window(200, 50, window=label_input)


entry_temp = ttk.Entry(root)
canvas.create_window(200, 90, window=entry_temp, width=150)  

unit_var = tk.StringVar(value="Celsius")
unit_menu = ttk.Combobox(root, textvariable=unit_var, values=["Celsius", "Fahrenheit", "Kelvin"])
canvas.create_window(200, 130, window=unit_menu, width=150)

convert_button = ttk.Button(root, text="Convert", command=convert_temperature)
canvas.create_window(200, 170, window=convert_button)


output_text = tk.Text(root, height=4, width=30, wrap="word", background="white", borderwidth=0)
output_text.tag_configure("blue", foreground="blue", font=("Arial", 10, "bold"))
output_text.tag_configure("black", foreground="black", font=("Arial", 10))
canvas.create_window(200, 220, window=output_text)
root.mainloop()
