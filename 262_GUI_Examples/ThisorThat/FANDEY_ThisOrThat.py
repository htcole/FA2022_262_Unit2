from tkinter import *
import tkinter.font as tkFont
import tkinter as tk
from PIL import Image, ImageTk
root = tk.Tk()

"""
Idea:
    - 5 Rounds
    - Pick This or That
    - If I agree you get a point
    - If I disagree you lose a ponit

"""
score=0
currentLevel=0

img1 = ImageTk.PhotoImage(Image.open("water.png"))
img2 = ImageTk.PhotoImage(Image.open("milk.png"))

def game(): #Clears title screen and starts the game
    global score, mainText
    title.destroy()
    startButton.destroy()
    startLevels(1,0)

def startLevels(y,z): #adds info for level 1, on completion, starts level 2
    global img1, img2, score
    scoreText="Score",score
    definePoints(y,z)#This is correct, if this button is hit you gain a point, else lose a point
    title = Label(root,text="This or That?",font=("Acumin Pro",size))
    title.place(relx=0.5, rely=0.1, anchor=CENTER)
    scLabel = Label(root,text=scoreText,font=("Acumin Pro",size))
    scLabel.place(relx=0.5, rely=0.85, anchor=CENTER)
    canvas1 = Canvas(root, width=500, height=500)
    canvas1.place(relx=0.2, rely=0.5, anchor=CENTER)
    canvas1.create_image(250, 250, image = img1)
    canvas2 = Canvas(root, width=500, height=500)
    canvas2.place(relx=0.8, rely=0.5, anchor=CENTER)
    canvas2.create_image(250, 250, image = img2)
    ThisThatButtons()
   
        
def ThisThatButtons():
    thisButton = Button(root, text="This", command=lambda:finishRound(definePoints.y))
    thisButton.place(relx=0.2, rely=0.85, anchor=CENTER)
    thatButton = Button(root, text="That", command=lambda:finishRound(definePoints.z))
    thatButton.place(relx=0.8, rely=0.85, anchor=CENTER)
    
def pointCalc(x):
    global score
    if(x==1):
        score+=1
    else:
        score-=1
    print(score)

def definePoints(y,z):
    definePoints.y=y
    definePoints.z=z
    
def nextLevel():
    global currentLevel, img1, img2,score
    print(currentLevel)
    if(currentLevel==1):
        img1= ImageTk.PhotoImage(Image.open("ps.png"))
        img2= ImageTk.PhotoImage(Image.open("xbox.png"))
        startLevels(0,1)
    elif(currentLevel==2):
        img1= ImageTk.PhotoImage(Image.open("java.png"))
        img2= ImageTk.PhotoImage(Image.open("python.png"))
        startLevels(0,1)
    elif(currentLevel==3):
        img1= ImageTk.PhotoImage(Image.open("twitter.png"))
        img2= ImageTk.PhotoImage(Image.open("facebook.png"))
        startLevels(1,0)
    elif(currentLevel==4):
        img1= ImageTk.PhotoImage(Image.open("youtube.png"))
        img2= ImageTk.PhotoImage(Image.open("twitch.png"))
        startLevels(0,1)
    elif(currentLevel==5):
        img1=None
        img2=None
        goText = ("Game Over\nYour Score is:",score)
        gameOver = Label(root,text=goText,font=("Acumin Pro",24))
        gameOver.place(relx=0.5,rely=0.2, anchor=CENTER)
        quitButton = Button(root, text="Quit", command=lambda:root.destroy())
        quitButton.place(relx=0.5, rely=0.5, anchor=CENTER)
        canvas = Canvas(root, width=1000, height=500)
        canvas.place(relx=0.5, rely=1, anchor=CENTER)
def finishRound(x):
    global currentLevel
    currentLevel+=1
    pointCalc(x)
    nextLevel()

    

mainText = "Welcome to This or That\n\nThe Game where your opinion doesn't matter!\nPick your favorite item, and if I agree with you, you get a point\nIf not, then you lose a point.\n Good Luck!"
size = 22

root.geometry("1000x800")
title = Label(root,text=mainText,font=("Acumin Pro",size))
title.place(relx=0.5, rely=0.2, anchor=CENTER)

startButton = Button(root, text="Start", command=lambda:game())
startButton.place(relx=0.5, rely=0.5, anchor=CENTER)


    





root.mainloop()