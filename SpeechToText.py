# -*- coding: utf-8 -*-
"""
Created on Sun May 24 23:36:34 2020

@author: hrith
"""


import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak: ")
    audio = r.listen(source)
    
    try:
        output = r.recognize_google(audio)
        print("You Said: {}".format(output.capitalize()))
        
    except:
        print("I Cannot Recognize What You Said....!!!!")
        print("Speak Again.....")