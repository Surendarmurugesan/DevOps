# names = ["john smith", "jay santi", "eva kuki"]
# Extend the code above so the code capitalizes all the names and the surnames of the list and then prints the new list.
# The output of your code should be as below:
# ['John Smith', 'Jay Santi', 'Eva Kuki']


names = ["john smith", "jay santi", "eva kuki"]
names_list = [name.title() for name in names]
print(names_list)

# example  3:
# usernames = ["john 1990", "alberta1970", "magnola2000"]
# Extend the code above so the code prints out a list containing the number of characters for each username.
# The output of your code should be as below:
# [9, 11, 11]

usernames = ["john 1990", "alberta1970", "magnola2000"]
user_list = [len(name) for name in usernames]
print(user_list)