# def my_function():

#     local_var ="Im local!"
#     print(local_var)

# my_function()
# print(local_var)






global_var = "I'm Global!"

def show_global():
    global global_var 
    global_var = "I'm Overriding You!!"
    print(global_var,"inside a function")

show_global()
print(global_var)