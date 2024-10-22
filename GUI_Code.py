import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter a To-Do",
                         key='todo',
                         size=(30, 10)
                         )
list_box = sg.Listbox(functions.get_todo(),
                      key="todos",
                      size=(30, 10)
                      )
label2 = sg.Text(key='popUp')

add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
close_button = sg.Button("Close")

window = sg.Window("My To-Do App",
                   layout=[
                       [label],
                       [input_box, add_button],
                       [list_box,],
                       [edit_button, complete_button, close_button],
                       [label2]
                           ],
                   font=('Times New Roman', 14)
                   )

while True:
    action, value = window.read()
    print(action)
    print(value)
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
                todos_list[index_of_new_todo] = new_todo + '\n'
                functions.write_todo(todos_list)
                window['todos'].update(values=todos_list)
                window['popUp'].update(f"{todo_to_edit} is updated to {new_todo}")
            except IndexError:
                window['popUp'].update("Please Select a todo to edit!")
        case 'todos':
            window['todo'].update(value=value['todos'][0])
        case 'Complete':
            try:
                completed_todo = value['todos'][0]
                todos = functions.get_todo()
                todos.remove(completed_todo)
                functions.write_todo(todos)
                window['todos'].update(values=todos)
                window['popUp'].update(f"Yay! you have completed-{completed_todo}")
            except IndexError:
                window['popUp'].update("Please Select the todo you have completed!")
        case 'Close':
            break
        case sg.WIN_CLOSED:
            break
window.close()
