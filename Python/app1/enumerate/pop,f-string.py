todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()  ## To remove extra spaces, "add "
    match user_action:
        case 'add':
            user_input = input("Enter a todos: ")
            todos.append(user_input)
        case 'show':
            for index, item in enumerate(todos):
                print(f"{index + 1}.{item}")
        case 'edit':
            number = int(input("Number of todo to edit: "))
            number = number - 1
            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Number of todo to complete: "))
            todos.pop(number - 1)
        case 'exit':
            break

print("Bye!!!")
