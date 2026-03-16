import tkinter as tk
import random
import pygame
import math

# Initialize pygame mixer for music
pygame.mixer.init()
pygame.mixer.music.load("neelothi.mp3")
pygame.mixer.music.play(-1)

# Create window
root = tk.Tk()
root.title("Birthday wish")
root.geometry("800x600")
root.configure(bg="darkblue")

canvas = tk.Canvas(root, width=800, height=600, bg="skyblue", highlightthickness=0)
canvas.pack()

# Draw cake
canvas.create_rectangle(300,420,500,470,fill="#ffb6c1",outline="")
canvas.create_rectangle(320,380,480,420,fill="#ff69b4",outline="")

# Candles on cake
for i in range(5):
    x = 340 + i*30
    canvas.create_rectangle(x,350,x+10,380,fill="white")
    canvas.create_oval(x-2,340,x+12,355,fill="orange")

# Tamil Birthday Text
colors = ["red","blue","green","purple","black","pink","yellow"]

text = canvas.create_text(
    400,
    120,
    text="Advance Happyy Brithday Panguuuu :) !\n love you so much dah \n miss you more chellowwwwww",
    font=("Arial",20,"bold"),
    fill="black"
)

def change_color():
    canvas.itemconfig(text, fill=random.choice(colors))
    root.after(500, change_color)

change_color()

# Balloons
balloons = []
for i in range(12):
    x = random.randint(50,750)
    y = random.randint(350,600)
    color = random.choice(colors)

    balloon = canvas.create_oval(x,y,x+40,y+50,fill=color,outline="")
    string = canvas.create_line(x+20,y+50,x+20,y+80)

    balloons.append((balloon,string))

def move_balloons():
    for balloon,string in balloons:
        canvas.move(balloon,0,-2)
        canvas.move(string,0,-2)
        pos = canvas.coords(balloon)
        if pos[1] < -60:
            x = random.randint(50,750)
            canvas.coords(balloon,x,600,x+40,650)
            canvas.coords(string,x+20,650,x+20,680)
    root.after(50,move_balloons)

move_balloons()

# Fireworks & Confetti Effect
confetti = []
fireworks = []

def create_confetti():
    for _ in range(30):
        x = random.randint(0, 800)
        y = random.randint(0, 600)
        size = random.randint(5, 10)
        color = random.choice(colors)
        confetti.append(canvas.create_oval(x, y, x+size, y+size, fill=color, outline=""))

def move_confetti():
    for c in confetti:
        canvas.move(c, random.randint(-2,2), random.randint(1,4))
        pos = canvas.coords(c)
        if pos[1] > 800:
            x = random.randint(0, 800)
            canvas.coords(c, x, 0, x + (pos[2]-pos[0]), (pos[3]-pos[1]))
    root.after(100, move_confetti)

def create_firework(x, y):
    points = []
    for angle in range(0, 360, 30):
        rad = angle * 3.14159 / 180

    end_x = x + 50 * random.uniform(0.7, 1.0) * math.cos(rad)
    end_y = y + 50 * random.uniform(0.7, 1.0) * math.sin(rad)
    points.append(canvas.create_line(x, y, end_x, end_y, fill=random.choice(colors), width=2))
    fireworks.extend(points)
    root.after(1500, lambda: [canvas.delete(p) for p in points])

def fireworks_show():
    x = random.randint(100, 700)
    y = random.randint(100, 300)
    create_firework(x, y)
    root.after(2000, fireworks_show)

create_confetti()
move_confetti()
fireworks_show()

# Start the Tkinter event loop
root.mainloop()