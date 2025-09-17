tasks = []

def addTask():
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"Task: '{task}' added to the list")

def listTasks():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current Tasks: ")
        for index, task in enumerate(tasks):
            print(f"#{index} : {task}")

def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Enter the # to delete: "))
        if not taskToDelete < 0 and taskToDelete <= len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task {taskToDelete} has been removed.")
        else:
            print(f"Task #{taskToDelete} was not found.")

    except:
        print("Invalid Input")

if __name__ == "__main__":
    print("Welcome to the to-do  list app")
    while True:
        print("Please select one of the following options:")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")

        choice = input("Enter your choice: ").lower().strip()

        if choice == "1":
            addTask()
        elif choice == "2":
            deleteTask()
        elif choice == "3":
            listTasks()
        elif choice == "4":
            break
        else:
            print("Invalid input. Please try again.")
    print("Goodbye!")
