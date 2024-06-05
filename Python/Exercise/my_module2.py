# import my_module

# results = my_module.add(1,2)

# print(results)

# from my_module import subtract as s

# result = s(10,6)

# print(result)


# from my_module import add as a

# result = a(4,8)

# print(result)



# from my_module import *

# import sys 
# print(sys.path)

# import datetime

# leo = datetime.datetime.now()



# formated_date = leo.strftime("%Y-%m-%d")
# day = leo.strftime("%A")
# formated_time = leo.strftime()




# print(leo)

import datetime

# Get the current date and time
now = datetime.datetime.now()

# Format the date and time
formatted_date = now.strftime("%Y-%m-%d")
day_of_week = now.strftime("%A")  # Day of the week
formatted_time = now.strftime("%H:%M:%S")

# Print the formatted date, day, and time
print(f"Date: {formatted_date}, Day: {day_of_week}, Time: {formatted_time}")