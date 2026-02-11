"""Pytest configuration and fixtures for the Todo CLI tests."""

import pytest
import tempfile
import os
from src.services.task_manager import TaskManager


@pytest.fixture
def task_manager():
    """Provide a TaskManager with isolated temporary storage for each test."""
    # Create a temporary file for this test
    temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False)
    temp_file.close()

    # Create TaskManager with the temporary file
    manager = TaskManager(storage_file=temp_file.name)

    yield manager

    # Cleanup: delete the temporary file after the test
    try:
        if os.path.exists(temp_file.name):
            os.unlink(temp_file.name)
    except Exception:
        pass  # Ignore cleanup errors


@pytest.fixture
def temp_storage_file():
    """Provide a temporary storage file path for tests that need direct file access."""
    temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False)
    temp_file.close()

    yield temp_file.name

    # Cleanup
    try:
        if os.path.exists(temp_file.name):
            os.unlink(temp_file.name)
    except Exception:
        pass