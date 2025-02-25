import json
import uuid
def display_menu():
    print("Task Manager")
    print("1:Add task")
    print("2:View task")
    print("3:Mark task as done")
    print("4:Delete task")
    print("======================")
def load_tasks(filename):
    try:        
        if not filename:
            with open(filename, "w") as file:

                json.dump([],file)
            return []
        with open (filename, "r") as file:
                print("file",file)
                return json.load(file)
    except Exception as e:
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

def main():
    filename = "D:\\learn_python\\Projects\\Task-Manager\\tasks.json"
    
    while True:
        display_menu()
        selected_menu=input("What do you want to do? ")

        if selected_menu == "1":
            task=input("Enter a task:\n")
            add_task(filename,task)




if __name__=="__main__":
    main()

