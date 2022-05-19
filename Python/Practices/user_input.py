user_input = input("Enter your name: ")
message = "Hello %s!!" % user_input
    # another method, f = refer the value
message = f"Hey {user_input}"
print(message, type(user_input))
# By default it storing as "string" value.


# Need to convert the user_input type.
Temp_value = float(input("Enter the temp: "))
print(Temp_value, type(Temp_value))

# String formatting with multiple variables::
name = input("Enter your Name: ")
surname = input("Enter your surname: ")
when = "today"
message = "Hello %s %s!" % (name, surname)
message2 = f"Hey {name} {surname}!!, What's up {when}"
print(message)
print(message2)


# There is also another way to format strings using the "{}".format(variable) form.
name = "John"
surname = "Smith"
message = "Your name is {}. Your surname is {}".format(name, surname)
print(message)
# Output: Your name is John. Your surname is Smith

#Using function
def foo(name):
    return f"Hi {name.capitalize()}"
print(foo("anderson"))