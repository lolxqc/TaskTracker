def add_task(tasks,task_name):
    tasks.append({"name":task_name,"completed":False})
    print(f"Task'{task_name}'added.")

def view_tasks(tasks):
    if not tasks:
        print("No task in the list.")
        return
    for index, task in enumerate(tasks):
        status="[x]" if task["completed"] else "[ ]"
        print(f"{index+1}.{status}{task['name']}")

def complete_task(tasks,task_index):
    if 1<=task_index <=len(tasks):
        tasks[task_index-1]["completed"]=True
        print(f"task{task_index}marked as completed.")
    else:
        print("Invalid task number")

def delete_task(tasks,task_index):
    if 1<=task_index <=len(tasks):
        del tasks[task_index-1]
        print(f"Task{task_index} deleted.")
    else:
        print("Invalid taks number.")

tasks=[]
while True:
    print("\nTask Tracker Menu:")
    print("1.Add Task")
    print("2.View Task")
    print("3.complete task")
    print("4.Delete task")
    print("5.Exit")

    choice=input("enter your choice: ")
    if choice=="1":
        task_name=input("enter task name: ")
        add_task(tasks,task_name)
    elif choice=="2":
        view_tasks(tasks)
    elif choice=="3":
        task_index=int(input("enter task number to complete: "))
    elif choice=="4":
        task_index=int(input("enter task number to delete: "))
        delete_task(tasks,task_index)
    elif choice=="5":
        break
    else:
        print("Invalid choice.Please try again")
