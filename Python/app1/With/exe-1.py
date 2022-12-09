
# The user runs the program. The program asks the user to enter "head" or "tail".  The user flips a coin on their
# desk, table, floor, etc., and then enters "head" or "tail". The user does the same over and over again.

while True:
    with open("sides.txt", 'r') as file:
        sides = file.readlines()

    user_input = input("Throw the coin and enter the head or tail here: ? ") + "\n"

    sides.append(user_input)

    with open("sides.txt", 'w') as wr:
        wr.writelines(sides)

    nr_heads = sides.count("head\n")
    percent = nr_heads / len(sides) * 100
    print(f"Heads: {percent}%")