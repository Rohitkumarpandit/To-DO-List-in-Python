tasks = []
def add_task():
  task = input("Enter a task: ")
  tasks.append(task)
  print("Task added!")

def view_tasks():
  if not tasks:
    print("No tasks added yet!")
    return
  for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")
def main():
  while True:
    # Display menu options
    print("\nTo-Do List App")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")
    
    # Get user choice
    choice = input("Enter your choice (1-3): ")
    
    if choice == '1':
      add_task()
    elif choice == '2':
      view_tasks()
    elif choice == '3':
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()