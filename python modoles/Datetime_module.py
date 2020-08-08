import datetime

# mydate = datetime.date(2020,1,1)        #creating our own date
# print(mydate)

today_date = datetime.date.today()        #displaying the current date


# print(today_date)

# print(today_date.year)          # printing the present year

# print(today_date.month)             #displaying the current month

# print(today_date.day)               #displaying the current date

# print(today_date.weekday())             #displaying the day of the week in an enumeration format (monday = 0)

# print(today_date.isoweekday())              #here monday = 1

# time_delta = datetime.timedelta(days=34)             #manipulation of time (addition or substraction of days)
# print(today_date + time_delta)

# new_year = datetime.date(2020,1,1)                      
# print("No of days passed",(today_date-new_year).days)           #number of days passed in a year

# my_time = datetime.time(7,55,52,60)         #creating our own time

# print(my_time)

# print(my_time.hour)             #printing the hour of my_time

# print(my_time.minute)

# print(my_time.second)

# print(my_time.microsecond)

# my_day = datetime.datetime(2020,1,1,7,45,56,60)         #printing the date and the time together
# print(my_day)

# print(my_day.now())          #calling the current date and time (not initialised)  


