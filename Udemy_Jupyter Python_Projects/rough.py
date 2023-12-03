from time import strftime
import datetime
import tkinter as tk
import itertools

now = datetime.datetime.now()
str_currenttime = now.strftime("%H:%M:%S %p")
print(str_currenttime)


root = tk.Tk()
image = tk.PhotoImage(file="1.png")
label = tk.Label(root, image=image)
label.pack()
root.mainloop()


colors = ['red', 'green', 'blue']

color_cycle = itertools.cycle((colors[i],i) for i in range(3))

for i in range(3):
    x,y = next(color_cycle)
    print("first value is {} and second value is {}".format(x,y))

z=12
if z==10:
    print("z is 10")
elif z==11:
    print('11')
else:
    print('finally')
