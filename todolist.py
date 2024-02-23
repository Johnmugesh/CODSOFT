tasks = []

def add_task(task):
    tasks.append(task)

def delete_task(index):
    if index < len(tasks):
        del tasks[index]
    else:
        print("Task index out of range.")

def update_task(index, new_task):
    if index < len(tasks):
        tasks[index] = new_task
    else:
        print("Task index out of range.")

def mark_completed(index):
    if index < len(tasks):
        tasks[index] += " - Completed"
    else:
        print("Task index out of range.")

while True:
    print("\nCurrent Tasks:")
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task}")
        
    print("\nMenu:")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Update Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task to add: ")
        add_task(task)
    elif choice == "2":
        index = int(input("Enter task index to delete: ")) - 1
        delete_task(index)
    elif choice == "3":
        index = int(input("Enter task index to update: ")) - 1
        new_task = input("Enter new task: ")
        update_task(index, new_task)
    elif choice == "4":
       index = int(input("Enter task index to mark as completed: ")) - 1
       mark_completed(index)
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
