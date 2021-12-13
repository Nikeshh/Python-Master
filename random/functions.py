# Creating functions
def mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return the_mean

print(mean([1, 4, 5]))

# Conditionals
def mean_with_condition(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    elif type(value) == list:
        the_mean = sum(value) / len(value)
    else:
        the_mean = None
    return the_mean

print(mean_with_condition([1, 4, 5]))
print(mean_with_condition({"Student1":1, "Student2": 4}))

# isinstance() works similar to type()
# isinstance(value, int)
# type(value) == int
