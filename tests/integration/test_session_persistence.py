"""Integration tests for session persistence of tasks in memory."""


from src.services.task_manager import TaskManager, TaskStatus
from src.cli.commands import (
    add_task_handler,
    list_tasks_handler,
    update_task_handler,
    delete_task_handler,
    complete_task_handler,
    incomplete_task_handler
)


def test_session_consistency(task_manager):
    """Test that tasks remain accessible and modifiable throughout a CLI session."""
    # Add several tasks in the "session"
    task1 = add_task_handler(task_manager, "Session Task 1", "Description 1")
    task2 = add_task_handler(task_manager, "Session Task 2", "Description 2")
    task3 = add_task_handler(task_manager, "Session Task 3", "Description 3")

    assert task1 is not None
    assert task2 is not None
    assert task3 is not None

    # Verify all tasks exist at the beginning
    initial_list = list_tasks_handler(task_manager)
    assert len(initial_list) == 3
    initial_ids = {task.id for task in initial_list}
    assert task1.id in initial_ids
    assert task2.id in initial_ids
    assert task3.id in initial_ids

    # Perform operations on tasks during the "session"
    updated_task = update_task_handler(task_manager, task1.id, "Updated Session Task 1")
    assert updated_task is not None
    assert updated_task.title == "Updated Session Task 1"

    complete_result = complete_task_handler(task_manager, task2.id)
    assert complete_result is True

    # Verify all tasks are still accessible after operations
    mid_session_list = list_tasks_handler(task_manager)
    assert len(mid_session_list) == 3

    # Find the updated task
    updated_found = next((t for t in mid_session_list if t.id == task1.id), None)
    assert updated_found is not None
    assert updated_found.title == "Updated Session Task 1"

    # Find the completed task
    completed_found = next((t for t in mid_session_list if t.id == task2.id), None)
    assert completed_found is not None
    assert completed_found.status == TaskStatus.COMPLETE

    # Perform more operations
    delete_result = delete_task_handler(task_manager, task3.id)
    assert delete_result is True

    # Verify state after delete
    final_list = list_tasks_handler(task_manager)
    assert len(final_list) == 2

    # Ensure the correct tasks remain
    final_ids = {task.id for task in final_list}
    assert task1.id in final_ids  # Updated task remains
    assert task2.id in final_ids  # Completed task remains
    assert task3.id not in final_ids  # Deleted task is gone


def test_id_consistency_throughout_session(task_manager):
    """Test that task IDs remain consistent throughout the session."""
    # Add a task
    original_task = add_task_handler(task_manager, "Persistent Task", "Will undergo operations")

    assert original_task is not None
    original_id = original_task.id

    # Perform multiple operations and verify ID stays the same
    # Update
    updated_task = update_task_handler(task_manager, original_id, "Updated Title")
    assert updated_task is not None
    assert updated_task.id == original_id  # ID should remain the same

    # Mark as complete
    complete_result = complete_task_handler(task_manager, original_id)
    assert complete_result is True

    # Verify the task still has the same ID after being marked complete
    completed_task = task_manager.get_task_by_id(original_id)
    assert completed_task is not None
    assert completed_task.id == original_id
    assert completed_task.status == TaskStatus.COMPLETE

    # Mark as incomplete
    incomplete_result = incomplete_task_handler(task_manager, original_id)
    assert incomplete_result is True

    # Verify the task still has the same ID after being marked incomplete
    back_to_pending = task_manager.get_task_by_id(original_id)
    assert back_to_pending is not None
    assert back_to_pending.id == original_id
    assert back_to_pending.status == TaskStatus.PENDING


def test_operation_order_independence(task_manager):
    """Test that operations can be performed in different orders without breaking."""
    # Add a task
    task = add_task_handler(task_manager, "Order Independence Task", "Testing different operation orders")

    assert task is not None
    task_id = task.id

    # First sequence: update, then complete
    updated_task = update_task_handler(task_manager, task_id, "Updated for Sequence 1")
    assert updated_task is not None

    complete_result = complete_task_handler(task_manager, task_id)
    assert complete_result is True

    # Reset to pending
    incomplete_result = incomplete_task_handler(task_manager, task_id)
    assert incomplete_result is True

    # Second sequence: complete, then update
    complete_again_result = complete_task_handler(task_manager, task_id)
    assert complete_again_result is True

    updated_after_complete = update_task_handler(task_manager, task_id, "Updated After Complete")
    assert updated_after_complete is not None

    # Verify final state
    final_task = task_manager.get_task_by_id(task_id)
    assert final_task is not None
    assert final_task.title == "Updated After Complete"
    # At this point the task should be complete from the previous complete command