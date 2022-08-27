from win32api import *
from win32gui import *
import win32con
import sys, os
import struct
import time
from win10toast import ToastNotifier
from Module4 import *
import ctypes
import time

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

#Mbox('Your title', 'Your text', 1)

