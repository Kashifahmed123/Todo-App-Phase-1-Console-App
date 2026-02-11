"""Contract tests for the list command."""


from src.services.task_manager import TaskManager
from src.cli.commands import add_task_handler, list_tasks_handler


def test_list_command_contract(task_manager):
    """Test that the list command handler follows the expected contract."""
    # Add a task first
    add_task_handler(task_manager, "Test Task 1", "Description 1")
    add_task_handler(task_manager, "Test Task 2", "Description 2")

    # Test listing tasks
    result = list_tasks_handler(task_manager)

    assert result is not None
    assert isinstance(result, list)
    assert len(result) == 2

    # Check that the tasks have expected properties
    for task in result:
        assert hasattr(task, 'id')
        assert hasattr(task, 'title')
        assert hasattr(task, 'description')
        assert hasattr(task, 'status')
        assert hasattr(task, 'created_at')
        assert hasattr(task, 'updated_at')


def test_list_command_empty(task_manager):
    """Test that the list command works when there are no tasks."""
    result = list_tasks_handler(task_manager)

    assert result is not None
    assert isinstance(result, list)
    assert len(result) == 0