#from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%H")
print(f"It is {now}")

while True:
    user_action = input("Type add,show,edit,complete or exit ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + "\n"

        # It opens and closes the files after ending the process.
        todoList = functions.get_todos()
        todoList.append(todo.title())
        functions.write_todos(todoList)

    elif user_action.startswith('show'):
        todoList = functions.get_todos()

        #Remove \n and append in list
        # new_todos = [item.strip('\n') for item in todoList]

        #Show the list
        for index, item in enumerate(todoList):
            item = item.strip('\n')
            row = f"{index + 1}.{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todoList = functions.get_todos()

            new_todo = input("Enter a new todo ").strip()
            todoList[number] = new_todo.title() + '\n'

            functions.write_todos(todoList)

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todoList = functions.get_todos()

            index = number - 1
            numTask = index
            todoList.pop(numTask)

            functions.write_todos(todoList)

            message = f"Todo {number} was removed from the list"

            print(message)
        except IndexError:
            print("There is no item with that number")
            continue
    elif 'exit' in user_action:
        break

    else:
        print("Command isnt valid.")


print("Bye!")


#Important code before
#'add' in user_action or 'new' in user_action
