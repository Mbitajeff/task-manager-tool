tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task added: {task}")

if __name__ == "__main__":
    task = input("Enter a task to add: ")
    add_task(task)


