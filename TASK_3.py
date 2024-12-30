tasks = []

x = "1. Add Task"
y = "2. Remove Task"
z = "3. View Task List"
a = "4. Exit"

# Display the menu
print(x)
print(y)
print(z)
print(a)

while True:
    task = input("\nEnter your choice of task (1/2/3/4): ")

    if task == '1':
        new_task = input("Enter the task to add: ")
        tasks.append(new_task)
        print(f"Task '{new_task}' added to the list!")

    elif task == '2':
        remove_task = input("Enter the task to remove: ")
        if remove_task in tasks:
            tasks.remove(remove_task)
            print(f"Task '{remove_task}' removed from the list!")
        else:
            print(f"Task '{remove_task}' not found in the list!")

    elif task == '3':
        if not tasks:
            print("Your to-do list is empty.")
        else:
            print("Here's your to-do list:")
            for index, t in enumerate(tasks, 1):
                print(f"{index}. {t}")

    elif task == '4':
        print("Exiting the To-Do List App.")
        break

    else:
        print("Invalid choice. Please select from 1, 2, 3, or 4.")

