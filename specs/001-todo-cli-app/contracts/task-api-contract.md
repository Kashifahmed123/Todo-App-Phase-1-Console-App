# Task API Contract: Python In-Memory Todo CLI App

**Feature**: Python In-Memory Todo CLI App | **Date**: 2026-02-06

## CLI Command Interface

### Add Task Command
**Command**: `todo add <title> [--description DESCRIPTION]`

**Input Parameters**:
- `<title>` (required): String, minimum 1 character
- `--description` (optional): String, nullable

**Output**:
- Success: JSON object with task details including ID
- Error: Error message with status code

**Example**:
```bash
todo add "Buy groceries" --description "Milk, bread, eggs"
```

**Expected Response**:
```json
{
  "id": "task_12345",
  "title": "Buy groceries",
  "description": "Milk, bread, eggs",
  "status": "PENDING",
  "created_at": "2026-02-06T10:00:00",
  "updated_at": "2026-02-06T10:00:00"
}
```

### View All Tasks Command
**Command**: `todo list`

**Input Parameters**: None

**Output**:
- Success: Array of task objects
- Error: Error message with status code

**Example**:
```bash
todo list
```

**Expected Response**:
```json
[
  {
    "id": "task_12345",
    "title": "Buy groceries",
    "description": "Milk, bread, eggs",
    "status": "PENDING",
    "created_at": "2026-02-06T10:00:00",
    "updated_at": "2026-02-06T10:00:00"
  },
  {
    "id": "task_12346",
    "title": "Walk the dog",
    "description": null,
    "status": "COMPLETE",
    "created_at": "2026-02-06T09:00:00",
    "updated_at": "2026-02-06T09:30:00"
  }
]
```

### Update Task Command
**Command**: `todo update <id> [--title TITLE] [--description DESCRIPTION]`

**Input Parameters**:
- `<id>` (required): String, task identifier
- `--title` (optional): String, minimum 1 character
- `--description` (optional): String, nullable

**Output**:
- Success: Updated task object
- Error: Error message with status code

**Example**:
```bash
todo update task_12345 --title "Buy weekly groceries"
```

**Expected Response**:
```json
{
  "id": "task_12345",
  "title": "Buy weekly groceries",
  "description": "Milk, bread, eggs",
  "status": "PENDING",
  "created_at": "2026-02-06T10:00:00",
  "updated_at": "2026-02-06T10:15:00"
}
```

### Delete Task Command
**Command**: `todo delete <id>`

**Input Parameters**:
- `<id>` (required): String, task identifier

**Output**:
- Success: Confirmation message with deleted task ID
- Error: Error message with status code

**Example**:
```bash
todo delete task_12345
```

**Expected Response**:
```json
{
  "message": "Task deleted successfully",
  "id": "task_12345"
}
```

### Mark Task Complete Command
**Command**: `todo complete <id>`

**Input Parameters**:
- `<id>` (required): String, task identifier

**Output**:
- Success: Updated task object with status changed to COMPLETE
- Error: Error message with status code

**Example**:
```bash
todo complete task_12345
```

**Expected Response**:
```json
{
  "id": "task_12345",
  "title": "Buy weekly groceries",
  "description": "Milk, bread, eggs",
  "status": "COMPLETE",
  "created_at": "2026-02-06T10:00:00",
  "updated_at": "2026-02-06T10:20:00"
}
```

### Mark Task Incomplete Command
**Command**: `todo incomplete <id>`

**Input Parameters**:
- `<id>` (required): String, task identifier

**Output**:
- Success: Updated task object with status changed to PENDING
- Error: Error message with status code

**Example**:
```bash
todo incomplete task_12345
```

**Expected Response**:
```json
{
  "id": "task_12345",
  "title": "Buy weekly groceries",
  "description": "Milk, bread, eggs",
  "status": "PENDING",
  "created_at": "2026-02-06T10:00:00",
  "updated_at": "2026-02-06T10:25:00"
}
```

## Error Handling

### Common Error Responses
```json
{
  "error": "Error message describing the issue",
  "status_code": 400,
  "request_id": "unique_request_identifier"
}
```

### Error Codes
- `400`: Bad Request (malformed input)
- `404`: Not Found (task ID does not exist)
- `422`: Unprocessable Entity (validation failed)
- `500`: Internal Server Error (unexpected error)