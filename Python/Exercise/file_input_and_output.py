# # Open a file in read mode
# file = open('functions.py', 'r')

# # Read the contents of the file
# content = file.read()

# # Print the contents
# print(content)

# # Close the file
# file.close()


# READ
# -----

# with open("example.txt","r") as file:
#     content = file.read()
#     print(content)

#     file.close()

    # WRITE
    # ------

# with open("example.txt","w") as f:
#     f.write("*ESSAY HAS BEEN WRITTEN BY BENZ")
    

# with open("example.txt","a") as file:
#     content = file.write("  , I have added some \"messages\"\n")
#     print(content)


# try:
   
#     with open("example.txt","x") as file:
#         content = file.write("  , I have added some \"messages\"\n")
#         print(content)

# except FileExistsError :
#     print("The file already exists")

   
# import os
# os.rename("example.txt" , "basic.txt")


import os 
os.shutdown("vscode")