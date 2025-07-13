def show_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks added.")
            else:
                print("Your Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks file found.")

def add_task():
    task = input("Enter new task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added!")

def remove_task():
    show_tasks()
    try:
        task_num = int(input("Enter task number to remove: "))
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        if 1 <= task_num <= len(tasks):
            del tasks[task_num - 1]
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print("Task removed.")
        else:
            print("Invalid task number.")
    except:
        print("Error occurred.")

while True:
    print("\n1. Show Tasks\n2. Add Task\n3. Remove Task\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        break
    else:
        print("Invalid choice!")