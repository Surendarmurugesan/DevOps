# The following formula calculates the free-fall time of an object.
#
# h is the free-fall distance and g is the gravity. On Earth, gravity is 9.80665 m/s2.
#
# Given the above information, we have created a program that calculates the free-fall time given the
# free-fall distance h and the gravity g which will be a default parameter with a value of 9.80665:

def calculate_time(h, g=9.80665):
    t = (2 * h / g) ** 0.5
    return t

time = calculate_time(100)
print(time)