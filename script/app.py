from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api, win32con
from PIL import ImageGrab
import tkinter as tk
from tkinter import filedialog, Text
import os
import sys
import threading



def none():
    print("You clicked me")

def click(x,y):
    win32api.SetCursorPos((int(np.random.uniform(x - 2, x + 2)),int(np.random.uniform(y - 2, y + 2))))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(np.random.uniform(0.08,0.13))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    print("X: ",x," Y: ",y," clicked")

def start_bot_thread():
    bot_thread = threading.Thread(target=start)
    bot_thread.start()

running = True
def start():
    print("[+]Turning on the bot, 3 seconds left")
    time.sleep(3)
    if pyautogui.locateOnScreen("./images/sauda.png", confidence=0.8, grayscale=True) != None:
        print("[+]Sauda has been located, searching for play button")
        time.sleep(0.5)
        clickPlay()
    else:
        print("[-]Sauda has not been located, please equip her and try again")
        return 0
    
def clickPlay():
    if pyautogui.locateOnScreen("./images/play.png", confidence=0.8, grayscale=True) != None:
        print("[+]Playbutton has been located, clicking it")
        x, y = pyautogui.locateCenterOnScreen("./images/play.png", confidence=0.8, grayscale=True)
        click(x,y)
        time.sleep(2)
        clickOnMap()
    else:
        print("[-]Playbutton has not been located, try again")
        return 0

def clickOnMap():
    if pyautogui.locateOnScreen("./images/mapOne.png", confidence=0.8, grayscale=True) != None:
        print("[+]Map has been located, clicking it")
        x, y = pyautogui.locateCenterOnScreen("./images/mapOne.png", confidence=0.8, grayscale=True)
        click(x,y)
        time.sleep(0.5)
        chooseDifficulty()
    else:
        print("[-]Map Moneky Meadow has not been located, try again")
        return 0

def chooseDifficulty():
    if pyautogui.locateOnScreen("./images/easyMapOne.png", confidence=0.8, grayscale=True) != None:
        print("[+]Easy difficulty has been located, clicking it")
        x, y = pyautogui.locateCenterOnScreen("./images/easyMapOne.png", confidence=0.8, grayscale=True)
        click(x,y)
        time.sleep(0.5)
        chooseStandard()
    else:
        print("[-]Easy difficulty has not been located, try again")
        return 0
    
def chooseStandard():
    if pyautogui.locateOnScreen("./images/standard.png", confidence=0.8, grayscale=True) != None:
        print("[+]Standard mode has been located, clicking it")
        x, y = pyautogui.locateCenterOnScreen("./images/standard.png", confidence=0.8, grayscale=True)
        click(x,y)
        time.sleep(4)
        clickSauda()
    else:
        print("[-]Standard has not been located, try again")
        return 0

def clickSauda():
    if pyautogui.locateOnScreen("./images/saudaTwo.png", confidence=0.8, grayscale=True) != None:
        x, y = pyautogui.locateCenterOnScreen("./images/saudaTwo.png", confidence=0.8, grayscale=True)
        click(x,y)
        time.sleep(0.5)
        placeSauda()
    else:
        print("[-]Oops! Something went wrong.")
        return 0

def placeSauda():
    if pyautogui.locateOnScreen("./images/spotForSauda.png", confidence=0.8, grayscale=True) != None:
        x, y = pyautogui.locateCenterOnScreen("./images/spotForSauda.png", confidence=0.8, grayscale=True)
        click(x,y)
        time.sleep(0.5)
        speedButtonDubleClick()
    else:
        print("[-]placeSauda error")
        return 0

def speedButtonDubleClick():
    if pyautogui.locateOnScreen("./images/speedButton.png", confidence=0.8, grayscale=True) != None:
        x, y = pyautogui.locateCenterOnScreen("./images/speedButton.png", confidence=0.8, grayscale=True)
        click(x,y)
        time.sleep(0.5)
        click(x,y)
        time.sleep(90)
        clickSpike()
    else:
        print("[-]speedButtonDubleClick error.")
        return 0
    
def clickSpike():
    if pyautogui.locateOnScreen("./images/spike.png", confidence=0.8, grayscale=True) != None:
        x, y = pyautogui.locateCenterOnScreen("./images/spike.png", confidence=0.8, grayscale=True)
        click(x,y)
        time.sleep(0.5)
        placeSpike()
    else:
        print("[-]spikeclick error.")


def placeSpike():
    if pyautogui.locateOnScreen("./images/spikeSpot.png", confidence=0.8, grayscale=True) != None:
        x, y = pyautogui.locateCenterOnScreen("./images/spikeSpot.png", confidence=0.8, grayscale=True)
        click(x,y)
        time.sleep(0.5)
        upgradesSpike()
    else:
        print("[-]spikeclick error.")

def upgradesSpike():
    if pyautogui.locateOnScreen("./images/spikeUpgrade.png", confidence=0.8, grayscale=True) != None:
        x, y = pyautogui.locateCenterOnScreen("./images/spikeUpgrade.png", confidence=0.8, grayscale=True)
        click(x,y)
        time.sleep(0.5)
        ux, uy = pyautogui.locateCenterOnScreen("./images/spikeRangeI.png", confidence=0.8, grayscale=True)
        click(ux,uy)
        time.sleep(0.5)
        click(ux,uy)
        time.sleep(0.5)
        ux2, uy2 = pyautogui.locateCenterOnScreen("./images/spikeFastI.png", confidence=0.8, grayscale=True)
        click(ux2,uy2)
        time.sleep(0.5)
        runningII = True
        runningIII = True
        runningIV = True
        while runningII:
            if pyautogui.locateOnScreen("./images/spikeFastII.png", confidence=0.8, grayscale=True) != None:
                ux3, uy3 = pyautogui.locateCenterOnScreen("./images/spikeFastII.png", confidence=0.8, grayscale=True)
                click(ux3,uy3)
                time.sleep(0.5)
                runningII = False

        while runningIII:
            if pyautogui.locateOnScreen("./images/spikeFastIII.png", confidence=0.8, grayscale=True) != None:
                ux4, uy4 = pyautogui.locateCenterOnScreen("./images/spikeFastIII.png", confidence=0.8, grayscale=True)
                click(ux4,uy4)
                time.sleep(0.5)
                runningIII = False

        while runningIV:
            if pyautogui.locateOnScreen("./images/spikeFastIV.png", confidence=0.8, grayscale=True) != None:
                ux5, uy5 = pyautogui.locateCenterOnScreen("./images/spikeFastIV.png", confidence=0.8, grayscale=True)
                click(ux5,uy5)
                time.sleep(0.5)
                runningIV = False
        print("Spike done")
        #upgradesPlane()
        goToMenu()
    else:
        print("[-]upgrade error.")


def goToMenu():
    runningNext = True
    while runningNext:
            if pyautogui.locateOnScreen("./images/next.png", confidence=0.8) != None:
                x, y = pyautogui.locateCenterOnScreen("./images/next.png", confidence=0.8)
                click(x,y)
                time.sleep(0.5)
                runningNext = False

    runningHome = True
    while runningHome:
            if pyautogui.locateOnScreen("./images/home.png", confidence=0.8) != None:
                x2, y2 = pyautogui.locateCenterOnScreen("./images/home.png", confidence=0.8)
                click(x2,y2)
                time.sleep(0.5)
                runningHome = False
                start_bot_thread()
    





# Plane not needed
#def upgradesPlane():
#    time.sleep(20)
#    x, y = pyautogui.locateCenterOnScreen("./images/plane.png", confidence=0.8)
#    click(x,y)
#    time.sleep(0.5)
#    x2, y2 = pyautogui.locateCenterOnScreen("./images/planeSpot.png", confidence=0.8)
#    click(x,y)
#    time.sleep(4)
#    planeRun = True
#    planeRunRapidI = True
#    planeRunRapidII = True
#    planeRunSharpI = True
#    planeRunSharpII = True
#    planeRunSharpIII = True
#    while planeRun:
#        if pyautogui.locateOnScreen("./images/planeRunWay.png", confidence=0.8, grayscale=True) != None:
#            x3, y3 = pyautogui.locateCenterOnScreen("./images/planeRunWay.pngg", confidence=0.8)
#            click(x3,y3)
#            time.sleep(0.5)
#            planeRun = False
#    while planeRunRapidI:
#        if pyautogui.locateOnScreen("./images/planeRapidI.png", confidence=0.8, grayscale=True) != None:
#            x4, y4 = pyautogui.locateCenterOnScreen("./images/planeRapidI.png", confidence=0.8)
#            click(x4,y4)
#            time.sleep(0.5)
#            planeRunRapidI = False
#
#    while planeRunRapidII:
#        if pyautogui.locateOnScreen("./images/planeRapidII.png", confidence=0.8, grayscale=True) != None:
#            x5, y5 = pyautogui.locateCenterOnScreen("./images/planeRapidII.png", confidence=0.8)
#            click(x5,y5)
#            time.sleep(0.5)
#            planeRunRapidII = False
#    
#    while planeRunSharpI:
#        if pyautogui.locateOnScreen("./images/planeSharpI.png", confidence=0.8, grayscale=True) != None:
#            x6, y6 = pyautogui.locateCenterOnScreen("./images/planeSharpI.png", confidence=0.8)
#            click(x6,y6)
#            time.sleep(0.5)
#            planeRunSharpI = False
#
#    while planeRunSharpII:
#        if pyautogui.locateOnScreen("./images/planeSharpII.png", confidence=0.8, grayscale=True) != None:
#            x6, y6 = pyautogui.locateCenterOnScreen("./images/planeSharpII.png", confidence=0.8)
#            click(x6,y6)
#            time.sleep(0.5)
#            planeRunSharpII = False
#
#    while planeRunSharpIII:
#        if pyautogui.locateOnScreen("./images/planeSharpIII.png", confidence=0.8, grayscale=True) != None:
#            x8, y8 = pyautogui.locateCenterOnScreen("./images/planeSharpIII.png", confidence=0.8)
#            click(x8,y8)
#            time.sleep(0.5)
#            planeRunSharpIII = False

#Application
root = tk.Tk()
root.title("Bloons TD6 Auto bot by Alex-G-R")
icon_path = "./Icon/icon.ico"
root.iconbitmap(icon_path)

canvas = tk.Canvas(root, height=500, width=800, bg="black")
canvas.pack()

#Start the bot
startBot = tk.Button(root, text="Start the Bot",command=start_bot_thread, padx=10, pady = 5, fg="white", bg="gray", height=2, width=50)
canvas.create_window(195, 33, window=startBot)

#Stop the bot
stopBot = tk.Button(root, text="Stop the Bot",command=none, padx=10, pady = 5, fg="white", bg="gray", height=2, width=50)
canvas.create_window(195, 468, window=stopBot)

#autoUpgradeCastle = tk.Button(root, text="Something", command=none, fg="white", bg="gray", height=2, width=25)
#canvas.create_window(100, 415, window=autoUpgradeCastle)
#
#autoUpgrade = tk.Button(root, text="Something", command=none, fg="white", bg="gray", height=2, width=25)
#canvas.create_window(290, 415, window=autoUpgrade)
#
#autoChest = tk.Button(root, text="Something", command=none, fg="white", bg="gray", height=2, width=52)
#canvas.create_window(195, 367, window=autoChest)

output_text = tk.Text(root, height=30, width=50, fg="white", bg="black")
canvas.create_window(590, 250, window=output_text)

#Redirect output to the text widet
def redirect_stdout(target_widget):
    class StdoutRedirector:
        def __init__(self, text_widget):
            self.text_widget = text_widget

        def write(self, message):
            self.text_widget.config(state=tk.NORMAL)  # Enable writing
            self.text_widget.insert("end", message)
            self.text_widget.see("end")  # Scroll to the end
            self.text_widget.config(state=tk.DISABLED)  # Disable writing

        def flush(self):
            pass

    sys.stdout = StdoutRedirector(target_widget)

    sys.stdout = StdoutRedirector(target_widget)

redirect_stdout(output_text)

root.mainloop()