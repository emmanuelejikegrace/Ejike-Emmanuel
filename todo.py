tasks = []

while True:
    print("\n --- TO-DO LIST ---")
    print("1. Add new task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Edit task")
    print("5. Exit!")

    choice = input("choose an option: ")

    if choice == "1":
        task = input("Enter a task: ")

        if task.strip() == "":
            print("Task cannot be empty!")

        elif task in tasks:
            print("Task already exists!")    
        else:
            tasks.append(task)
            print("Task added!")    

    elif choice == "2":
        if len(tasks) == 0:
            print("you have no task yet!")

        else:
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")     

    elif choice == "3":
        if len(tasks) == 0:
            print("You have no task to remove")
        else:
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")

        try:    
            task_number = int(input("Enter the number of the task you want to remove: "))

            if task_number >= 1 and task_number <= len(tasks):

                tasks.pop(task_number - 1)

                print("Task removed!")
            else:
                print("Invalid task number") 

        except ValueError:
            print("Please enter a valide number")             

    elif choice == "4":
        if len(tasks) == 0:
            print("you have no task to edit!")

        else:
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")

            try:
                task_number = int(input("Enter the number of the task you want to edit: "))

                if task_number >= 1 and task_number <= len(tasks):
                    new_task = input("Enter the new task: ")

                    if new_task.strip() == "":
                        print("Task cannot be empty!")
                    else:
                        tasks[task_number - 1] = new_task
                        print("Task updated!")

                else:
                    print("Invalid task number")

            except ValueError:
                print("please enter a valid number")
    elif choice == "5":
        print("Thank you for using the to-do list, Goodbye!")
        break
    else:
        print("Invalid choice, please choose a number between 1 to 5")





