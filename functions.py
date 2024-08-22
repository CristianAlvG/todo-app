FILE_PATH = 'todoList.txt'

def get_todos(filepath = FILE_PATH):
    """" Read the text file and return the list of
    to do items """
    with open(filepath, 'r') as file:
        todoList = file.readlines()
    return todoList

def write_todos(todoList, filepath = FILE_PATH):
    """" Write the to-do items list in the text file """
    with open(filepath, 'w') as file:
        file.writelines(todoList)


if __name__ == "__main__":
    print(get_todos())