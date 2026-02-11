# Data Model: Python In-Memory Todo CLI App

**Feature**: Python In-Memory Todo CLI App | **Date**: 2026-02-06

## Entities

### Task
**Description**: Represents a single todo item that can be managed by the application

**Fields**:
- `id: str` - Unique identifier for the task (auto-generated)
- `title: str` - Mandatory title of the task (min length: 1 character)
- `description: Optional[str]` - Optional description of the task (nullable)
- `status: TaskStatus` - Current status of the task (Pending or Complete)
- `created_at: datetime` - Timestamp when the task was created
- `updated_at: datetime` - Timestamp when the task was last modified

**Validation Rules**:
- Title must be at least 1 character long
- ID must be unique across all tasks
- Status must be either 'PENDING' or 'COMPLETE'

**State Transitions**:
- From 'PENDING' to 'COMPLETE' when marked as complete
- From 'COMPLETE' to 'PENDING' when marked as incomplete

### TaskStatus Enum
**Description**: Enumeration of possible statuses for a task

**Values**:
- `PENDING` - Task has not been completed
- `COMPLETE` - Task has been completed

## Relationships

### Task Storage
**Description**: In-memory storage structure to hold all tasks

**Structure**:
```python
task_storage: Dict[str, Task] = {}
```

**Access Pattern**:
- Key: Task.id (str)
- Value: Task instance
- Provides O(1) lookup, insertion, and deletion operations

## Data Flow

### Task Creation Flow
1. User provides title (mandatory) and description (optional)
2. System generates unique ID
3. System sets status to 'PENDING'
4. System records created_at timestamp
5. System stores task in task_storage

### Task Update Flow
1. User provides task ID and new title/description
2. System validates existence of task
3. System updates specified fields
4. System updates updated_at timestamp
5. System validates updated task

### Task Deletion Flow
1. User provides task ID
2. System validates existence of task
3. System removes task from storage
4. System returns confirmation

## Constraints

### Uniqueness Constraints
- Task.id must be unique across all stored tasks
- No duplicate IDs allowed

### Data Integrity Constraints
- Task.title cannot be empty
- Task.status must be one of the allowed values (PENDING, COMPLETE)
- Timestamps must be valid datetime objects

### Storage Constraints
- All tasks stored in-memory only (no persistence)
- Data cleared when application terminates
- No external storage dependencies