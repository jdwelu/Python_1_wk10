#!/usr/bin/env python3

# Importing the time classes I think I'll need.
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


# Defining a function to get and parse the date entered.
# Taking a more conventional date, because order will not matter.
def get_date():
    try:
        got_date_str = input("Please enter your date (MM/DD/YYYY): ")
        got_date = datetime.strptime(got_date_str, "%m/%d/%Y")
        # print(got_date)
        return got_date
    except Exception as e:
        print()
        print(" *** ERROR HAS OCCURRED *** ")
        print("Error Type:", type(e))
        print("Error:", e)
        print("Error Arguments:", e.args)
        got_date = datetime(1941, 12, 6)
        return got_date

# Program prompt.
print()
print("============================================")
print("Welcome to the Pearl Harbor Date Calculator!")
print("============================================")
print()
print("Enter any date after Pearl Harbor,")
print("and this program will tell you how")
print("many days it has been...")
print()
print("Should you enter an invalid date,")
print("before Pearl Harbor, you will be")
print("prompted again for a usable date.")
print()
print()


# Start of the date loop.
condition = True

while condition == True:

    pearl_harbor = datetime(1941, 12, 7)
    got_date = 0

    entered_date = get_date() # Gets the date from the user.

    # print(entered_date)   #Gives full date including timer.

    adjusted_date = entered_date - pearl_harbor # Subtracts Pearl Harbor.

    # print(adjusted_date)   #Gives Days plus timer again.
       
    days = adjusted_date.days #Only grabs the number of days.
    
    if pearl_harbor < entered_date:
        print()
        print()
        print("----------------------------------------------")
        print("Days passed since Pearl Harbor =", days, "days")
        print("----------------------------------------------")
        print()
        print()
        condition = False

    elif pearl_harbor >= entered_date:
        print()
        print()
        print("***Invalid date entry please try again.***")
        print()
        print()
        condition = True

# I considered having this, but since I used error handling to just feed
# a date, you will never end up outside of the two 'if' statements.
##    else:
##        print()
##        print("*** Oops, it appears an error occurred.***")
##        print("------------------------------------------")
##        print("+++++++++++Please try again!!!++++++++++++")
##        print()
##        condition = True
