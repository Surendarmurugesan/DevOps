import random

lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

rand = random.randint(lower_bound, upper_bound)
print(rand)