tasks = []

while True:
    print("\n --- TO-DO LIST ---")
    print("1. Add new task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("choose an option: ")

    if choice == "1":
        task = input("Enter a task: ")
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
        print("Thank you for useing the To-Do list. Goodbye!")
        break
    else:
        print("Invalid choice. Choose a number between 1 to 4!")                   


