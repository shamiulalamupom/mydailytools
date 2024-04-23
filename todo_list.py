my_todo_list = []

def addtask():
    todo = {"title": input("Title: "), "desc": input("Description: ")}
    my_todo_list.append(todo)
    print("New task has been added!")

def displaytask(todo_list):
    if not todo_list:
        print("There is no task to display.")
    else:
        print("Todos that I need to do:")
        for todo in todo_list:
            print(f"{todo['title']}: {todo['desc']}")

def deletetask(todo_list: list):
    if not todo_list:
        print("There is no todo to delete.")
    else:
        print("Which todo you want to delete. Select by number: ")
        index = 1
        for todo in todo_list:
            print(f"{index}. {todo['title']}: {todo['desc']}")
            index+=1
        try:
            inp = int(input(f"Enter which task you want to delete (1 to {index-1})"))
            if inp < index:
                todo_list.pop(inp-1)
        except ValueError:
            print("There was an error. Please try again in some time.")

def modifytask(todo_list):
    if not todo_list:
        print("There is no todo to modify.")
    else:
        print("Which todo you want to delete. Select by number: ")
        index = 1
        for todo in todo_list:
            print(f"{index}. {todo['title']}: {todo['desc']}")
            index+=1
        try:
            inp = int(input(f"Enter which task you want to modify (1 to {index-1})"))
            if inp < index:
                print("Leave empty if you don't want to change.")
                inp_title = input("Enter the new title: ")
                inp_desc = input("Enter the new description: ")

                if inp_title:
                    todo_list[inp-1]["title"] = inp_title
                    
                if inp_desc:
                    todo_list[inp-1]["desc"] = inp_desc
        except ValueError:
            print("There was an error. Please try again in some time.")
