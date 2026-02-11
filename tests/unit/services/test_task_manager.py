"""Unit tests for the TaskManager service."""

import pytest
from datetime import datetime
from src.services.task_manager import TaskManager
from src.models.task import Task, TaskStatus


def test_task_manager_initialization(task_manager):
    """Test that TaskManager initializes with empty storage."""
    tasks = task_manager.get_all_tasks()
    assert len(tasks) == 0


def test_add_task_success(task_manager):
    """Test adding a task successfully."""
    task = task_manager.add_task("Test Task", "Test Description")

    assert task is not None
    assert task.title == "Test Task"
    assert task.description == "Test Description"
    assert task.status == TaskStatus.PENDING
    assert isinstance(task.created_at, datetime)
    assert isinstance(task.updated_at, datetime)


def test_add_task_without_description(task_manager):
    """Test adding a task without description."""
    task = task_manager.add_task("Test Task")

    assert task is not None
    assert task.title == "Test Task"
    assert task.description is None


def test_add_task_empty_title(task_manager):
    """Test that adding a task with empty title raises ValueError."""
    with pytest.raises(ValueError, match="Task title cannot be empty"):
        task_manager.add_task("")

    with pytest.raises(ValueError, match="Task title cannot be empty"):
        task_manager.add_task("   ")


def test_get_all_tasks(task_manager):
    """Test retrieving all tasks."""
    task1 = task_manager.add_task("Task 1", "Description 1")
    task2 = task_manager.add_task("Task 2", "Description 2")

    all_tasks = task_manager.get_all_tasks()

    assert len(all_tasks) == 2
    task_ids = {t.id for t in all_tasks}
    assert task1.id in task_ids
    assert task2.id in task_ids


def test_get_task_by_id(task_manager):
    """Test retrieving a specific task by ID."""
    task = task_manager.add_task("Test Task", "Test Description")
    retrieved_task = task_manager.get_task_by_id(task.id)

    assert retrieved_task is not None
    assert retrieved_task.id == task.id
    assert retrieved_task.title == task.title


def test_get_task_by_id_nonexistent(task_manager):
    """Test retrieving a nonexistent task returns None."""
    retrieved_task = task_manager.get_task_by_id("nonexistent-id")

    assert retrieved_task is None


def test_update_task_title(task_manager):
    """Test updating a task's title."""
    task = task_manager.add_task("Original Title", "Original Description")
    updated_task = task_manager.update_task(task.id, title="Updated Title")

    assert updated_task is not None
    assert updated_task.title == "Updated Title"
    assert updated_task.description == "Original Description"


def test_update_task_description(task_manager):
    """Test updating a task's description."""
    task = task_manager.add_task("Original Title", "Original Description")
    updated_task = task_manager.update_task(task.id, description="Updated Description")

    assert updated_task is not None
    assert updated_task.title == "Original Title"
    assert updated_task.description == "Updated Description"


def test_update_task_both_fields(task_manager):
    """Test updating both title and description."""
    task = task_manager.add_task("Original Title", "Original Description")
    updated_task = task_manager.update_task(task.id, title="Updated Title", description="Updated Description")

    assert updated_task is not None
    assert updated_task.title == "Updated Title"
    assert updated_task.description == "Updated Description"


def test_update_task_nonexistent(task_manager):
    """Test updating a nonexistent task returns None."""
    updated_task = task_manager.update_task("nonexistent-id", title="New Title")

    assert updated_task is None


def test_update_task_empty_title(task_manager):
    """Test that updating with empty title raises ValueError."""
    task = task_manager.add_task("Original Title", "Original Description")

    with pytest.raises(ValueError, match="Task title cannot be empty"):
        task_manager.update_task(task.id, title="")


def test_delete_task_success(task_manager):
    """Test deleting a task successfully."""
    task = task_manager.add_task("Test Task", "Test Description")
    result = task_manager.delete_task(task.id)

    assert result is True

    # Verify task is gone
    retrieved_task = task_manager.get_task_by_id(task.id)
    assert retrieved_task is None


def test_delete_task_nonexistent(task_manager):
    """Test deleting a nonexistent task returns False."""
    result = task_manager.delete_task("nonexistent-id")

    assert result is False


def test_toggle_task_status_pending_to_complete(task_manager):
    """Test toggling task status from PENDING to COMPLETE."""
    task = task_manager.add_task("Test Task", "Test Description")
    assert task.status == TaskStatus.PENDING

    new_status = task_manager.toggle_task_status(task.id)

    assert new_status == TaskStatus.COMPLETE

    # Verify the task status was updated
    updated_task = task_manager.get_task_by_id(task.id)
    assert updated_task.status == TaskStatus.COMPLETE


def test_toggle_task_status_complete_to_pending(task_manager):
    """Test toggling task status from COMPLETE to PENDING."""
    task = task_manager.add_task("Test Task", "Test Description")

    # First toggle to COMPLETE
    task_manager.toggle_task_status(task.id)

    # Second toggle back to PENDING
    new_status = task_manager.toggle_task_status(task.id)

    assert new_status == TaskStatus.PENDING

    # Verify the task status was updated
    updated_task = task_manager.get_task_by_id(task.id)
    assert updated_task.status == TaskStatus.PENDING


def test_toggle_task_status_nonexistent(task_manager):
    """Test toggling status of nonexistent task returns None."""
    result = task_manager.toggle_task_status("nonexistent-id")

    assert result is None


def test_task_timestamps_update(task_manager):
    """Test that updated_at timestamp changes on updates."""
    task = task_manager.add_task("Test Task", "Test Description")
    original_updated_at = task.updated_at

    # Small delay to ensure timestamp difference
    import time
    time.sleep(0.01)

    # Update the task
    updated_task = task_manager.update_task(task.id, title="Updated Title")

    assert updated_task.updated_at > original_updated_at