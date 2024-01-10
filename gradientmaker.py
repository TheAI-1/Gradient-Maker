import copy
import tkinter as tk
import random

#creating the window and canvas using the tkinter library
window = tk.Tk()
window.geometry("1000x500")
canvas = tk.Canvas(window, width=1000, height=500, bg="lightblue")
canvas.grid(column=0, row=0)

#input values
colour1 = [0, 191, 172]
colour2 = [255, 33, 170]
resolution = 5
point = 0.3

#gradient maker
difference = []
increases = []
resolution -= 1
gradient = [colour1]
total = copy.deepcopy(colour1) #total was changing colour1 with just doing total = colour1 (with = it just refers to the same point in memory)
for i in range(3):
    difference.append(colour1[i] - colour2[i]) #finds the differences between the rgb values of the colours
    increases.append(difference[i]/resolution) #divides the differences by the resolution to find the step size
for i in range(resolution): #repeats for how many different colours you want
    temp = []
    for j in range(3): #3 because 3 different values in each part of the list (rgb)
        temp.append(total[j] - increases[j]) #adding the current value (r g or b) to a temporary array so it can be added to the gradient array
        total[j] -= increases[j] #finds the total (not sure why i needed this)
    gradient.append(temp) #saves the temporary value to the "gradient" array
x = 0
y = 0
step = 1000/(resolution+1)


#placing the gradient into the window
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
