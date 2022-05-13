# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)

# Adding elements one at a time
Dict[0] = 'Hey'
Dict[1] = 'Suren'
Dict[2] = 8
print("\nDictionary after adding 3 elements: ")
print(Dict)

# Adding set of values to a single Key
Dict['Value_set'] = 4,6,8
print("\nDictionary after adding 3 elements: ")
print(Dict)

# Updating existing Key's Value
Dict[2] = 'Welcome'
print("\nUpdated key value: ")
print(Dict)

# Adding Nested Key value to Dictionary
Dict[5] = {'Nested' :{'1' : 'Life', '2' : 'DevOps'}}
print("\nAdding a Nested Key: ")
print(Dict)


#            Accessing elements from a Dictionary
# In order to access the items of a dictionary refer to its key name. Key can be used inside square brackets.

# Python program to demonstrate accessing a element from a Dictionary
 
# Creating a Dictionary
Dict = {1: 'DevOps', 'name': 'For', 3: 'DevOps'}
 
# accessing a element using key
print("Accessing a element using key:")
print(Dict['name'])
 
# accessing a element using key
print("Accessing a element using key:")
print(Dict[1])

# There is also a method called get() that will also help in accessing the element from a dictionary.
# Creating a Dictionary
Dict = {1: 'DevOps', 'name': 'For', 3: 'DevOps'}
 
# accessing a element using get()
# method
print("Accessing a element using get:")
print(Dict.get(3))


#          Accessing an element of a nested dictionary
#   In order to access the value of any key in the nested dictionary, use indexing [] syntax.
# Creating a Dictionary
Dict = {'Dict1': {1: 'DevOps'},
        'Dict2': {'Name': 'For'}}
 
# Accessing element using key
print(Dict['Dict1'])
print(Dict['Dict1'][1])
print(Dict['Dict2']['Name'])

#          Removing Elements from Dictionary
# Initial Dictionary
Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'DevOps',
        'A' : {1 : 'DevOps', 2 : 'For', 3 : 'DevOps'},
        'B' : {1 : 'DevOps', 2 : 'Life'}}
print("Initial Dictionary: ")
print(Dict)
 
# Deleting a Key value
del Dict[6]
print("\nDeleting a specific key: ")
print(Dict)
 
# Deleting a Key from
# Nested Dictionary
del Dict['A'][2]
print("\nDeleting a key from Nested Dictionary: ")
print(Dict)

# Using pop() method
# Pop() method is used to return and delete the value of the key specified.
# Creating a Dictionary
Dict = {1: 'DevOps', 2: 5, 'name': 'For', 3: 'DevOps'}

# Deleting a key using pop() method
pop_ele = Dict.pop(1)
print('\nDictionary after deletion: ' + str(Dict))
print('Value associated to poped key is: ' + str(pop_ele))

# popitem() method
# The popitem() returns and removes an arbitrary element (key, value) pair from the dictionary.
# Creating Dictionary
Dict = {2: 5, 1: 'DevOps', 'name': 'For', 3: 'DevOps'}

# Deleting an arbitrary key
# using popitem() function
pop_ele = Dict.popitem()
print("\nDictionary after deletion: " + str(Dict))
print("The arbitrary pair returned is: " + str(pop_ele))

# Using clear() method
# All the items from a dictionary can be deleted at once by using clear() method.

# Creating a Dictionary
Dict = {1: 'DevOps', 'name': 'For', 3: 'DevOps'}
 
# Deleting entire Dictionary
Dict.clear()
print("\nDeleting Entire Dictionary: ")
print(Dict)