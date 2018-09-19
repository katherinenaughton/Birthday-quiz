"""
birthday.py
Author: Katie Naughton
Credit: I worked alone. 
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""

name = input("Hello, what is your name? ")
month = input("Hi, " + name + " what month were you born in? ")
year = int(input("And what year were you born in, " + name + "? "))
day= input("And the day? ")

#Halloween and Birthday
if month == "October" and day == "31": 
    print("You were born on Halloween!")
if month == "September" and day == "17": 
    print("Happy Birthday!")
 
#Baby Boomers
if 1946<=year<=1964 and month in [ "September", "October", "November"]:
    print("You are a fall Baby Boomer!")
if 1946<=year<=1964 and month in [ "December", "January", "February"]:
    print("You are a winter Baby Boomer!")
if 1946<=year<=1964 and month in [ "March", "April", "May"]:
    print("You are a spring Baby Boomer!")
if 1946<=year<=1964 and month in [ "June", "July", "August"]:
    print("You are a summer Baby Boomer!")
    
#Generation X
if 1965<=year<=1974 and month in [ "September", "October", "November"]:
    print("You are a fall baby of Generation X!")
if 1965<=year<=1974 and month in [ "December", "January", "February"]:
    print("You are a winter baby of Generation X!")
if 1965<=year<=1974 and month in [ "March", "April", "May"]:
    print("You are a spring baby of Generation X !")
if 1965<=year<=1974 and month in [ "June", "July", "August"]:
    print("You are a summer baby of Generation X!")
    
#Xennials
if 1975<=year<=1979 and month in [ "September", "October", "November"]:
    print("You are a fall Xennial!")
if 1975<=year<=1979 and month in [ "December", "January", "February"]:
    print("You are a winter Xennial!")
if 1975<=year<=1979 and month in [ "March", "April", "May"]:
    print("You are a spring Xennial !")
if 1975<=year<=1979 and month in [ "June", "July", "August"]:
    print("You are a summer Xennial!")
    
#Millennials
if 1980<=year<=1994 and month in [ "September", "October", "November"]:
    print("You are a fall Millennial!")
if 1980<=year<=1994 and month in [ "December", "January", "February"]:
    print("You are a winter Millennial!")
if 1980<=year<=1994 and month in [ "March", "April", "May"]:
    print("You are a spring Millennial !")
if 1980<=year<=1994 and month in [ "June", "July", "August"]:
    print("You are a summer Millennial!")

#Generation Z
if 1995<=year<=2012 and month in [ "September", "October", "November"]:
    print("You are a fall baby of Generation Z!")
if 1995<=year<=2012 and month in [ "December", "January", "February"]:
    print("You are a winter baby of Generation Z!")
if 1995<=year<=2012 and month in [ "March", "April", "May"]:
    print("You are a spring baby of Generation Z!")
if 1995<=year<=2012 and month in [ "June", "July", "August"]:
    print("You are a summer baby of Generation Z!")

#Generation Alpha
if 2012<=year<=2025 and month in [ "September", "October", "November"]:
    print("You are a fall baby of Generation Alpha!")
if 2012<=year<=2025 and month in [ "December", "January", "February"]:
    print("You are a winter baby of Generation Alpha!")
if 2012<=year<=2025 and month in [ "March", "April", "May"]:
    print("You are a spring baby of Generation Alpha!")
if 2012<=year<=2025 and month in [ "June", "July", "August"]:
    print("You are a summer baby of Generation Alpha!")




