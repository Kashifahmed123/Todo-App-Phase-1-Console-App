"""Unit tests for the Task dataclass."""

import pytest
from datetime import datetime
from src.models.task import Task, TaskStatus, generate_unique_id


def test_task_creation():
    """Test that a Task object can be instantiated with title, description, and status."""
    task_id = generate_unique_id()
    task = Task(
        id=task_id,
        title="Test Task",
        description="Test Description",
        status=TaskStatus.PENDING
    )

    assert task.id == task_id
    assert task.title == "Test Task"
    assert task.description == "Test Description"
    assert task.status == TaskStatus.PENDING
    assert isinstance(task.created_at, datetime)
    assert isinstance(task.updated_at, datetime)


def test_task_default_values():
    """Test that Task has proper default values."""
    task_id = generate_unique_id()
    task = Task(id=task_id, title="Test Task")

    assert task.id == task_id
    assert task.title == "Test Task"
    assert task.description is None
    assert task.status == TaskStatus.PENDING
    assert isinstance(task.created_at, datetime)
    assert isinstance(task.updated_at, datetime)


def test_generate_unique_id():
    """Test that unique IDs are generated properly."""
    id1 = generate_unique_id()
    id2 = generate_unique_id()

    assert id1.startswith("task_")
    assert id2.startswith("task_")
    assert len(id1) == len(id2)  # Both should have the same format
    assert id1 != id2  # Should be different