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
resolution = 1000
point = 0.75

#gradient maker
difference = []
increases = []
resolution -= 1 #taking into account the first colour, so that the inputted resolution will equal the displayed resolution
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
    hexgradient = [] #creates/resets the array for the hexidecimal form of each value
    for j in range(3):
        temp = hex(int(gradient[i][j])) #creates a temporary variable for the hexidecimal value
        temp = temp.replace("0x","") #turns the value into hex
        if len(temp) == 1:
            temp = "0" + temp
        hexgradient.append(temp) #adds the hex value to the hexidecimal value array

    colour = "#" + hexgradient[0] + hexgradient[1] + hexgradient[2] #creates a colour based on the hexadecimal array
    canvas.create_rectangle(x, y, x+step, y+500, fill=colour, outline=colour) #places the coloured block on the canvas
    x += step #finds the x coordinate for the next colour

#colour point finder
increase = [] #resets the increases array for use in the point finder
pointcolour = [] #creates a new empty array to store the rgb values of the point
for i in range(3):
    increase.append(difference[i]*point) #multiplies the differences by the point in order to find how much higher the value for each colour should be
    pointcolour.append(colour1[i]-increase[i]) #finds the colour of the point

#generating the hexidecimal values for the rgb - for the most part the same process as above, just with one colour
colour = []
for i in range(3):
    temp = hex(int(pointcolour[i]))
    temp = temp.replace("0x","")
    if len(temp) == 1:
        temp = "0" + temp
    colour.append(temp)

colour = "#" + colour[0] + colour[1] + colour[2] #creates the full hexidecimal code for the colour
canvas.create_rectangle(0, y+450, 1000, y+500, fill=colour, outline=colour) #places the colour on the canvas
