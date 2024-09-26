thingstodo = []


def listt(thingstodo, todolist):

    if todolist == 'show list':
        return f'Your list is: {', '.join(thingstodo)}'
    elif 'remove' in todolist:
        stuff_to_remove = todolist.replace('remove', '').strip().split(',')
        for item in stuff_to_remove:
            item = item.strip()
            if item in thingstodo:
                thingstodo.remove(item)
        return f'Updated list after removal: {', '.join(thingstodo)}'
    else:
        thingstodo.extend([item.strip() for item in todolist.split(',')])
    return ''' Saved to the list. '''


while True:
    todolist = input('Enter the things you have to do in your to do list. \n rules: (seperate with a comma), if you want to show list, say \'show list\'. \n If you want to remove something, say \'remove\' and the things you want removed: ')
    print(f'{listt(thingstodo, todolist)}')