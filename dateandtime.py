from datetime import date
from datetime import time
from datetime import datetime

today = date.today()
print("Today is ", today)

print("Date components: ", today.day, today.month, today.year)

print()

# The weekday numbers go from 0-6, Moday-Sunday.
print("Today's weekday number is", today.weekday())
days = ["Monday", "Tuesday", "Wednesday", "Thurday", "Friday", "Saturday", "Sunday"]
print("Which is a", days[today.weekday()])

print()
# Using the datetime module
today = datetime.now()
print("The current date and time is", today)

t = datetime.time(datetime.now())
print("The current time is",t)