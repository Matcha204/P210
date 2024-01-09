import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
import ftplib
import os
import time
import ntpath #This is used to extract filename from path

from tkinter import filedialog
from pathlib import Path


from playsound import playsound
import pygame
from pygame import mixer

PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096


name = None
listbox =  None
textarea= None
labelchat = None
text_message = None

def connectToServer():
    global SERVER
    global name
    global send_file
    cname= name.get()
    SERVER.send(cname.encode())

def play():
    global song_selected
    song_selected=listbox.get(ANCHOR)

    pygame
    mixer.init()
    mixer.music.load('shared_files'+song_selected)
    mixer.music.play()
    if(song_selected != ""):
        infolabel.configure(text="Now Playing" + song_selected)
    else:
        infolabel.configure(text="")

def stop():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.pause()
    infolabel.configure(text="")
    
def musicWindow():

   
    print("\n\t\t\t\tMUSIC SHARING")

    #Client GUI starts here
    window=Tk()

    window.title('Music Sharing')
    window.geometry("500x350")

    global name
    global listbox
    global textarea
    global labelchat
    global text_message
    global filePathLabel

    namelabel = Label(window, text= "Enter Your Name", font = ("Calibri",10))
    namelabel.place(x=10, y=8)

    name = Entry(window,width =30,font = ("Calibri",10))
    name.place(x=120,y=8)
    name.focus()

    selectsong = Button(window,text="Select Song",bd=1, font = ("Calibri",10))
    selectsong.place(x=350,y=6)

    separator = ttk.Separator(window, orient='horizontal')
    separator.place(x=0, y=35, relwidth=1, height=0.1)

    labelusers = Label(window, text= "Active Users", font = ("Calibri",10))
    labelusers.place(x=10, y=50)

    listbox = Listbox(window,height = 5,width = 67,activestyle = 'dotbox', font = ("Calibri",10))
    listbox.place(x=10, y=70)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listbox.yview)

    playbutton=Button(window,text="Play",bd=1, font = ("Calibri",10), command=play)
    playButton.place(x=282,y=160)

    stopButton=Button(window,text="Stop",bd=1, font = ("Calibri",10), command=stop)
    stopButton.place(x=350,y=160)

    upload=Button(window,text="Upload",bd=1, font = ("Calibri",10))
    upload.place(x=435,y=160)

    download=Button(window,text="Download",bd=1, font = ("Calibri",10))
    download.place(x=550,y=160)

    infolabel = Label(window, text="Chat Window", font=("Calibri",10))
    infolabel.place(x=10,y=180)

    textarea = Text(window, width= 67, height= 6, font= ("Calibri",10))
    textarea.place(x=10,y=200)

    scrollbar = Scrollbar(textarea)
    scrollbar.place(relheight = 1, relx = 1)
    scrollbar.config(command = listbox.yview)

    text_message = Entry(window, width = 43, font = ("Calibri",12))
    text_message.pack()
    text_message.place(x= 19, y=306)

    attach = Button(window, text = "Attach and Send", bd=1, font= ('Calibri',10))
    attach.place(x=10,y=305)

    filePathLabel = Label(window, text="", fg="blue", font=("Calibri",8))
    filePathLabel.place(x=10,y=330)
  
  
  
  
  
    window.mainloop()




def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

   
    musicWindow()

setup()

