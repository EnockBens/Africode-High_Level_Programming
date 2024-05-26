# try:

#     results = 5 / 0

# except ZeroDivisionError:
#     print("Sorry, Input Cannot be Divided by 0")


# try: 

#     x =int(input("enter a number: "))

#     y = 1 / x

# except (ValueError,ZeroDivisionError):
#     print("number cannot be divided by 0")


# try: 
#     risky_operation()
          
# except Exception as e :
#     print(f"An Error Occured: {e}")

def Validate_Age(age):
    
    if age < 18 :
        raise ValueError("Age Must Be 18 or Older")
    else:
        return True
    
try:
    Validate_Age(19)

except ValueError as e:
      print(e)
else:
    print("meets the minimum age")

finally:
    print("I always run no matter what")

  