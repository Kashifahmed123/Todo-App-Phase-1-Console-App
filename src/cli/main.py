"""Entry point for the Todo CLI application."""

import argparse
import sys
from .commands import (
    add_task_handler,
    list_tasks_handler,
    update_task_handler,
    delete_task_handler,
    complete_task_handler,
    incomplete_task_handler
)
from ..services.task_manager import TaskManager


def create_parser() -> argparse.ArgumentParser:
    """Create the argument parser for the CLI application."""
    parser = argparse.ArgumentParser(
        description="A simple CLI-based todo application with in-memory storage"
    )

    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('title', help='Task title')
    add_parser.add_argument('--description', '-d', help='Task description')

    # List command
    list_parser = subparsers.add_parser('list', help='List all tasks')

    # Update command
    update_parser = subparsers.add_parser('update', help='Update a task')
    update_parser.add_argument('id', help='Task ID')
    update_parser.add_argument('--title', help='New task title')
    update_parser.add_argument('--description', '-d', help='New task description')

    # Delete command
    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('id', help='Task ID')

    # Complete command
    complete_parser = subparsers.add_parser('complete', help='Mark task as complete')
    complete_parser.add_argument('id', help='Task ID')

    # Incomplete command
    incomplete_parser = subparsers.add_parser('incomplete', help='Mark task as incomplete')
    incomplete_parser.add_argument('id', help='Task ID')

    return parser


def main() -> None:
    """Main entry point for the CLI application."""
    parser = create_parser()
    args = parser.parse_args()

    # Create a shared task manager instance
    task_manager = TaskManager()

    if args.command == 'add':
        result = add_task_handler(task_manager, args.title, args.description)
        if result:
            print(f"Task added: {result.id}")
            print(result)
        else:
            print("Failed to add task")
            sys.exit(1)
    elif args.command == 'list':
        result = list_tasks_handler(task_manager)
        if result is not None:
            if result:
                for task in result:
                    print(f"ID: {task.id}")
                    print(f"Title: {task.title}")
                    print(f"Description: {task.description or 'None'}")
                    print(f"Status: {task.status.value}")
                    print(f"Created: {task.created_at}")
                    print(f"Updated: {task.updated_at}")
                    print("-" * 40)
            else:
                print("No tasks found.")
        else:
            print("Failed to list tasks")
            sys.exit(1)
    elif args.command == 'update':
        result = update_task_handler(task_manager, args.id, args.title, args.description)
        if result:
            print(f"Task updated: {result.id}")
        else:
            print(f"Task with ID {args.id} not found")
            sys.exit(1)
    elif args.command == 'delete':
        result = delete_task_handler(task_manager, args.id)
        if result:
            print(f"Task with ID {args.id} deleted successfully")
        else:
            print(f"Task with ID {args.id} not found")
            sys.exit(1)
    elif args.command == 'complete':
        result = complete_task_handler(task_manager, args.id)
        if result:
            print(f"Task with ID {args.id} marked as complete")
        else:
            print(f"Task with ID {args.id} not found")
            sys.exit(1)
    elif args.command == 'incomplete':
        result = incomplete_task_handler(task_manager, args.id)
        if result:
            print(f"Task with ID {args.id} marked as incomplete")
        elif result is None:  # Task not found
            print(f"Task with ID {args.id} not found")
            sys.exit(1)
        else:  # Some other error occurred
            print(f"Failed to mark task with ID {args.id} as incomplete")
            sys.exit(1)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()