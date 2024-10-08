

#The intent of this application is to walk users through creating on itemized list of tasks that can be modified based on completion and necessity.
# Menu1 is adding tasks to a list through input
# Menu2 is printing said list itemized
# Menu3 is moving tasks from To-Do list to Completed and removing them from the first list
# Menu4 is deleting a task from To-Do list
# Menu5 is exiting app
# BONUS: Prioritize tasks, add due dates, color-coding tasks based on status.

todo_list = []
completed_list = []


def task_manager():
    print('\nWelcome to the To-Do List Application!')
    while True:
        try:
            selection = input(' \nMenu:\n\n1. Add a Task\n2. View Task\n3. Mark a task as complete\n4. Delete a task\n5. Quit\n\nPlease select a menu option: ')
        except ValueError: # Handles an input that is not an int
            print('Selection should be just the number.\n For Example: If you would like to add a task, simply input "1"')
        else:
            if selection == '1':
                adding_task()
            elif selection =='2':
                view_list()
            elif selection == '3':
                alter_todo_list()
            elif selection == '4':
                delete()
            elif selection == '5':
                quit()
                break
            

def adding_task():            
        while True:
            add_task = input('Would you like to add a task? Yes/No ').lower()
            if add_task == 'yes':
                addition = input(f'Please input task to add to your To-Do list: ')
                todo_list.append(addition)
            elif add_task =='no':
                break    
            else:
                print('Try Again')


def view_list():
    print('Here is your current task list:')
    for count, task in enumerate(todo_list, 1):
        print(f'{count}. {task}') # List each task itemized

def alter_todo_list():
    try: 
        print('Here is your current task list:')
        for count, task in enumerate(todo_list, 1):
            print(f'{count}. {task}') # List each task itemized
        to_mark_complete = (int(input('\nWhich task is completed?\n Input the corresponding task line number: ')) - 1)
        completed_list.append(todo_list[to_mark_complete])
        del todo_list[to_mark_complete]
        print('Tasks to do:')
        for count, task in enumerate(todo_list, 1):
            print(f'{count}. {task}') # List each task itemized
        print('Tasks completed:')
        for count, task in enumerate(completed_list, 1):
            print(f'{count}. {task}') # List each task itemized
    except IndexError:
        print('This task does not exist in your "To-Do" list\n Please be sure to use the task line number for your selection.')
    except ValueError:
        print('Selection example: "1" instead of "One".')

def delete():
    for count, task in enumerate(todo_list, 1):
            print(f'{count}. {task}') # List each task itemized
    try: #need to make the following input relate to the slice of the list
        delete_task = (int(input('Which task no longer requires compeltion?\n Input the appropriate line number: '))-1)
        del todo_list[delete_task]
    except ValueError: #Handle unexpected inputs
        print('This task does not exist in your "To-Do" list\n Please be sure to use the task line number for your selection.')
    except IndexError:
        print('Selection example: "1" instead of "One".')
    else:
        print('Here is your current task list:')
        for count, task in enumerate(todo_list, 1):
            print(f'{count}. {task}') # List each task itemized

def quit():
    quit = input('Are you sure you want to quit? Yes/No? ').lower()
    if quit == 'yes':
        print('Thank you for using the "To-Do List"! \n Wishing you a productive day!')
        print('\nHere are your current "To-Do" tasks:')
        for count, task in enumerate(todo_list, 1):
            print(f'{count}. {task}')
        print('\nHere are your current "Completed" tasks:')
        for count, task in enumerate(completed_list, 1):
            print(f'{count}. {task}')
    else:
        print('Return to main menu.')        
    

task_manager()
