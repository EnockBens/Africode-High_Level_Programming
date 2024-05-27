students = {"bett" , "benz" , "nicholus" , "naomy" , "gladwel" }

# how to check whether a value is part of a set
# -------------------------------------------------
# print ("benz" in students)

# Convert set to list
# ***********************
# students_list = list(students)


# students_list[1] = "kipkorir"

# students = set(students_list)

# print(students )

students2 = {"Tyrene" , "benz" , "Brian" , "naomy" , "gladwel" }

# to check whether values in a set are common in a different set
# *******************************************************************
    #   INTERSECTION
#common value = (students.intersection(students2))


# to check the difference between two sets
# ****************************************
    # DIFFERENCE
# print(students.difference(students2))

# to print all the vallues
# ***************************
    # UNION
# print(students.union(students2))


male_students = {"bett" , "benz" , "nicholus"}

# if male_students.issubset(students):
#     print("male_students is a subset of students")
# else:
#     print("male_students is not a subset of students")

if students.issuperset(male_students):
    print("students is a subset of male_students")
else:
    print("students is not a subset of male_students")
