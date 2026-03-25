import json
import os

#The file to save the to-do list tasks
SAVE_FILE = "to-do-list.json"

#Loads tasks from the save file if it exists, otherwise returns an empty list
def load_tasks():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, 'r') as f:
            return json.load(f)
    return []

#Saves the current list of tasks to the save file
def save_tasks(tasks):
    with open(SAVE_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

#Displays the current list of tasks, or a message if there are no tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        print("To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

#Adds a new task to the list after prompting the user for input
def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print("Task added.")
    else:
        print("No task entered.")

#Removes a task from the list based on user input, after displaying the current tasks
def remove_task(tasks):
    display_tasks(tasks)
    if tasks:
        try:
            idx = int(input("Enter the number of the task to remove: "))
            if 1 <= idx <= len(tasks):
                removed_task = tasks.pop(idx - 1)
                print(f"Removed task: {removed_task}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

#Marks a task as completed by removing it from the list, after displaying the current tasks
def complete_task(tasks):
    display_tasks(tasks)
    if tasks:
        try:
            idx = int(input("Enter the number of the task to mark as completed: "))
            if 1 <= idx <= len(tasks):
                completed_task = tasks.pop(idx - 1)
                print(f"Completed task: {completed_task}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    
    while True:
        print("\nMenu:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Mark task as completed")
        print("5. Exit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
            save_tasks(tasks)
        elif choice == '3':
            remove_task(tasks)
            save_tasks(tasks)
        elif choice == '4':
            complete_task(tasks)
            save_tasks(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()