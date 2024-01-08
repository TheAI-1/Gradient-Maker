import copy
import tkinter as tk
import random
window = tk.Tk()
window.geometry("1000x500")
canvas = tk.Canvas(window, width=1000, height=500, bg="lightblue")
canvas.grid(column=0, row=0)

#input values
colour1 = [185, 66, 66]
colour2 = [10, 110, 0]
resolution = 1000
point = 0.3

#gradient maker
difference = []
increases = []
resolution -= 1
gradient = [colour1]
total = copy.deepcopy(colour1)
for i in range(3):
    difference.append(colour1[i] - colour2[i])
    increases.append(difference[i]/resolution)
for i in range(resolution):
    temp = []
    for j in range(3):
        temp.append(total[j] - increases[j])
        total[j] -= increases[j]
    gradient.append(temp)
x = 0
y = 0
step = 1000/(resolution+1)



for i in range(len(gradient)):
    hexgradient = []
    for j in range(3):
        temp = hex(int(gradient[i][j]))
        temp = temp.replace("0x","")
        if len(temp) == 1:
            temp = "0" + temp
        hexgradient.append(temp)

    colour = "#" + hexgradient[0] + hexgradient[1] + hexgradient[2]
    canvas.create_rectangle(x, y, x+step, y+500, fill=colour, outline=colour)
    x += step

#colour point finder
increase = []
pointcolour = []
for i in range(3):
    print(difference)
    increase.append(difference[i]*point)
    pointcolour.append(colour1[i]-increase[i])
print(pointcolour)

colour = []
for i in range(3):
    temp = hex(int(pointcolour[i]))
    temp = temp.replace("0x","")
    if len(temp) == 1:
        temp = "0" + temp
    colour.append(temp)

colour = "#" + colour[0] + colour[1] + colour[2]
canvas.create_rectangle(0, y+450, 1000, y+500, fill=colour, outline=colour)

