"""Task management service for the Todo CLI application."""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional
from ..models.task import Task, TaskStatus, generate_unique_id


class TaskManager:
    """Manages tasks with persistent JSON storage."""

    def __init__(self, storage_file: Optional[str] = None) -> None:
        """Initialize the task manager with persistent storage."""
        if storage_file is None:
            # Default storage location in project root
            storage_file = os.path.join(os.getcwd(), '.todo_data.json')

        self.storage_file = storage_file
        self._tasks: Dict[str, Task] = {}
        self._load_tasks()

    def _load_tasks(self) -> None:
        """Load tasks from JSON file."""
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for task_data in data:
                        task = Task(
                            id=task_data['id'],
                            title=task_data['title'],
                            description=task_data.get('description'),
                            status=TaskStatus[task_data['status']],
                            created_at=datetime.fromisoformat(task_data['created_at']),
                            updated_at=datetime.fromisoformat(task_data['updated_at'])
                        )
                        self._tasks[task.id] = task
            except (json.JSONDecodeError, KeyError, ValueError) as e:
                # If file is corrupted, start fresh
                print(f"Warning: Could not load tasks from {self.storage_file}: {e}")
                self._tasks = {}

    def _save_tasks(self) -> None:
        """Save tasks to JSON file."""
        try:
            data = []
            for task in self._tasks.values():
                data.append({
                    'id': task.id,
                    'title': task.title,
                    'description': task.description,
                    'status': task.status.name,
                    'created_at': task.created_at.isoformat(),
                    'updated_at': task.updated_at.isoformat()
                })

            with open(self.storage_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Warning: Could not save tasks to {self.storage_file}: {e}")

    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        """Add a new task to the storage."""
        if not title.strip():
            raise ValueError("Task title cannot be empty")

        task_id = generate_unique_id()
        task = Task(
            id=task_id,
            title=title.strip(),
            description=description,
            status=TaskStatus.PENDING,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )

        self._tasks[task_id] = task
        self._save_tasks()
        return task

    def get_all_tasks(self) -> List[Task]:
        """Retrieve all tasks from storage."""
        return list(self._tasks.values())

    def get_task_by_id(self, task_id: str) -> Optional[Task]:
        """Retrieve a specific task by its ID."""
        return self._tasks.get(task_id)

    def update_task(self, task_id: str, title: Optional[str] = None, description: Optional[str] = None) -> Optional[Task]:
        """Update an existing task with new information."""
        if task_id not in self._tasks:
            return None

        task = self._tasks[task_id]

        if title is not None:
            if not title.strip():
                raise ValueError("Task title cannot be empty")
            task.title = title.strip()

        if description is not None:
            task.description = description

        task.updated_at = datetime.now()
        self._save_tasks()
        return task

    def delete_task(self, task_id: str) -> bool:
        """Delete a task from storage."""
        if task_id in self._tasks:
            del self._tasks[task_id]
            self._save_tasks()
            return True
        return False

    def toggle_task_status(self, task_id: str) -> Optional[TaskStatus]:
        """Toggle the status of a task between PENDING and COMPLETE."""
        if task_id not in self._tasks:
            return None

        task = self._tasks[task_id]
        if task.status == TaskStatus.PENDING:
            task.status = TaskStatus.COMPLETE
        else:
            task.status = TaskStatus.PENDING

        task.updated_at = datetime.now()
        self._save_tasks()
        return task.status

    def set_task_complete(self, task_id: str) -> bool:
        """Set a task status to COMPLETE."""
        if task_id not in self._tasks:
            return False

        task = self._tasks[task_id]
        task.status = TaskStatus.COMPLETE
        task.updated_at = datetime.now()
        self._save_tasks()
        return True

    def set_task_incomplete(self, task_id: str) -> bool:
        """Set a task status to PENDING."""
        if task_id not in self._tasks:
            return False

        task = self._tasks[task_id]
        task.status = TaskStatus.PENDING
        task.updated_at = datetime.now()
        self._save_tasks()
        return True