import json
import uuid
def display_menu():
    print("Task Manager")
    print("1:Add task")
    print("2:View task")
    print("3:Mark task as done")
    print("4:Mark task as undone")
    print("4:Delete task")
    print("======================")
def load_tasks(filename):
    try:        
        
        with open (filename, "r") as file:
                print("file",file)
                return json.load(file)
    except Exception as e:
        return []
        print(e)
def save_tasks(filename,tasks):
    with open(filename, "w") as file:
        json.dump(tasks,file)
    return True

def add_task(filename,task_name):  
    if not task_name.strip():
        print("Task name cannot be empty")
        return False

    tasks=load_tasks(filename)
    print("tasks",tasks)
    new_task={"id":str(uuid.uuid4()), "task_name":task_name.strip(), "done":False}
    tasks.append(new_task)
    save_tasks(filename,tasks)
def view_task(filename):
    tasks=load_tasks(filename)
    if not tasks:
        print("No task available")
        return    
    for index,task in enumerate(tasks):
        print(index+1,".",task["task_name"])
def mark_task_done(filename):
    task_id=input("Enter an id of the task to mark it as done: ")
    tasks=load_tasks(filename)
    for task in tasks:
        if task_id==task["id"]:
            task["done"]=True
            save_tasks(filename,tasks)
            print("Task marked as done")
            return
    print("Task not found") 
def mark_task_undone(filename):
    task_id=input("Enter an id of the task to mark it as undone:")
    tasks=load_tasks(filename)
    for task in tasks:
        if task_id==task["id"]:
            
            if task["done"]==False:
                print("Task is already undone")
                return
            task["done"]=False
            save_tasks(filename,tasks)
            print("Task marked as undone")
            return
    print("Task not found")  
def delete_task(filename):
    delete_task_id=input("Enter an id of the task that need to be deleted:")
    tasks=load_tasks(filename)   
    for index, task in enumerate(tasks):
        if delete_task_id==task["id"]:
            tasks.pop(index)
            save_tasks(filename,tasks)
            print("Task deleted successfully")
            return
    print("Task doesnot exist")

def main():
    filename = "D:\\learn_python\\Projects\\Task-Manager\\tasks.json"
    
    while True:
        display_menu()
        selected_menu=input("What do you want to do? ")

        if selected_menu == "1":
            task=input("Enter a task:\n")
            add_task(filename,task)
        elif selected_menu=="2":
            view_task(filename)
        elif selected_menu=="3":
            mark_task_done(filename)
        elif selected_menu=="4":
            mark_task_undone(filename)  
        elif selected_menu=="5":
            delete_task(filename)
              

        




if __name__=="__main__":
    main()

