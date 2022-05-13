# String is a sequence of characters. 
# It can be declared in python by using double-quotes. 
# Strings are immutable, i.e., they cannot be changed.
# Can't delete a character of string. ex: del String_value[2]
# Delete the entire string. ex: del String_value


# Assigning string to a variable
a = "This is a 2+4 string"
print (a)

# Python Program to access characters of String
String1 = "GeeksForGeeks "
print("Initial String: ")
print(String1)
  
# Printing First character
print("\nFirst character of String is: ")
print(String1[0])
  
# Printing Last character
print("\nLast character of String is: ")
print(String1[-1])

# Python Program to demonstrate String slicing
# Creating a String
String1 = "GeeksForGeeks"
print("Initial String: ") 
print(String1)
  
# Printing 3rd to 12th character
print("\nSlicing characters from 3-12: ")
print(String1[3:12])
  
# Printing characters between 
# 3rd and 2nd last character
print("\nSlicing characters between " + "3rd and 2nd last character: ")
print(String1[3:-2])