import pyttsx3
import speech_recognition as sr
from speech import *
import time
from datetime import datetime
import pywhatkit as kit
import wikipedia
import pyautogui
import time
pyautogui.FAILSAFE = False

def search_wiki(query):
    results = wikipedia.summary(query, sentences=2)
    return results

def play_on_youtube(video):
    kit.playonyt(video)

def search_on_google(query):
    kit.search(query)    

def show_desktop():
    x=(1919,1079)
    pyautogui.moveTo(x[0],x[1])
    pyautogui.click()

def close_tab():
    show_desktop()
    x=(836,1061)
    pyautogui.moveTo(x[0],x[1])
    pyautogui.click()
    pyautogui.hotkey('ctrl','w')


