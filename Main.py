# tkinter python - Use this for GUI Construction when ready

#Module = Consider a module to be the same as a code library. A file containing a set of functions you want to include in your application.

# import OS module to clear console before receiving new Data
import os

#import datetime module, and date module to use for calculating age 
from datetime import date
from datetime import datetime

# Clears Console on every iteration / Start 
if os.name == ("nt") :
    _ = os.system("cls")

# Creates dictionary Containing Birthday Dates 
Birthdays = {}

#Creats a dicionary to contain age of Person
age = {}

# Gathers input for the Number of Birthday Entries to be entered
birthday_entries = int(input(" Enter Amount of Birthday Entries : "))

# Loops through the number of entries entered. Gathers name and birthday from user input
for i in range(birthday_entries):
    name = input(" Enter name : ")
    date_input = (input(" Enter Birthday in Current Format YYYY/MM/DD: "))
    Birthdays[name] = date_input

# Checks to see if the user Input is fromatted correctly to be handled 
try: 
    date = datetime.strptime(date_input,"%Y/%m/%d")
    print (" You Entered : {date} ")
    print (" Birth Year : {date.year} ")
    print (" Birth Month : {date.Month} ")
    print (" Birth Day : {date.day} ")

except ValueError:
    print(" Incorrect date formate. Please use YYYY/MM/DD ")

# function to Calculate age 
def age_conversion(Birthdays):   
    today = date.today()
    age = today.year - Birthdays.year

    if (today.month, today.day) < (Birthdays.Month, Birthdays.day):
        age -= 1
1
#age = age_conversion(Birthdays)

print(" Dictionary Contents:    ", Birthdays)
print(" Your are ", age, "Years old !")
