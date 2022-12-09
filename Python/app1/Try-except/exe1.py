total = int(input("Enter the total value: "))

try:
    val = int(input("Enter the value: "))
    avg = val / total * 100
    print(f" That is {avg}%")
except ValueError:
    print("You need to enter a number. Run the program again.")
except ZeroDivisionError:
    print("Your total value cannot be zero.")
