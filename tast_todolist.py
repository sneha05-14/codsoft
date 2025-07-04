todo_list = []

def view_tasks():
    if not todo_list:
        print("Your to-do list is empty!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(todo_list, start=1):
            status = "✓" if task["completed"] else "✗"
            print(f"{i}. [{status}] {task['task']}")

def add_task():
    task = input("Enter the task: ")
    todo_list.append({"task": task, "completed": False})
    print("Task added!")

def complete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to mark as completed: "))
        if 1 <= task_num <= len(todo_list):
            todo_list[task_num - 1]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(todo_list):
            removed = todo_list.pop(task_num - 1)
            print(f"Task '{removed['task']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
