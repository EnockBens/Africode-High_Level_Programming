# import sys
# Max_Recursion = sys.getrecursionlimit()
# print(Max_Recursion)

# def Hello_Function():
#     print(Hello_Function)
#     Hello_Function()

# Hello_Function()


# def Count_Down(start):
#     """
#     count-down from a number 
#     """
#     print(start)
#     if start > 0:

#      Count_Down(start-1)

# Count_Down(3)



# def Count_Down(start):
#     """
#     count-down from a number 
#     """
#     print(start)
#     if start < 16:

#      Count_Down(start+1)

# Count_Down(1)

# def fact(n):
#     f = 1
#     for i in range(1,n+1):
#         f = f*i
#     return f
# result = fact(10)

# print(result)



def factorial(n):
    '''
    calculate the factorial of a number
    '''

    if n == 0:
       return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))