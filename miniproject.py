tasks = []

def add_task():
    task = input("Enter new task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks found.")
        return

    print("\nYour Tasks:")
    for idx, t in enumerate(tasks, 1):
        status = "✔ Done" if t["completed"] else "⏳ Pending"
        print(f"{idx}. {t['task']} - {status}")

def mark_complete():
    view_tasks()
    try:
        num = int(input("Enter task number to mark complete: "))
        tasks[num-1]["completed"] = True
        print("Task marked as completed!")
    except (ValueError, IndexError):
        print("Invalid task number!")

def delete_task():
    view_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        tasks.pop(num-1)
        print("Task deleted!")
    except (ValueError, IndexError):
        print("Invalid task number!")

def save_tasks():
    try:
        with open("tasks.txt", "w") as file:
            for t in tasks:
                file.write(f"{t['task']}|{t['completed']}\n")
        print("Tasks saved to file!")
    except:
        print("Error while saving!")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                name, status = line.strip().split("|")
                tasks.append({"task": name, "completed": status == 'True'})
        print("Tasks loaded from file!")
    except FileNotFoundError:
        print("No saved file found!")
    except:
        print("Error while loading!")

def menu():
    load_tasks()
    while True:
        print("\n---- TO-DO MENU ----")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Complete")
        print("4. Delete Task")
        print("5. Save Tasks")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_complete()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            save_tasks()
        elif choice == '6':
            save_tasks()
            print("Bye!")
            break
        else:
            print("Invalid option!")

menu()