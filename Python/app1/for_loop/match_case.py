todos = []

while True:
    user_action = input("Type add, show or exit: ")
    user_action = user_action.strip()  ## To remove extra spaces, "add "
    match user_action:
        case 'add':
            user_input = input("Enter a todos: ")
            todos.append(user_input)
        case 'show':
            for i in todos:
                print(i)
        case 'exit':
            break

print("Bye!!!")
