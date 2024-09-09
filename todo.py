import argparse
import json
import os

# File to store the tasks
TODO_FILE = 'tasks.json'


def load_tasks():
    """Loads tasks from the JSON file."""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    """Saves tasks to the JSON file."""
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file)


def add_task(task):
    """Adds a task to the list."""
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print(f'Task "{task}" added.')


def list_tasks():
    """Lists all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found!")
        return

    for i, task in enumerate(tasks, 1):
        status = "✔" if task['done'] else "✘"
        print(f"{i}. {task['task']} [{status}]")


def remove_task(task_number):
    """Removes a task by its number."""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f'Task "{removed_task["task"]}" removed.')
    else:
        print("Invalid task number.")


def mark_done(task_number):
    """Marks a task as done."""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_tasks(tasks)
        print(f'Task "{tasks[task_number - 1]["task"]}" marked as done.')
    else:
        print("Invalid task number.")


def main():
    parser = argparse.ArgumentParser(description="Simple To-Do List CLI")
    
    subparsers = parser.add_subparsers(dest="command")
    
    # Add a task
    parser_add = subparsers.add_parser('add', help="Add a task")
    parser_add.add_argument('task', type=str, help="The task to add")
    
    # List all tasks
    parser_list = subparsers.add_parser('list', help="List all tasks")
    
    # Remove a task
    parser_remove = subparsers.add_parser('remove', help="Remove a task")
    parser_remove.add_argument('number', type=int, help="Task number to remove")
    
    # Mark a task as done
    parser_done = subparsers.add_parser('done', help="Mark task as done")
    parser_done.add_argument('number', type=int, help="Task number to mark as done")
    
    args = parser.parse_args()

    # Call the appropriate function based on the command
    if args.command == "add":
        add_task(args.task)
    elif args.command == "list":
        list_tasks()
    elif args.command == "remove":
        remove_task(args.number)
    elif args.command == "done":
        mark_done(args.number)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
