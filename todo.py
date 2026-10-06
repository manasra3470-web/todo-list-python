tasks = []


def show_tasks():
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\n----- YOUR TASKS -----")
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else " "
        print(f"{i}. [{status}] {task['name']}")


def add_task():
    task_name = input("\nEnter task: ")

    if task_name.strip() == "":
        print("Task cannot be empty.")
        return

    tasks.append({
        "name": task_name,
        "completed": False
    })

    print("Task added successfully!")


def complete_task():
    show_tasks()

    if not tasks:
        return

    try:
        task_number = int(input("\nEnter task number to complete: "))

        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            print("Task completed!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    show_tasks()

    if not tasks:
        return

    try:
        task_number = int(input("\nEnter task number to delete: "))

        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            print(f"Deleted: {deleted_task['name']}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


while True:
    print("\n======================")
    print("      TO-DO LIST")
    print("======================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("\nThank you for using To-Do List!")
        break
    else:
        print("\nInvalid choice. Please try again.")
