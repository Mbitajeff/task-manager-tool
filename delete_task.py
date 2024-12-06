# delete_task.py
tasks = ["Sample Task 1", "Sample Task 2"]

def delete_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task deleted: {task}")
    else:
        print(f"Task not found: {task}")

if __name__ == "__main__":
    task = input("Enter a task to delete: ")
    delete_task(task)


