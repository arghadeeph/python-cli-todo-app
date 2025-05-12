from database import get_db_connection 

conn = get_db_connection()
cursor = conn.cursor(dictionary=True)

def add_task():
    taskvalue = input("Enter a new task: ")
    cursor.execute("INSERT INTO tasks (task) VALUES (%s)", (taskvalue,))
    conn.commit()
    print("Task added successfully!") 
    view_task()

def view_task():
    cursor.execute("SELECT * FROM tasks")  
    tasks = cursor.fetchall() 
    print("\nYour Tasks:") 
    for task in tasks:
        status = '✔️' if task['is_done'] else '❌'
        print(f"{task['id']} -> {task['task']} {status}")

def mark_done():
    task_id = input("Enter task ID to mark as completed: ")
    cursor.execute('UPDATE tasks set is_done = TRUE WHERE id= %s', (task_id,))
    conn.commit()
    print('The task marked completed!')
    view_task()

def delete_task():
    task_id = input("Enter task ID to delete task: ")
    cursor.execute('DELETE FROM tasks WHERE id= %s', (task_id,))
    conn.commit()
    print('The task deleted successfully!')
    view_task()   

def menu():
    while True:
         print("\nTo-Do List Menu")
         print("1. Add Task")
         print("2. View Tasks")
         print("3. Mark Task as Completed")
         print("4. Delete Task")
         print("5. Exit")

         choice = input('Choose an option: ')

         if choice == '1':
            add_task()
         elif choice == '2':
             view_task()
         elif choice == '3':
             mark_done()
         elif choice == '4':
            delete_task()   
         elif choice == '5':
            break
         else:
            print("Invalid choice. Try again.")    


if __name__ == "__main__":
    menu()
    cursor.close()
    conn.close()
