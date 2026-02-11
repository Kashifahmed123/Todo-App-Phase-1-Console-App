"""Contract tests for the complete command."""


from src.services.task_manager import TaskManager, TaskStatus
from src.cli.commands import add_task_handler, complete_task_handler, list_tasks_handler


def test_complete_command_contract(task_manager):
    """Test that the complete command handler follows the expected contract."""
    # Add a task first (should be PENDING by default)
    original_task = add_task_handler(task_manager, "Test Title", "Test Description")

    assert original_task is not None
    assert original_task.status == TaskStatus.PENDING

    # Complete the task
    result = complete_task_handler(task_manager, original_task.id)

    assert result is True  # Task was found and status is COMPLETE

    # Verify task status is now COMPLETE
    updated_task = task_manager.get_task_by_id(original_task.id)
    assert updated_task is not None
    assert updated_task.status == TaskStatus.COMPLETE


def test_complete_command_nonexistent_task(task_manager):
    """Test that the complete command handles nonexistent tasks properly."""
    result = complete_task_handler(task_manager, "nonexistent-id")

    assert result is None


def test_complete_already_completed_task(task_manager):
    """Test completing a task that's already completed."""
    # Add a task first
    original_task = add_task_handler(task_manager, "Test Title", "Test Description")

    assert original_task is not None
    assert original_task.status == TaskStatus.PENDING

    # Complete the task
    result1 = complete_task_handler(task_manager, original_task.id)

    assert result1 is True

    # Verify task is now complete
    task_after_first_complete = task_manager.get_task_by_id(original_task.id)
    assert task_after_first_complete is not None
    assert task_after_first_complete.status == TaskStatus.COMPLETE

    # Try to complete again
    result2 = complete_task_handler(task_manager, original_task.id)

    # Result should indicate the final state is complete
    assert result2 is True


def test_complete_multiple_tasks(task_manager):
    """Test completing multiple tasks."""
    # Add multiple tasks
    task1 = add_task_handler(task_manager, "Task 1", "Desc 1")
    task2 = add_task_handler(task_manager, "Task 2", "Desc 2")
    task3 = add_task_handler(task_manager, "Task 3", "Desc 3")

    assert task1 is not None
    assert task2 is not None
    assert task3 is not None

    # Complete one task
    result = complete_task_handler(task_manager, task2.id)

    assert result is True

    # Verify tasks have correct states
    all_tasks = list_tasks_handler(task_manager)
    completed_task = next((t for t in all_tasks if t.id == task2.id), None)
    pending_tasks = [t for t in all_tasks if t.id != task2.id]

    assert completed_task is not None
    assert completed_task.status == TaskStatus.COMPLETE

    for task in pending_tasks:
        assert task.status == TaskStatus.PENDING