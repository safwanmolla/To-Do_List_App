import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter a To-Do",key='todo')
add_button = sg.Button("Add")

window = sg.Window("My To-Do App",
                   layout=[
                       [label],
                       [input_box, add_button]
                           ],
                   font=('Times New Roman',14)
                   )
while True:
    action, value = window.read()
    print(action)
    print(value)
    match action:
        case 'Add':
            todos = functions.get_todo()
            new_todo = value["todo"] + '\n'
            todos.append(new_todo)
            functions.write_todo(todos)
        case sg.WIN_CLOSED:
            break

window.close()
