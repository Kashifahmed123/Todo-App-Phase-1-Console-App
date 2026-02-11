"""Contract tests for the add command."""

import json
from src.services.task_manager import TaskManager
from src.cli.commands import add_task_handler


def test_add_command_contract(task_manager):
    """Test that the add command handler follows the expected contract."""
    # Test successful task addition
    result = add_task_handler(task_manager, "Test Title", "Test Description")

    assert result is not None
    assert hasattr(result, 'id')
    assert hasattr(result, 'title')
    assert hasattr(result, 'description')
    assert hasattr(result, 'status')
    assert hasattr(result, 'created_at')
    assert hasattr(result, 'updated_at')

    assert result.title == "Test Title"
    assert result.description == "Test Description"


def test_add_command_contract_without_description(task_manager):
    """Test that the add command works without a description."""
    result = add_task_handler(task_manager, "Test Title")

    assert result is not None
    assert result.title == "Test Title"
    assert result.description is None


def test_add_command_contract_invalid_title(task_manager):
    """Test that the add command handles invalid titles properly."""
    result = add_task_handler(task_manager, "")

    assert result is None

    result = add_task_handler(task_manager, "   ")

    assert result is None