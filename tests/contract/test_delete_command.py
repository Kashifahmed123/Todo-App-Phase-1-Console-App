"""Contract tests for the delete command."""


from src.services.task_manager import TaskManager
from src.cli.commands import add_task_handler, delete_task_handler, list_tasks_handler


def test_delete_command_contract(task_manager):
    """Test that the delete command handler follows the expected contract."""
    # Add a task first
    original_task = add_task_handler(task_manager, "Test Title", "Test Description")

    assert original_task is not None

    # Verify task exists
    tasks_before = list_tasks_handler(task_manager)
    assert len(tasks_before) == 1

    # Delete the task
    result = delete_task_handler(task_manager, original_task.id)

    assert result is True

    # Verify task no longer exists
    tasks_after = list_tasks_handler(task_manager)
    assert len(tasks_after) == 0


def test_delete_command_nonexistent_task(task_manager):
    """Test that the delete command handles nonexistent tasks properly."""
    result = delete_task_handler(task_manager, "nonexistent-id")

    assert result is False


def test_delete_multiple_tasks(task_manager):
    """Test deleting multiple tasks."""
    # Add multiple tasks
    task1 = add_task_handler(task_manager, "Task 1", "Desc 1")
    task2 = add_task_handler(task_manager, "Task 2", "Desc 2")
    task3 = add_task_handler(task_manager, "Task 3", "Desc 3")

    assert task1 is not None
    assert task2 is not None
    assert task3 is not None

    # Verify all tasks exist
    tasks_before = list_tasks_handler(task_manager)
    assert len(tasks_before) == 3

    # Delete one task
    result = delete_task_handler(task_manager, task2.id)

    assert result is True

    # Verify only two tasks remain
    tasks_after = list_tasks_handler(task_manager)
    assert len(tasks_after) == 2

    # Verify correct task was deleted
    remaining_ids = [t.id for t in tasks_after]
    assert task2.id not in remaining_ids
    assert task1.id in remaining_ids
    assert task3.id in remaining_ids