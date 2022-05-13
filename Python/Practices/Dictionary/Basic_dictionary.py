# Dictionary can be created by placing a sequence of elements within curly {} braces, separated by ‘comma’. Dictionary holds pairs of values, one being the Key and the other corresponding pair element being its Key:value. Values in a dictionary can be of any data type and can be duplicated, whereas keys can’t be repeated and must be immutable.

# Creating a Dictionary
# with Integer Keys
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print("Dictionary with the use of Integer Keys: ")
print(Dict)
keys = Dict.keys()
value = Dict.values()
print(keys)
print(value)


# Values in a dictionary can be of any data type and can be duplicated, whereas keys can’t be repeated and must be immutable.
    # Creating a Dictionary
    # with Mixed keys
Dict = {'Name': 'Geeks', 1: 'hey', 1: [1, 2, 3, 4], 2: 'hello'}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)


# Dictionary can also be created by the built-in function dict(). An empty dictionary can be created by just placing to curly braces{}. 
    # Creating an empty Dictionary
Sample = {}
print("\n\nEmpty Dictionary: ")
print(Sample)
 
    # Creating a Dictionary with dict() method
Sample = dict({1: 'Geeks', 2: 'For', 3:'Geeks'})
print("\nDictionary with the use of dict(): ")
print(Sample)
    # Creating a Dictionary
    # with each item as a Pair
Sample = dict([(1, 'Geeks'), (2, 'For')])
print("\nDictionary with each item as a pair: ")
print(Sample)


# Nested Dictionary
    # Creating a Nested Dictionary
    # as shown in the below image
print("\n\nNested Dictionary:")
Dict = {1: 'Geeks', 2: 'For', 3:{'A' : 'Welcome', 'B' : 'To', 'C' : 'Geeks'}}
print(Dict)


# Adding elements to a Dictionary