from tkinter import *
import tkinter as tkt
from time import strftime
import datetime

window = tkt.Tk()
window.title("Sruthi's schedule")
window.config(bg="light blue")

#window.geometry("240x580")
def time():
    Label(window,font="Helvetica 14 bold",bg="light blue",fg="Black",text ="Time Now:").grid(row=1, column=1,sticky =E)
    #display current day on next col
    today = datetime.datetime.today()
    day_name = today.strftime("%A")
    Label(window,font="Helvetica 14 bold",bg="Black",fg="white",text =day_name).grid(row=1, column=2,sticky =EW)
    #display current time on 3rd col
    now = datetime.datetime.now()
    str_currenttime = now.strftime("%H:%M:%S %p")
    Label(window,font="Helvetica 14 bold",bg="Black",fg="white",text=str_currenttime).grid(row=1, column=3,sticky =W)
    #lbl.config(text = str_currenttime)
    window.after(1000, time)
    #window.mainloop()

class Sruthi_Schedule():
    def __init__(self):
        #display divder line at the top
        Label(window,font="Helvetica 3 bold",bg="light blue").grid(row=2, column=1,sticky =EW)
        Label(window,font="Helvetica 3 bold",bg="light blue").grid(row=2, column=2,sticky =EW)
        Label(window,font="Helvetica 3 bold",bg="light blue").grid(row=2, column=3,sticky =EW)

        # add label widgets
        #col labels
        Label(window,font="Helvetica 12 bold",bg="purple",text ="Weekday").grid(row=3, column=1,sticky =EW)
        Label(window,font="Helvetica 12 bold",bg="purple",text ="School").grid(row=3, column=2,sticky =EW)
        Label(window,font="Helvetica 12 bold",bg="purple",text ="Skills").grid(row=3, column=3,sticky =EW)

        #row labels
        Label(window,font="Helvetica 12",bg="light blue",text ="Sunday:").grid(row=4, column=1,sticky =E)
        #lbl.pack(anchor = "center",fill = "both",expand=1)
        Label(window,font="Helvetica 12",bg="light blue",text ="Monday:").grid(row=5, column=1,sticky =E)
        Label(window,font="Helvetica 12",bg="light blue",text ="Tuesday:").grid(row=6, column=1,sticky =E)
        Label(window,font="Helvetica 12",bg="light blue",text ="Wednesday:").grid(row=7, column=1,sticky =E)
        Label(window,font="Helvetica 12",bg="light blue",text ="Thursday:").grid(row=8, column=1,sticky =E)
        Label(window,font="Helvetica 12",bg="light blue",text ="Friday:").grid(row=9, column=1,sticky =E)
        Label(window,font="Helvetica 12",bg="light blue",text ="Saturday:").grid(row=10, column=1,sticky =E)
       
        #col values
        #col 2
        Label(window,font="Helvetica 12 bold",bg="Teal",text ="FUN and Family TIME!!!").grid(row=4, column=2,sticky =EW)
        Label(window,font="Helvetica 12",bg="Teal",text ="   8:30 AM   ").grid(row=5, column=2,sticky =EW)
        Label(window,font="Helvetica 12",bg="Teal",text ="   8:30 AM   ").grid(row=6, column=2,sticky =EW)
        Label(window,font="Helvetica 12",bg="Teal",text ="   8:30 AM   ").grid(row=7, column=2,sticky =EW)
        Label(window,font="Helvetica 12",bg="Teal",text ="   8:30 AM   ").grid(row=8, column=2,sticky =EW)
        Label(window,font="Helvetica 12",bg="Teal",text ="   8:30 AM   ").grid(row=9, column=2,sticky =EW)
        Label(window,font="Helvetica 12 bold",bg="Teal",text ="FUN and Family TIME!!!").grid(row=10, column=2,sticky =EW)
        #col 3
        Label(window,font="Helvetica 12",bg="light blue",text ="10:30 AM : Singing").grid(row=4, column=3,sticky =W)
        Label(window,font="Helvetica 12 bold",bg="light blue",text ="FUN and Family TIME!!!   ").grid(row=5, column=3,sticky =W)
        Label(window,font="Helvetica 12",bg="light blue",text ="6:15 PM : Taekwondo").grid(row=6, column=3,sticky =W)
        Label(window,font="Helvetica 12",bg="light blue",text ="7:00 PM : Piano").grid(row=7, column=3,sticky =W)
        Label(window,font="Helvetica 12",bg="light blue",text ="6:15 PM : Taekwondo").grid(row=8, column=3,sticky =W)
        Label(window,font="Helvetica 12",bg="light blue",text ="6:00 PM : Hindi School").grid(row=9, column=3,sticky =W)
        Label(window,font="Helvetica 12",bg="light blue",text ="Fun Time").grid(row=10, column=3,sticky =W)
    
        #Empty row at the end
        Label(window,font="Helvetica 12", text="                                    ",bg="purple",).grid(row=11, column=1)
        Label(window,font="Helvetica 12", text="                                    ",bg="purple",).grid(row=11, column=2)
        Label(window,font="Helvetica 12", text="                                             ",bg="purple",).grid(row=11, column=3)


# main loop below here   
Sruthi_Schedule()
time()
mainloop()