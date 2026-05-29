# Initialize storage: The list acts as your full "Database Table" 
my_tasks = []

def add_task():
    """Input phase: Capturing task details."""
    task_desc = input("Enter task description: ")
    
    # Process phase: Dictionary maps to a 'Table Row' 
    new_task = {
        'id': len(my_tasks) + 1, # Primary Key concept
        'task': task_desc
    }
    
    # Process phase: Appending to list simulates 'INSERT INTO' 
    my_tasks.append(new_task)
    print("Task committed to system.")

def view_tasks():
    """Output phase: Iterator protocol creating a temporary view of the state."""
    print("\n--- CURRENT TABLE STATE ---")
    if not my_tasks:
        print("Table is empty.")
    else:
        # Iterator Protocol used to read data [cite: 210, 214]
        for row in my_tasks:
            print(f"ID: {row['id']} | TASK: {row['task']}")

def delete_task():
    """Process phase: Deleting a row from the list."""
    try:
        task_id = int(input("Enter ID to delete: "))
        
        # Logic to recreate the list without the target 'row' 
        new_list = [row for row in my_tasks if row['id'] != task_id]
        
        if len(new_list) == len(my_tasks):
            print("Error: Task ID not found.")
        else:
            my_tasks[:] = new_list # Updating the persistent list in memory
            print("Row processed: Task deleted.")
    except ValueError:
        print("Invalid input: Please enter a numeric ID.")

def main():
    while True:
        print("\n--- TO-DO LIST (DATABASE SIMULATION) ---")
        print("1. Add Task (INSERT)")
        print("2. View Tasks (SELECT ALL)")
        print("3. Delete Task (DELETE)")
        print("4. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()