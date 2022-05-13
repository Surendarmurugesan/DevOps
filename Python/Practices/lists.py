# Lists are one of the most powerful tools in python. 
# They are just like the arrays declared in other languages. But the most powerful thing is that list need not be always homogeneous. 
# A single list can contain strings, integers, as well as objects. 
# Lists can also be used for implementing stacks and queues. 
# Lists are mutable, i.e., they can be altered once declared.


# Declaring a list
L = [1, "a" , "string" , 1+2]
print(L)
# append = will add the value at last
L.append(6)
print(L)
# pop = will delete the last value.(By default)- If mention index, it will remove that one.
L.pop()
L.pop(2)
print(L)
print (L[2])