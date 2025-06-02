filepath = ("D:\python\Python_summer_tasks\Task06.txt")

def load_tasks():
    tasks = []
    try:
        with open(filepath,"r") as file:
            for line in file:
                task,status = line.strip().split("||")
                tasks.append({"tasks": task, "done": status == "done"})
    except FileNotFoundError:
        open(filepath,"w").close()
    return tasks

def save_tasks(tasks):
    with open(filepath,"w") as file :
        for task in tasks :
            status = "done" if task["done"] else "pending"
            file.write(f"{task['task']}||{status}\n")

def add_task(tasks):
    task_name = input("Enter your task name :").strip()
    tasks.append({"task" : task_name,"done": False})
    save_tasks(tasks)
    print("Task saved sucessfully ✅\n")

def view_tasks(tasks):
    if not tasks :
        print("No Tasks found. \n")
        return
    print("\n To do list :")
    for idx, task in enumerate(tasks,1):
        status = "✅" if task["done"] else "❌"
        print(f"{idx}.{task['task']} [{status}]")
    print()

def mark_task_done(tasks):
    view_tasks(tasks)
    try :
        task_num = int(input("Enter task number to mark as done :"))
        if 1 <= task_num <= len(tasks) :
            tasks[task_num -1]["done"] = True
            save_tasks(tasks)
            print("Task marked as done.\n")
        else :
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number .\n")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Deleted task: {removed['task']}\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def main():
    print("=== Simple To-Do App ===")
    tasks = load_tasks()

    while True:
        print("Menu:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select from the menu.\n")

if __name__ == "__main__":
    main()
        