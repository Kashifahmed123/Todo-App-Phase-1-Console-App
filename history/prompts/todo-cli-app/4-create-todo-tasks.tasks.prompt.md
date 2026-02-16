---
id: 4
title: create-todo-tasks
stage: tasks
date: 2026-02-06
surface: agent
model: Claude Sonnet 4.5
feature: todo-cli-app
branch: 001-todo-cli-app
user: user
command: /sp.tasks
labels: [tasks, todo-app, python, cli]
links:
  spec: specs/001-todo-cli-app/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/001-todo-cli-app/tasks.md
tests:
---
## Prompt

# Tasks: Phase I - In-Memory Todo CLI

## Phase A: Foundation & Models
- [ ] **Task 1: Define Data Models**
  - **Description:** Create `Task` dataclass in `src/models.py`.
  - **Lineage:** Spec Section 2 (Attributes), Plan Section 1.
  - **Acceptance:** `Task` object can be instantiated with title, description, and status.
- [ ] **Task 2: Initialize TodoManager**
  - **Description:** Create `TodoManager` class in `src/manager.py` with an internal dictionary for storage.
  - **Lineage:** Plan Section 3 (Decision: Option B).
  - **Acceptance:** `TodoManager` exists with an empty `tasks` attribute.

## Phase B: Core Logic Implementation (The 5 Features)
- [ ] **Task 3: Add Task Logic**
  - **Description:** Implement `add_task` method with auto-incrementing ID.
  - **Lineage:** Spec Section 2 (Add).
  - **Acceptance:** Calling `add_task` increases the task count by 1.
- [ ] **Task 4: View & Toggle Logic**
  - **Description:** Implement `get_all_tasks` and `toggle_status` methods.
  - **Lineage:** Spec Section 2 (View, Mark Complete).
  - **Acceptance:** Status flips between Pending and Complete for a valid ID.
- [ ] **Task 5: Update & Delete Logic**
  - **Description:** Implement `update_task` and `delete_task` methods.
  - **Lineage:** Spec Section 2 (Update, Delete).
  - **Acceptance:** Deleting a task removes it from the internal dictionary completely.

## Phase C: Interface & Integration
- [ ] **Task 6: Build CLI Menu Loop**
  - **Description:** Create a while-loop interface in `src/main.py` to handle user input.
  - **Lineage:** Plan Section 3 (Interaction).
  - **Acceptance:** User can navigate between all 5 options via terminal input.
- [ ] **Checkpoint: Phase I Final Review**
  - **Description:** Manual walkthrough of the full task lifecycle.
  - **Acceptance:** User can Add, View, Update, Mark Complete, and Delete in one execution.

## Response snapshot

I've analyzed the user's input and the existing design documents to create a comprehensive task breakdown for the Python In-Memory Todo CLI App. The tasks.md file includes:

1. Phase 1: Setup tasks for project initialization
2. Phase 2: Foundational tasks for core infrastructure
3. Phase 3: User Story 1 (P1 priority) - CLI Task Management
4. Phase 4: User Story 2 (P2 priority) - Task Lifecycle Operations
5. Phase 5: User Story 3 (P3 priority) - Persistent Session Experience
6. Phase 6: Polish and cross-cutting concerns

Each task follows the required format with checkboxes, task IDs, story labels where appropriate, and parallelism indicators. The tasks are organized to enable independent implementation and testing of each user story, following the Spec-Driven Development methodology.

## Outcome

- ✅ Impact: Created comprehensive task breakdown for todo CLI app
- 🧪 Tests: Included test tasks for each user story
- 📁 Files: specs/001-todo-cli-app/tasks.md
- 🔁 Next prompts: Begin implementation of tasks
- 🧠 Reflection: Successfully organized tasks by user story with proper dependencies

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS - all tasks properly formatted
- Prompt variant (if applicable): task generation from design docs
- Next experiment (smallest change to try): begin task implementation