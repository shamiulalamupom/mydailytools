import pickle
import os
from pathlib import Path

def load_tasks(filename: str):
    while 1:
        try:
            with open(filename, 'rb') as file:
                todo_list = pickle.load(file)
                return todo_list
        except Exception as e:
            Path(f'{os.getcwd()}/todo_list.pkl').touch()
            with open(filename, 'wb') as file:
                pickle.dump([], file)

def addtask():
    todo_list = load_tasks('todo_list.pkl')
            
    todo = {"title": input("Title: "), "desc": input("Description: ")}
    todo_list.append(todo)
    with open('todo_list.pkl', 'wb') as file:
        pickle.dump(todo_list, file)
    print("New task has been added!")

def displaytask():
    todo_list = load_tasks('todo_list.pkl')
    if not todo_list:
        print("There is no task to display.")
    else:
        print("Todos that I need to do:")
        for todo in todo_list:
            print(f"{todo['title']}: {todo['desc']}")

def deletetask():
    todo_list = load_tasks('todo_list.pkl')
    
    if not todo_list:
        print("There is no todo to delete.")
    else:
        print("Which todo you want to delete. Select by number: ")
        index = 1
        for todo in todo_list:
            print(f"{index}. {todo['title']}: {todo['desc']}")
            index+=1
        try:
            inp = int(input(f"Enter which task you want to delete (1 to {index-1}): "))
            if inp < index:
                todo_list.pop(inp-1)
            with open('todo_list.pkl', 'wb') as file:
                pickle.dump(todo_list, file)
        except ValueError:
            print("There was an error. Please try again in some time.")

def modifytask():
    todo_list = load_tasks('todo_list.pkl')
    if not todo_list:
        print("There is no todo to modify.")
    else:
        print("Which todo you want to delete. Select by number: ")
        index = 1
        for todo in todo_list:
            print(f"{index}. {todo['title']}: {todo['desc']}")
            index+=1
        try:
            inp = int(input(f"Enter which task you want to modify (1 to {index-1}): "))
            if inp < index:
                print("Leave empty if you don't want to change.")
                inp_title = input("Enter the new title: ")
                inp_desc = input("Enter the new description: ")

                if inp_title:
                    todo_list[inp-1]["title"] = inp_title
                    
                if inp_desc:
                    todo_list[inp-1]["desc"] = inp_desc
                
            with open('todo_list.pkl', 'wb') as file:
                pickle.dump(todo_list, file)
        except ValueError:
            print("There was an error. Please try again in some time.")

def todo_list():
    while 1:
        print("""Choose between the tasks you want to do:
    1. Add a task.
    2. Display all the tasks.
    3. Delete a task.
    4. Modify a task.""")
        inp = input("Enter your choice (1-4 and Enter to close): ")
        if inp == '':
            break
        
        try:
            inp = int(inp)
        except ValueError:
            print("Please try again in some time.")

        if inp == 1:
            addtask()
        elif inp == 2:
            displaytask()
        elif inp == 3:
            deletetask()
        elif inp == 4:
            modifytask()
        else:
            print("Try again in some time.")

if __name__ == "__main__":
    todo_list()