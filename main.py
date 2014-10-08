__author__ = 'Marcus'
import time
import twitter
from Counter import Counter
import keypresser
import os
import win32com

os.startfile('C://Program Files (x86)//BGB//bgb.exe')
def startup():
    shell = win32com.client.Dispatch('WScript.Shell')
    shell.AppActivate('bgb')
    time.sleep(0.2)
    shell.SendKeys("+{F10}")
    time.sleep(0.1)
    shell.SendKeys("r")
    time.sleep(0.2)
    shell.SendKeys('0')
    shell.SendKeys("{Enter}")

inputdict = {'Up' : 'd',
             'Down': 'f',
             'Left': 's',
             'Right': 'a',
             'A' : 'g',
             'B' : 'h',
             "Select" : 'j',
             "Start" : 'k'
             }
startup()
while True:
    process = twitter.TwitterProcess()
    process.cycle()
    letter_to_send = inputdict[process.button]
    keypresser.presskey(letter_to_send)
    time.sleep(1)