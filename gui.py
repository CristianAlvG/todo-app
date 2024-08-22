import functions
import FreeSimpleGUI as sg

#Widgets
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button("Add")

#Build
window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]], font=('Helvetica', 15))

#Values and Events
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo']
            todos.append(new_todo + "\n")
            functions.write_todos(todos)
        case sg.WINDOW_CLOSED:
            break

window.close()
