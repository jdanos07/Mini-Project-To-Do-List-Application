todo_list = []
completed_list = []
Dict_list_names = {}

def list_personalizing(): #Name list and possibly add future possibility of multiple lists
    personalize_list = input('Would you like to name your list? Yes/No ').lower
    if personalize_list == 'yes':
        list_name = input('Input list name here: ')
        print(list_name)
        Dict_list_names.update(list_name)
        
    else:
        pass

list_personalizing()
print(Dict_list_names)