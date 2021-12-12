from flask import Flask, render_template
import pygame
from pygame import mixer
import os
from tkinter import *
import random


app = Flask(__name__)

mixer.init()

curSong = -1
listofFiles = []
path = os.getcwd() + "/Songs"
def randomize():
    global listofFiles
    random.shuffle(listofFiles)
def getAllFiles():
    global path
    global listofFiles
    for root, dirs, files in os.walk(path):
        for file in files:
            listofFiles.append(os.path.join(root,file))
def getNextSong():
    global curSong
    global listofFiles
    curSong += 1
    if(curSong >= len(listofFiles)):
        curSong = 0
    elif(curSong < 0):
        curSong = len(listofFiles)
    return listofFiles[curSong]
def getPrevSong():
    global curSong
    global listofFiles
    curSong -= 1
    if(curSong >= len(listofFiles)):
        curSong = 0
    elif(curSong < 0):
        curSong = len(listofFiles)-1
    return listofFiles[curSong]


@app.route('/')
def index():
  return render_template('MainControl.html')


def addSongToPlaylist(indexOfSong, indexOfPlaylist):
    print("todo")

isPlaying = False
isPaused = True


getAllFiles()

print(listofFiles)

#Play Button
@app.route('/play/')
def play():
    global isPaused
    global isPlaying
    global songList
    if(isPlaying == False):
        randomize()
        mixer.music.load(getNextSong())
        mixer.music.play()
        isPlaying = True
    elif(isPaused == True):
        mixer.music.pause()
        isPaused = False
    else:
        mixer.music.unpause()
        isPaused = True
    return render_template('MainControl.html',data=True) 

@app.route('/stop/')
def stop():
    global isPlaying
    mixer.music.stop()
    isPlaying = False
    return render_template('MainControl.html',data=True) 

@app.route('/prev/')
def prev():
    mixer.music.load(getPrevSong())
    mixer.music.play()
    isPlaying = True
    isPaused = False
    return render_template('MainControl.html')

#Next Button
@app.route('/next/')
def skip():
    mixer.music.load(getNextSong())
    mixer.music.play()
    isPlaying = True
    isPaused = False
    return render_template('MainControl.html')

if __name__ == '__main__':
  app.run(debug=True,host="0.0.0.0")