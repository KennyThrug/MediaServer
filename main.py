from flask import Flask, render_template
import pygame, mutagen.mp3
from pygame import mixer
import os
from tkinter import *
import random
import threading
import wave


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
    listofFiles = []
    for root, dirs, files in os.walk(path):
        for file in files:
            listofFiles.append(os.path.join(root,file))
    print(listofFiles)
def getNextSong():
    global curSong
    global listofFiles
    curSong += 1
    if(curSong >= len(listofFiles)):
        curSong = 0
    elif(curSong < 0):
        curSong = len(listofFiles)

    #mp3 = mutagen.mp3.MP3(listofFiles[curSong])
    #pygame.mixer.init(frequency=mp3.info.sample_rate)

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
def hasSong():
    global listofFiles
    global curSong
    return not (len(listofFiles) == curSong)


@app.route('/')
def index():
  return render_template('MainControl.html')


def addSongToPlaylist(indexOfSong, indexOfPlaylist):
    print("todo")

isPlaying = False
isPaused = True


getAllFiles()

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
        isPaused = False
    elif(isPaused == False):
        mixer.music.pause()
        isPaused = True
    else:
        mixer.music.unpause()
        isPaused = False
    return render_template('MainControl.html') 

@app.route('/stop/')
def stop():
    global isPlaying
    mixer.music.stop()
    isPlaying = False
    return render_template('MainControl.html') 

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

@app.route('/shuffle/')
def shuffle():
    getAllFiles()
    randomize()
    return render_template('MainControl.html')

def getShouldPause():
    global isPlaying
    global isPaused
    global mixer
    if(isPlaying and not isPaused):
        if(not mixer.music.get_busy()):
            return True
    return False

def runApp():
    app.run(debug=True,host="0.0.0.0")
def checkForNextSong():
    while(True):
        if(getShouldPause()):
            skip()

if __name__ == '__main__':
    t1 = threading.Thread(target=checkForNextSong)
    t1.start()
    runApp()
    t1.join()