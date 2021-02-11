import time
import csv
import tkinter as tk
from csv import writer
from tkinter import messagebox,simpledialog

# import tkinter module to root window
ROOT = tk.Tk()
# Withdraw this widget from the screen such that it is unmapped and forgotten by the window manager
ROOT.withdraw()
# take string input from user in message with pop-up box to ask what to remind
message = simpledialog.askstring(title= "Reminder", prompt="What should i remind you off?")

# take integer input from user for after how many minutes
local = simpledialog.askinteger(title= "Reminder", prompt="In how many minutes?")

# convert the number of minutes to seconds
# converting minutes to seconds
local = local * 60

#open text file in append and write mode
with open('reminder.txt', 'a+') as file_object:
    file_object.seek(0) # point to the beginning of the file
    data = file_object.read(100) # read for more objects in the file
    if len(data) > 0 :
        file_object.write("\n") # in next line
        file_object.write(message + "," + str(local)) # concat into a text file with ","

ROOT.withdraw()

# number of minutes for which the program will sleep (from time module takes method sleep with variable local name)
#time.sleep(local)

# after
#messagebox.showinfo("Notification",message)
