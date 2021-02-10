import time
import tkinter as tk
from tkinter import messagebox,simpledialog

# ask user for a reminder
# print ("What should i remind you off?")
# import tkinter module to root
ROOT = tk.Tk()
ROOT.withdraw()
message = simpledialog.askstring(title= "Reminder", prompt="What should i remind you off?")

# take user's input
# message = str(input())

# ask user "in how many minutes"
# print ("In how many minutes?")

ROOT.withdraw()
local = simpledialog.askinteger(title= "Reminder", prompt="In how many minutes?")

# convert the number of minutes to seconds
# local_time = float(input())

# converting minutes to seconds
local = local * 60

# number of minutes for which the program will sleep (from time module takes method sleep with variable local name)
time.sleep(local)

# after
messagebox.showinfo("Notification",message)
