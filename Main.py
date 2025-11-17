# tkinter python - Use this for GUI Construction when ready

# import OS module to clear console before receiving new Data
import os

# Clears Console on every iteration / Start 
if os.name == ("nt") :
    _ = os.system("cls")

# Creates dictionary Conatinig Birthday Dates 
Birthdays = {}

# Number of Birthday Entries to be entered
birthday_entries = int(input(" Enter Amount of Birthday Entries : "))

for i in range(birthday_entries):
    name = input("Enter name : ")
    Date = input ("Enter Birthday : ")
    Birthdays[name] = Date

    print(" Dictionary Contents:    ", Birthdays)

