import time

# ask user for a reminder
print ("What should i remind you off?")

# take user's input
message = str(input())

# ask user "in how many minutes"
print ("In how many minutes?")

# convert the number of minutes to seconds
local_time = float(input())

# converting minutes to seconds
local_time = local_time * 60

# number of minutes for which the program will sleep (from time module takes method sleep with variable local name)
time.sleep(local_time)

# after
print(message)