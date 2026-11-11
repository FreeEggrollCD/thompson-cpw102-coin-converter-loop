# Zeller's Congruence - Calculate the day of the week for a given date

# Get date input from user
year = int(input('Enter year (e.g., 2015): '))
month = int(input('Enter month (1-12): '))
day = int(input('Enter day of the month (1-31): '))

# Adjust for January and February by treating them
#   as months 13 and 14 of the previous year
if month == 1 or month == 2:
    month += 12
    year -= 1
    
# Split year into century (j) and year of the century (k)
year_of_century = year % 100   # Last two digits of the year
century = year // 100          # First two digits of the year

# Apply Zeller’s Congruence formula
weekday_number = (day + (26 * (month + 1)) // 10 + year_of_century + 
                 (year_of_century // 4) + (century // 4) + (5 * century)) % 7

# Determine the weekday name using if/elif statements
if weekday_number == 0:
    weekday_name = 'Saturday'
elif weekday_number == 1:
    weekday_name = 'Sunday'
elif weekday_number == 2:
    weekday_name = 'Monday'
elif weekday_number == 3:
    weekday_name = 'Tuesday'
elif weekday_number == 4:
    weekday_name = 'Wednesday'
elif weekday_number == 5:
    weekday_name = 'Thursday'
else:
    weekday_name = 'Friday'

# Display the result
print('Day of the week is', weekday_name)
