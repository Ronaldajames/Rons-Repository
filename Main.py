# tkinter python - Use this for GUI Construction when ready

#Module = Consider a module to be the same as a code library. A file containing a set of functions you want to include in your application.

# import OS module to clear console before receiving new Data
import os

#import datetime module, and date module to use for calculating age 
from datetime import date

# Clears Console on every iteration / Start 
if os.name == ("nt") :
    _ = os.system("cls")

# Creates dictionary Conatinig Birthday Dates 
Birthdays = {}

#Creats a dicionary to contain age of Person
age = {}

# Gathers input for the Number of Birthday Entries to be entered
birthday_entries = int(input(" Enter Amount of Birthday Entries : "))

# Loops through the number of entries entered. Gathers name and birthday from user input
for i in range(birthday_entries):
    name = input("Enter name : ")
    Date = input ("Enter Birthday : ")
    Birthdays[name] = Date

    
# function to Calculate age 
def age_conversion(Birthdays):   
    today = date.today()
    age = today.year - Birthdays.year

    if (today.month, today.day) < (Birthdays.Month, Birthdays.day):
        age -= 1

print(" Dictionary Contents:    ", Birthdays)
print(" Your are ", age, "Years old !")
