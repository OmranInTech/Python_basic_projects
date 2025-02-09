tasks = []

def Addingtask():
    task = input("Enter task to do: ")
    tasks.append(task)
    print("Task added successfully!")

def showingtasks():
    if tasks:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks available.")

def delete_task():
    showingtasks()
    if tasks:
        try:
            task_index = int(input("Enter task number to delete: ")) - 1
            if 0 <= task_index < len(tasks):
                removed_task = tasks.pop(task_index)
                print(f"Removed task: {removed_task}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

while True:
    print("\n1- Add Task")
    print("2- Show Tasks")
    print("3- Delete Task")
    print("4- Exit")

    try:
        input_a = int(input("Select Option: "))
        
        if input_a == 1:
            Addingtask()
        elif input_a == 2:
            showingtasks()
        elif input_a == 3:
            delete_task()
        elif input_a == 4:
            print("Goodbye!")
            break
        else:
            print("Wrong option selected. Try again.")
    except ValueError:
        print("Please enter a valid number.")
