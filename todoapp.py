import json
import os

TODO_FILE = "todos.json"

class TodoList:
    def __init__(self):
        self.todos = []
        self.load_todos()

    def load_todos(self):
        if os.path.exists(TODO_FILE):
            with open(TODO_FILE, 'r') as file:
                self.todos = json.load(file)

    def save_todos(self):
        with open(TODO_FILE, 'w') as file:
            json.dump(self.todos, file, indent=4)

    def add(self, task):
        self.todos.append({"task": task, "done": False})
        self.save_todos()

    def remove(self, index):
        if 0 <= index < len(self.todos):
            self.todos.pop(index)
            self.save_todos()

    def list(self):
        for i, todo in enumerate(self.todos):
            status = "Done" if todo["done"] else "Not Done"
            print(f"{i + 1}. {todo['task']} - {status}")

    def mark_done(self, index):
        if 0 <= index < len(self.todos):
            self.todos[index]["done"] = True
            self.save_todos()

def main():
    todo_list = TodoList()

    while True:
        print("\nTodo List Application")
        print("1. Add a new task")
        print("2. Remove a task")
        print("3. List all tasks")
        print("4. Mark a task as done")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add(task)
            print("Task added.")
        elif choice == '2':
            index = int(input("Enter the task number to remove: ")) - 1
            todo_list.remove(index)
            print("Task removed.")
        elif choice == '3':
            todo_list.list()
        elif choice == '4':
            index = int(input("Enter the task number to mark as done: ")) - 1
            todo_list.mark_done(index)
            print("Task marked as done.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
