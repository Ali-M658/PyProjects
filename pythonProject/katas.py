import tkinter as tk
import time
from PIL import Image, ImageTk

Digital_clock = tk.Tk()
Digital_clock.title('Online Clock')
Digital_clock.geometry('500x300')
Digital_clock.configure(background='green')

sun_image = Image.open(r"C:\Users\dimao\Downloads\sunphoto.jpg")
sea_image = Image.open(r"C:\Users\dimao\Downloads\sea.jpg")
grass_image = Image.open(r"C:\Users\dimao\Downloads\grass.jpg")

real_sun = ImageTk.PhotoImage(sun_image)
real_sea = ImageTk.PhotoImage(sea_image)
real_grass = ImageTk.PhotoImage(grass_image)
def time_clock():
    current_time = time.strftime("%I:%M:%S %p")
    if '0' in current_time[:1]:
        current_time = current_time[1:]
    current_date = time.strftime("%A, %D , %Y")
    clock_label.config(text=current_time)
    date_label.config(text=current_date)
    clock_label.after(1000, time_clock)

clock_label = tk.Label(Digital_clock, font=("Arial", 45), bg="red",fg="blue")
clock_label.pack(expand=True)

date_label = tk.Label(Digital_clock, font=("arial",45), bg="black", fg="blue")
date_label.pack(expand=True)

background_label = tk.Label(Digital_clock)
background_label.pack(fill = tk.BOTH, expand=True)

def change_sun():
    background_label.config(image = real_sun)

def change_sea():
    background_label.config(image = real_sea)

def change_grass():
    background_label.config(image = real_grass)

def black_color():
    Digital_clock.config(bg="#000000")

button_sun = tk.Button(Digital_clock, text="Click\n for\n Image of sun", command=change_sun)
button_sun.pack()

button_sea = tk.Button(Digital_clock, text="Click\n for\n image of sea", command=change_sea)
button_sea.pack()

button_grass = tk.Button(Digital_clock, text="Click\n for\n image of grass", command=change_grass)
button_grass.pack()

button = tk.Button(Digital_clock, text="Click to get to blackscreen", command=black_color)
button.pack()

time_clock()
Digital_clock.mainloop()

