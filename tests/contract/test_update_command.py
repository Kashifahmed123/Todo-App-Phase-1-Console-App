"""Contract tests for the update command."""


from src.services.task_manager import TaskManager
from src.cli.commands import add_task_handler, update_task_handler


def test_update_command_contract(task_manager):
    """Test that the update command handler follows the expected contract."""
    # Add a task first
    original_task = add_task_handler(task_manager, "Original Title", "Original Description")

    assert original_task is not None

    # Update the task
    result = update_task_handler(task_manager, original_task.id, "Updated Title", "Updated Description")

    assert result is not None
    assert result.id == original_task.id
    assert result.title == "Updated Title"
    assert result.description == "Updated Description"


def test_update_command_partial_updates(task_manager):
    """Test that the update command works with partial updates."""
    # Add a task first
    original_task = add_task_handler(task_manager, "Original Title", "Original Description")

    assert original_task is not None

    # Update only the title
    result = update_task_handler(task_manager, original_task.id, title="Updated Title Only")

    assert result is not None
    assert result.id == original_task.id
    assert result.title == "Updated Title Only"
    assert result.description == "Original Description"  # Should remain unchanged

    # Update only the description
    result = update_task_handler(task_manager, original_task.id, description="Updated Desc Only")

    assert result is not None
    assert result.id == original_task.id
    assert result.title == "Updated Title Only"  # Should remain unchanged
    assert result.description == "Updated Desc Only"


def test_update_command_nonexistent_task(task_manager):
    """Test that the update command handles nonexistent tasks properly."""
    result = update_task_handler(task_manager, "nonexistent-id", "New Title")

    assert result is None


def test_update_command_invalid_title(task_manager):
    """Test that the update command handles invalid titles properly."""
    # Add a task first
    original_task = add_task_handler(task_manager, "Original Title", "Original Description")

    assert original_task is not None

    # Try to update with empty title
    result = update_task_handler(task_manager, original_task.id, "")

    assert result is None

    # Try to update with whitespace-only title
    result = update_task_handler(task_manager, original_task.id, "   ")

    assert result is None