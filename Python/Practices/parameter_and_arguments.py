def area(a,b=3):
    return a - b

print(area(a=4, b=2))


def converter(feet, coefficient = 3.2808):
    meters = feet / coefficient
    return meters
 
print(converter(10))

def volume(a, b, c):
    return a * b * c
 
print(volume(1, b=2, c=10))


# Functions with an Arbitrary Number of Non-keyword Arguments
# Sometimes, we passing n number of arguments, so use "*args"
def mean (*args):
    return sum(args) / len(args)

print(mean(1, 2, 3))

def find_max(*args):
    return max(args)
print(find_max(3, 99, 1001, 2, 8))


# Functions with an Arbitrary Number of Keyword Arguments
# Sometimes, we passing n number of arguments with keyword, so use "**kwargs". Output will provide as "Dictionary".
def mean(**kwargs):
    return kwargs

print(mean(a=1, b=2, c=3))

# Example:
def find_sum(**kwargs):
    return sum(kwargs.values())
    
print(find_sum(a=4, b=2, c=1, d=2))

def find_winner(**kwargs):
    return max(kwargs, key = kwargs.get)
 
print(find_winner(Andy = 17, Marry = 19, Sim = 45, Kae = 34))