# exercise-06 What's the  Season?
import datetime
# Write the code that:
convert = {
  'Jan' : 1,
  'Feb' : 2,
  'Mar' : 3,
  'Apr' : 4,
  'May' : 5,
  'Jun' : 6,
  'Jul' : 7,
  'Aug' : 8,
  'Sep' : 9,
  'Oct' : 10,
  'Nov' : 11,
  'Dec' : 12
}

# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
month = input('Enter the month of the year (Jan - Dec):')
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
day = int(input('Enter the day of the month:'))
# 3. Calculate what season it is based upon this chart:
date = datetime.datetime(2000,convert[month],day)

if date < datetime.datetime(2000,3,19):
  season = 'Winter'
elif date < datetime.datetime(2000,6,20):
  season = 'Spring'
elif date < datetime.datetime(2000,9,21):
  season = 'Summer'
elif date < datetime.datetime(2000,12,20):
  season = 'Fall'
elif date < datetime.datetime(2001,1,1):
  season = 'Winter'

#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 
print(f'{month} {day} is in {season}')
# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.