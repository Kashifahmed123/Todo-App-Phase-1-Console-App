# Todo CLI App

A Python 3.13+ command-line todo application with in-memory storage, built following Spec-Driven Development (SDD) methodology.

## Features

- **Add Tasks**: Create tasks with mandatory title and optional description
- **List Tasks**: View all tasks in a formatted list with ID, title, description, and status
- **Update Tasks**: Modify task title or description using task ID
- **Delete Tasks**: Permanently remove tasks from memory
- **Mark Complete/Incomplete**: Toggle task status between PENDING and COMPLETE

## Requirements

- Python 3.13+
- `uv` package manager

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Todo-App
```

2. Create a virtual environment using uv:
```bash
uv venv
```

3. Activate the virtual environment:
```bash
# On Windows
.venv\Scripts\activate

# On macOS/Linux
source .venv/bin/activate
```

4. Install the package in development mode:
```bash
uv pip install -e .
```

## Usage

### Add a Task
```bash
python -m src.cli.main add "Buy groceries" --description "Milk, bread, eggs"
```

### List All Tasks
```bash
python -m src.cli.main list
```

### Update a Task
```bash
python -m src.cli.main update <task-id> --title "Updated title" --description "Updated description"
```

### Mark Task as Complete
```bash
python -m src.cli.main complete <task-id>
```

### Mark Task as Incomplete
```bash
python -m src.cli.main incomplete <task-id>
```

### Delete a Task
```bash
python -m src.cli.main delete <task-id>
```

## Architecture

The application follows clean architecture principles with clear separation of concerns:

- **Models** (`src/models/`): Data structures and enums
- **Services** (`src/services/`): Business logic and task management
- **CLI** (`src/cli/`): Command-line interface and user interaction

## Data Storage

Tasks are stored persistently in a JSON file (`.todo_data.json`) in the project root directory. This means:
- ✅ Tasks persist between command executions
- ✅ Tasks survive application restarts
- ✅ You can backup/restore tasks by copying the JSON file
- ⚠️ The JSON file is excluded from git (see `.gitignore`)

The storage file is automatically created on first use and updated after each operation.

## Testing

Run tests using pytest:
```bash
pytest tests/
```

Test coverage includes:
- Unit tests for models
- Contract tests for CLI commands
- Integration tests for task lifecycle and session persistence

## Development

This project was developed following Spec-Driven Development (SDD) methodology:
1. Specification (`specs/001-todo-cli-app/spec.md`)
2. Implementation Plan (`specs/001-todo-cli-app/plan.md`)
3. Task Breakdown (`specs/001-todo-cli-app/tasks.md`)
4. Implementation

## Type Hints

The codebase maintains 100% type hint coverage for all modules, ensuring type safety and better IDE support.

## License

MIT