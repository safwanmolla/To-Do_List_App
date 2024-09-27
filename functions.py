def get_todo(filepath='todos.txt'):
    with open(filepath, 'r') as f:
        local_todos = f.readlines()

    return local_todos


def write_todo(local_todo, filepath='todos.txt'):
    with open(filepath, 'w') as f:
        f.writelines(local_todo)
