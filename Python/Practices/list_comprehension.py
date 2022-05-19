# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

temp = [221, 300, 480, 350]
new_temps = [val / 10 for val in temp]
print(new_temps)

# List comprehension with IF condition.
temp = [221, -90, 300, 480, 350, -1000]
new_temps = [val / 10 for val in temp if val > 0]
print(new_temps)

# List comprehension with IF-ELSE condition.
temp = [221, -90, 300, 480, 350, -1000]
new_temps = [val / 10 if val > 0 else 0 for val in temp]
print(new_temps)