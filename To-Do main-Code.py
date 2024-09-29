# from functions import get_todo , write_todo
import functions
import time


now = time.strftime("%b %d, %Y and %H:%M:%S")
print("It is ", now)
while True:
    user_action = (input("Enter what yo wanna do. Add, Edit, Show, Mark completed or Exit")).strip()
    user_action = user_action.capitalize()

    """
    if 'Add' in user_action:
    Above if statement gets executed even if someone give an input like "edit Add a member" 
     which should execute the if statement with "Edit" condition
    """

    if user_action.startswith('Add'):
        todo = user_action[4:]
        todo = todo.capitalize()

        todos = functions.get_todo("todos.txt")
        todos.append(todo + '\n')

        functions.write_todo(todos)

        print("Added a new To-Do: ", todo)

    elif user_action.startswith('Show'):

        todos = functions.get_todo()

        for index, item in enumerate(todos):
            item.capitalize()
            print(f'{index + 1}-{item}', end='')

    elif user_action.startswith('Edit'):
        try:
            number = int(user_action[5:])
            index = number - 1

            todos = functions.get_todo()

            new_todo = input('Enter new To-Do: ')
            new_todo = new_todo.capitalize()
            todos[index] = new_todo + '\n'

            functions.write_todo(todos)

        except ValueError:
            print("Entered value after 'Edit' command must be the number of the To-Do you want to edit.")
            continue
        except IndexError:
            print(f"{number} does not exists. Do you want to add '{new_todo}' as a new To-Do ?")
            continue
    elif user_action.startswith('Complete'):

        todos = functions.get_todo()

        number = int(user_action[9:])
        index = number - 1
        todo_to_remove = todos[index].strip('\n')  # we need to strip '\n' as it could make a newline in output
        todos.pop(index)

        functions.write_todo(todos)

        print(f'Yay! You have completed - {todo_to_remove}')

    elif user_action.startswith('Exit'):
        print('See Ya !')
        break

    else:
        print()
        print("Please choose an action from Add, Show, Edit, Mark Complete or Exit.")
        print()
