"""Task model for the Todo CLI application."""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional


class TaskStatus(Enum):
    """Enumeration of possible statuses for a task."""

    PENDING = "PENDING"
    COMPLETE = "COMPLETE"


@dataclass
class Task:
    """Represents a single todo item that can be managed by the application."""

    id: str
    title: str
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.PENDING
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)


def generate_unique_id() -> str:
    """Generate a unique ID for a new task."""
    import uuid
    return f"task_{uuid.uuid4().hex[:8]}"