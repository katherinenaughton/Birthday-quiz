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

from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day
month = month_name[todaymonth]

name = input("Hello, what is your name? ")
month = input("Hi " + name + ", what was the name of the month you were born in? ")
year = int(input("And what year were born in, " + name + "? "))
day= int(input("And the day? "))

#Halloween and Birthday
if month == "October" and day == 31: 
    print("You were born on Halloween!")
elif month == month and day == todaydate: 
    print("Happy birthday!")
    

#Stone Age 
elif 0<=year<=1979 and month in [ "September", "October", "November"]:
    print(name + ", you are a fall baby of the Stone Age.")
elif 0<=year<=1979 and month in [ "December", "January", "February"]:
    print(name+ ", you are a winter baby of the Stone Age.")
elif 0<=year<=1979 and month in [ "March", "April", "May"]:
    print(name+ ", you are a spring baby of the Stone Age.")
elif 0<=year<=1979 and month in [ "June", "July", "August"]:
    print(name+ ", you are a summer baby of the Stone Age.")
    
#eighties
elif 1980<=year<=1989 and month in [ "September", "October", "November"]:
    print(name+ ", you are a fall baby of the eighties.")
elif 1980<=year<=1989 and month in [ "December", "January", "February"]:
    print(name+ ", you are a winter baby of the eighties.")
elif 1980<=year<=1989 and month in [ "March", "April", "May"]:
    print(name+ ", you are a spring baby of the eighties.")
elif 1980<=year<=1989 and month in [ "June", "July", "August"]:
    print(name+ ", you are a summer baby of the eighties.")
    
#nineties
elif 1990<=year<=1999 and month in [ "September", "October", "November"]:
    print(name+ ", you are a fall baby of the nineties.")
elif 1990<=year<=1999 and month in [ "December", "January", "February"]:
    print(name+ ", you are a winter baby of the nineties.")
elif 1990<=year<=1999 and month in [ "March", "April", "May"]:
    print(name+ ", you are a spring baby of the nineties.")
elif 1990<=year<=1999 and month in [ "June", "July", "August"]:
    print(name+ ", you are a summer baby of the nineties.")

#two thousands
elif 2000<=year<=2018 and month in [ "September", "October", "November"]:
    print(name+ ", you are a fall baby of the two thousands.")
elif 2000<=year<=2018 and month in [ "December", "January", "February"]:
    print(name+ ", you are a winter baby of the two thousands.")
elif 2000<=year<=2018 and month in [ "March", "April", "May"]:
    print(name+ ", you are a spring baby of the two thousands.")
elif 2000<=year<=2018 and month in [ "June", "July", "August"]:
    print(name+ ", you are a summer baby of the two thousands.")






