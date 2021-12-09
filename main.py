from flask import Flask, render_template
import pygame
from pygame import mixer
import os
from tkinter import *


app = Flask(__name__)

mixer.init()
mixer.music.load("Songs/blowing_raspberries.mp3")

@app.route('/')
def index():
  return render_template('MainControl.html')


def addSongToPlaylist(indexOfSong, indexOfPlaylist):
    print("todo")

#Play Button
@app.route('/play/')
def play():
    mixer.music.play()
    return render_template('MainControl.html',data=True) 

@app.route('/stop/')
def stop():
    mixer.music.play()
    return render_template('MainControl.html',data=True) 

@app.route('/prev/')
def prev():
    mixer.music.play()
    return render_template('MainControl.html',data=True) 

#Pause Button
@app.route('/pause/')
def pause(varName=None):
    mixer.music.pause()
    return render_template('MainControl.html')

#Next Button
@app.route('/next/')
def skip():
    return render_template('MainControl.html')

#Randomize Playlist
def randomizePlaylist():
    print("todo")

#Start A Playlist
def startPlaylist():
    print("todo")

if __name__ == '__main__':
  app.run(debug=True)