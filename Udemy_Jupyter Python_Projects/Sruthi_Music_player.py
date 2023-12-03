import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os


Label(window,font="Helvetica 12", text="Chinna's Music Player",bg="Blue",).grid(row=12, column=2)

PlayButton = Button(window,width=5,height=3, font="Helvetica 12 bold",text="PLAY",command=test,bg="red",fg="white")
StopButton = Button(window,width=5,height=3, font="Helvetica 12 bold",text="STOP",command=test,bg="purple",fg="white")
PauseButton = Button(window,width=5,height=3, font="Helvetica 12 bold",text="PAUSE",command=test,bg="green",fg="white")
UnPauseButton = Button(window,width=5,height=3, font="Helvetica 12 bold",text="UNPAUSE",command=test,bg="blue",fg="white")
SelectSonglistButton =  Button(window,width=5,height=3, font="Helvetica 12 bold",text="SELECT SONGS",command=test,bg="Yellow",fg="white")

PlayButton.grid(row=13,column=1)
StopButton.grid(row=13,column=2)
PauseButton.grid(row=14,column=1)
UnPauseButton.grid(row=14,column=2)
SelectSonglistButton.grid(row=15,column=1)

def __del__(self):
print ("here in del")
pygame.mixer.music.stop()

def play(self):
    print("here")
    
def ExitMusicPlayer(self):
    #pygame.mixer.music.stop()
    # def pause(self):
    print("here in exit music player")

def unpause(self):
    print("here")

def SelectSongs(self):
    print("here")


def on_closing(mp):
mp.ExitMusicPlayer()
window.destroy()

def test():
print("hello")


#window.protocol("WM_DELETE_WINDOW", on_closing)
Music_player()
