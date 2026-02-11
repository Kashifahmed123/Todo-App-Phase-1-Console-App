# Quickstart Guide: Python In-Memory Todo CLI App

**Feature**: Python In-Memory Todo CLI App | **Date**: 2026-02-06

## Prerequisites

- Python 3.13+
- `uv` package manager installed

## Installation

1. Clone or create the project directory
2. Install dependencies using uv:
```bash
uv venv  # Creates a virtual environment
uv pip install -e .  # Installs the package in development mode
```

## Project Structure

```
todo-cli-app/
├── src/
│   ├── __init__.py
│   ├── models/
│   │   └── task.py
│   ├── services/
│   │   └── task_manager.py
│   └── cli/
│       ├── main.py
│       └── commands.py
├── tests/
├── pyproject.toml
└── README.md
```

## Running the Application

```bash
python -m src.cli.main --help
```

## Basic Usage Examples

### Add a Task
```bash
python -m src.cli.main add "My new task" --description "Some details about the task"
```

### List All Tasks
```bash
python -m src.cli.main list
```

### Update a Task
```bash
python -m src.cli.main update task_id --title "Updated title" --description "Updated description"
```

### Mark Task as Complete
```bash
python -m src.cli.main complete task_id
```

### Delete a Task
```bash
python -m src.cli.main delete task_id
```

## Development Commands

### Running Tests
```bash
python -m pytest tests/
```

### Type Checking
```bash
python -m mypy src/
```

## Configuration

The application uses in-memory storage by default. No additional configuration is required for basic operation.

## Troubleshooting

- If commands fail, ensure the virtual environment is activated
- Check that Python 3.13+ is installed
- Verify that all dependencies were installed correctly