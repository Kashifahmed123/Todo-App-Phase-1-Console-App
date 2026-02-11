"""Integration tests for the full task lifecycle."""


from src.services.task_manager import TaskManager, TaskStatus
from src.cli.commands import (
    add_task_handler,
    list_tasks_handler,
    update_task_handler,
    delete_task_handler,
    complete_task_handler,
    incomplete_task_handler
)


def test_full_task_lifecycle(task_manager):
    """Test the complete lifecycle of a task through all operations."""
    # Step 1: Add a task
    task = add_task_handler(task_manager, "Buy groceries", "Need to buy milk, bread, eggs")

    assert task is not None
    assert task.title == "Buy groceries"
    assert task.description == "Need to buy milk, bread, eggs"
    assert task.status == TaskStatus.PENDING

    original_id = task.id

    # Step 2: List tasks (should have 1)
    tasks = list_tasks_handler(task_manager)
    assert len(tasks) == 1
    assert tasks[0].id == original_id

    # Step 3: Update the task
    updated_task = update_task_handler(task_manager, original_id, "Buy weekly groceries", "Milk, bread, eggs, fruit")

    assert updated_task is not None
    assert updated_task.id == original_id
    assert updated_task.title == "Buy weekly groceries"
    assert updated_task.description == "Milk, bread, eggs, fruit"

    # Step 4: Mark as complete
    complete_result = complete_task_handler(task_manager, original_id)

    assert complete_result is True

    # Verify the task is now complete
    completed_task = task_manager.get_task_by_id(original_id)
    assert completed_task is not None
    assert completed_task.status == TaskStatus.COMPLETE

    # Step 5: Mark as incomplete again
    incomplete_result = incomplete_task_handler(task_manager, original_id)

    assert incomplete_result is True

    # Verify the task is now pending again
    back_to_pending = task_manager.get_task_by_id(original_id)
    assert back_to_pending is not None
    assert back_to_pending.status == TaskStatus.PENDING

    # Step 6: Delete the task
    delete_result = delete_task_handler(task_manager, original_id)

    assert delete_result is True

    # Verify the task is gone
    final_list = list_tasks_handler(task_manager)
    assert len(final_list) == 0

    # Verify task can't be retrieved
    missing_task = task_manager.get_task_by_id(original_id)
    assert missing_task is None


def test_multiple_tasks_lifecycle(task_manager):
    """Test operations on multiple tasks."""
    # Add multiple tasks
    task1 = add_task_handler(task_manager, "Task 1", "Description 1")
    task2 = add_task_handler(task_manager, "Task 2", "Description 2")
    task3 = add_task_handler(task_manager, "Task 3", "Description 3")

    # Verify all tasks exist
    all_tasks = list_tasks_handler(task_manager)
    assert len(all_tasks) == 3

    # Complete task2
    complete_result = complete_task_handler(task_manager, task2.id)
    assert complete_result is True

    # Update task1
    updated_task1 = update_task_handler(task_manager, task1.id, "Updated Task 1")
    assert updated_task1 is not None
    assert updated_task1.title == "Updated Task 1"

    # Delete task3
    delete_result = delete_task_handler(task_manager, task3.id)
    assert delete_result is True

    # Verify final state
    final_tasks = list_tasks_handler(task_manager)
    assert len(final_tasks) == 2

    # Check that task1 is updated and still pending
    updated_task = next((t for t in final_tasks if t.id == task1.id), None)
    assert updated_task is not None
    assert updated_task.title == "Updated Task 1"

    # Check that task2 is complete
    completed_task = next((t for t in final_tasks if t.id == task2.id), None)
    assert completed_task is not None
    assert completed_task.status == TaskStatus.COMPLETE