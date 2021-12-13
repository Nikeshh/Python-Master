# Simple multiplication - Number of hours in a week
print(24*7)

# Variables
day_hours = 24
week_days = 7
hours = day_hours * week_days
print("Hours in a week is " + str(hours))

# Type of variable
x = 10
print(type(x))

# Compound datatype - List
student_grades = [9.8, 10.1]
print(student_grades[0])

# Ranges
student_grades_using_range = list(range(1, 10)) 
print(student_grades_using_range[8])
list(range(1, 10, 2)) #2 is the difference between consecutive numbers

rainfall = [10.0, 10, "34", [10, 20]] #A list inside list is also possible

# dir function -> returns functions and methods of a specified object
# dir(str)
# dir(float)
# dir(int)
# dir(list)

# help function -> used to find the usage of a method
# help(str.upper)

# How to get all the built in methods?
# dir(__builtins__)

# Find the sum, length and mean for student grades
student_sum = sum(student_grades)
student_len = len(student_grades)
student_mean = student_sum / student_len
print(student_mean)

# Find the count of 10.0 in a list
student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
student_len = student_grades.count(10.0)
print(student_len)

# Dictionary
student_dict = {"Marry": 9.0, "Ricky": 10.0}
# To get the values from the dictionary
student_dict_values = student_dict.values()
student_dict_sum = sum(student_dict_values)

# Note: List, Dictionary and Tuples are different data types

# Tuples -> Tuples are immutable but lists are mutable
# Tuples are faster than lists
student_tuple = (1, 2, 3)
student_list = [1, 2, 3]
student_dict = {"Student1": 1, "Student2": 2}
student_list.append(4) # Not possible in the case of tuples
student_list.remove(4) # Not possible in the case of tuples

# More operations with list
# dir(list)
sample_list = [1.1, 2.2, 3.3]
sample_list.index(2.2) # sample_list.index(value, start_index, stop_index)
sample_list.__getitem__(0)
sample_list[0]
sample_list.clear()

# List Slices -> lower limit is inclusive but upper limit is exclusive
sample_list[1:3]