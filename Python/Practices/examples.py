## Example 1
name = "Sally"# employee name 
data = "#123" 
print (name+data)

## Example 2
countries = ["USA", "Canada", "India"]
countries[0], countries[1] = countries[1], countries[0]
print(countries)

## Example 3
def get_even_func(numbers):
    even_numbers = [num for num in numbers if not num % 2]
    print(even_numbers)
    return even_numbers
get_even_func([1, 2, 3, 4, 5, 6])

## Example 4
i = 1
x = 3
sum = 0
while ( i <= x ):
 sum += i
 i += 1
print(sum)

