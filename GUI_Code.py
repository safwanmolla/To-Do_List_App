import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter a To-Do",
                         key='todo',
                         size=(30,10)
                         )
add_button = sg.Button("Add")

list_box = sg.Listbox(functions.get_todo(),
                      key="todos",
                      size=(30,10)
                      )
edit_button= sg.Button("Edit")
window = sg.Window("My To-Do App",
                   layout=[
                       [label],
                       [input_box, add_button],
                       [list_box,edit_button]
                           ],
                   font=('Times New Roman',14)
                   )
while True:
    action, value = window.read()
    # print(action)
    # print(value)
    # print(value['todos'])
    # Above will give us some insights about the variables.
    match action:
        case 'Add':
            todos = functions.get_todo()
            new_todo = value["todo"] + '\n'
            todos.append(new_todo)
            functions.write_todo(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = value['todos'][0]
                new_todo = value['todo']
                todos_list = functions.get_todo()
                index_of_new_todo = todos_list.index(todo_to_edit)
                todos_list[index_of_new_todo] = new_todo +'\n'
                functions.write_todo(todos_list)
                window['todos'].update(values=todos_list)
            except IndexError:
                print("Please Select a todo to edit")
        case 'todos':
            window['todo'].update(value=value['todos'][0])
        case sg.WIN_CLOSED:
            break


window.close()
