"""Command handlers for the Todo CLI application."""

from typing import List, Optional
from ..models.task import Task, TaskStatus
from ..services.task_manager import TaskManager


def add_task_handler(task_manager: TaskManager, title: str, description: Optional[str] = None) -> Optional[Task]:
    """Handle the add task command."""
    try:
        task = task_manager.add_task(title, description)
        return task
    except ValueError as e:
        print(f"Error: {e}")
        return None


def list_tasks_handler(task_manager: TaskManager) -> Optional[List[Task]]:
    """Handle the list tasks command."""
    try:
        tasks = task_manager.get_all_tasks()
        return tasks
    except Exception as e:
        print(f"Error listing tasks: {e}")
        return None


def update_task_handler(
    task_manager: TaskManager,
    task_id: str,
    title: Optional[str] = None,
    description: Optional[str] = None
) -> Optional[Task]:
    """Handle the update task command."""
    try:
        task = task_manager.update_task(task_id, title, description)
        return task
    except ValueError as e:
        print(f"Error: {e}")
        return None


def delete_task_handler(task_manager: TaskManager, task_id: str) -> bool:
    """Handle the delete task command."""
    try:
        success = task_manager.delete_task(task_id)
        return success
    except Exception as e:
        print(f"Error deleting task: {e}")
        return False


def complete_task_handler(task_manager: TaskManager, task_id: str) -> Optional[bool]:
    """Handle the complete task command - ensure task status is COMPLETE."""
    try:
        result = task_manager.set_task_complete(task_id)
        return result if result else None
    except Exception as e:
        print(f"Error completing task: {e}")
        return None


def incomplete_task_handler(task_manager: TaskManager, task_id: str) -> Optional[bool]:
    """Handle the incomplete task command - ensure task status is PENDING."""
    try:
        result = task_manager.set_task_incomplete(task_id)
        return result if result else None
    except Exception as e:
        print(f"Error marking task as incomplete: {e}")
        return None