# Research: Python In-Memory Todo CLI App

**Feature**: Python In-Memory Todo CLI App | **Date**: 2026-02-06

## Key Decisions & Rationale

### Decision: Data Storage Structure
- **Problem**: How to store tasks in memory for optimal performance
- **Options Considered**:
  - Option A: List of Dictionaries
  - Option B: Dictionary of Objects (Key = ID)
  - Option C: List of Dataclass instances
- **Selection**: **Option B** (Dictionary of Objects with ID as key)
- **Rationale**: Provides O(1) lookup for Update/Delete/Mark Complete operations by ID, which matches the user requirement to operate on tasks using their unique ID

### Decision: CLI Interaction Pattern
- **Problem**: How to implement CLI interface for task management
- **Options Considered**:
  - Option A: While-loop Menu System
  - Option B: Command-line Arguments Pattern (e.g., `todo add "title"`)
  - Option C: Interactive REPL-style Interface
- **Selection**: **Option B** (Command-line Arguments Pattern)
- **Rationale**: Matches Unix/CLI conventions, easier to automate, and cleaner user experience for command-line applications

### Decision: Data Model Implementation
- **Problem**: How to represent Task data structure
- **Options Considered**:
  - Option A: Dictionary
  - Option B: Named Tuple
  - Option C: Dataclass
  - Option D: Pydantic Model
- **Selection**: **Option C** (Dataclass)
- **Rationale**: Built into Python 3.7+, supports type hints, immutable if needed, and provides clean representation

### Decision: Dependency Management
- **Problem**: How to manage project dependencies and virtual environment
- **Selection**: **uv**
- **Rationale**: As specified in requirements, uv is fast and efficient for Python dependency management

### Decision: Type Hints and Validation
- **Problem**: How to ensure type safety with Python 3.13+
- **Options Considered**:
  - Option A: Basic type hints
  - Option B: Advanced type hints with typing module
  - Option C: Type hints + runtime validation
- **Selection**: **Option B** (Advanced type hints with typing module)
- **Rationale**: As specified in requirements, leveraging Python 3.13+ features for maximum type safety

## Technology Research Findings

### Python 3.13 Features
- `type` statement for type aliases
- Enhanced type checker support
- Improved error messages
- Better performance characteristics

### CLI Framework Options
- **argparse**: Built-in, sufficient for simple CLI
- **click**: More advanced, decorator-based
- **typer**: Modern, type-hint driven CLI
- **Selected**: Will use argparse for simplicity and stdlib compliance

### Testing Framework
- **pytest**: Industry standard for Python testing
- Good fixture support
- Extensive plugin ecosystem
- Selected for testing framework

## Architecture Patterns

### Repository Pattern
- Appropriate for this application
- Separates data access logic from business logic
- Enables easy testing of business logic separately from data operations

### Single Responsibility Principle
- TaskManager handles only task operations
- CLI module handles only user interface
- Models contain only data definitions