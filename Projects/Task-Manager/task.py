import json
import uuid

print("1:Add task")
print("2:View task")
print("3:Mark task as done")
print("4:Delete task")

selected_menu = input("What do you want to do? ")
filename = "D:\\learn_python\\Projects\\Task-Manager\\tasks.json"

if selected_menu == "1":
    # print("Enter a task:")
    task = input("Enter a task:\n")
    # print(task)

    # filename = "D:\\learn_python\\Projects\\Task-Manager\\tasks.json"
    new_entry = {"id": str(uuid.uuid1()), "task_name": task, "done": False}

    # Step 2: Read file contents
    with open(filename, "r") as file:
        data = json.load(file)

    # Step 3: Update json object
    data.append(new_entry)

    # Step 4: Write json file
    with open(filename, "w") as file:
        json.dump(data, file)
elif selected_menu == "2":
    # print("These are your task")
    with open(filename,"r") as file:
        data=json.load(file)
        for index, task in enumerate(data):
            print(index+1,":", task.get("task_name"))

elif selected_menu == "3":
    # print("Input task id to marked it as done")
    task_id=input("Enter an id of task to mark it as done?  ")
    task_found=False
    with open(filename,"r") as file:
        data=json.load(file)
        for task in data:
            if task.get("id")==task_id:
                task_found=True
                task["done"]=True
                print("Task with this id exists") 
                break  
            else:
                pass
        if task_found==False:
            print("Task with given id doesnot exist")

        # print("change data",data)
        with open(filename, "w") as file:
            json.dump(data, file)
elif selected_menu == "4":
    print("Input your task id to deleted")
    delete_task_id=input("Enter an id of a task you want to delete? ")
    task_found=False
    with open(filename,"r") as file:
        data=json.load(file)
        for index, task in enumerate (data):
            if task.get("id")==delete_task_id:
                task_found=True
                data.pop(index)
                # print("Task with this id exists") 
                break  
            else:
                pass
        if task_found==False:
            print("Task with given id doesnot exist")

        # print("change data",data)
        with open(filename, "w") as file:
            json.dump(data, file)
else:
    print("Selected menu is invalid")
