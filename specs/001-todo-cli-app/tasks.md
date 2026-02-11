---
description: "Task list for Python In-Memory Todo CLI App implementation"
---

# Tasks: Python In-Memory Todo CLI App

**Input**: Design documents from `/specs/001-todo-cli-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Test tasks included as specified in feature requirements
**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

<!--
  ============================================================================
  IMPORTANT: The tasks below are the actual implementation tasks based on:
  - User stories from spec.md (with their priorities P1, P2, P3...)
  - Feature requirements from plan.md
  - Entities from data-model.md
  - Endpoints from contracts/

  Tasks are organized by user story so each story can be:
  - Implemented independently
  - Tested independently
  - Delivered as an MVP increment

  Each user story includes: Tests (if requested) → Models → Services → CLI → Integration
  ============================================================================
-->

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project directory structure per implementation plan
- [x] T002 [P] Create src/__init__.py file
- [x] T003 [P] Create src/models/__init__.py file
- [x] T004 [P] Create src/services/__init__.py file
- [x] T005 [P] Create src/cli/__init__.py file
- [x] T006 Create pyproject.toml with uv configuration and dependencies

---
## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T007 Create Task dataclass with id, title, description, status, timestamps in src/models/task.py
- [x] T008 Create TaskStatus enum in src/models/task.py
- [x] T009 Create TaskManager class skeleton in src/services/task_manager.py
- [x] T010 Create CLI argument parser in src/cli/main.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - CLI Task Management (Priority: P1) 🎯 MVP

**Goal**: Enable users to add tasks via CLI commands and view them in a formatted list

**Independent Test**: The application allows users to add tasks via CLI commands, view them in a formatted list, and maintain tasks in memory during the session.

### Tests for User Story 1
> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T011 [P] [US1] Create unit test for Task dataclass instantiation in tests/unit/models/test_task.py
- [x] T012 [P] [US1] Create contract test for add command in tests/contract/test_add_command.py
- [x] T013 [P] [US1] Create contract test for list command in tests/contract/test_list_command.py

### Implementation for User Story 1

- [x] T014 [US1] Implement Task creation with auto-generated ID in src/models/task.py
- [x] T015 [US1] Implement add_task method in src/services/task_manager.py
- [x] T016 [US1] Implement get_all_tasks method in src/services/task_manager.py
- [x] T017 [US1] Implement add command handler in src/cli/commands.py
- [x] T018 [US1] Implement list command handler in src/cli/commands.py
- [x] T019 [US1] Integrate command handlers with CLI argument parser in src/cli/main.py
- [x] T020 [US1] Add proper error handling for missing title validation in src/services/task_manager.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---
## Phase 4: User Story 2 - Task Lifecycle Operations (Priority: P2)

**Goal**: Enable users to modify existing tasks, mark them as complete, and remove unwanted tasks

**Independent Test**: The application allows users to update task details, toggle completion status, and delete tasks via CLI commands.

### Tests for User Story 2
> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T021 [P] [US2] Create contract test for update command in tests/contract/test_update_command.py
- [x] T022 [P] [US2] Create contract test for delete command in tests/contract/test_delete_command.py
- [x] T023 [P] [US2] Create contract test for complete command in tests/contract/test_complete_command.py

### Implementation for User Story 2

- [x] T024 [US2] Implement update_task method in src/services/task_manager.py
- [x] T025 [US2] Implement delete_task method in src/services/task_manager.py
- [x] T026 [US2] Implement toggle_task_status method in src/services/task_manager.py
- [x] T027 [US2] Implement update command handler in src/cli/commands.py
- [x] T028 [US2] Implement delete command handler in src/cli/commands.py
- [x] T029 [US2] Implement complete command handler in src/cli/commands.py
- [x] T030 [US2] Implement incomplete command handler in src/cli/commands.py
- [x] T031 [US2] Add validation for non-existent task IDs in src/services/task_manager.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---
## Phase 5: User Story 3 - Persistent Session Experience (Priority: P3)

**Goal**: Ensure tasks persist consistently within a session and provide reliable in-memory management

**Independent Test**: Tasks remain accessible and modifiable throughout the CLI session with consistent ID assignments.

### Tests for User Story 3
> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T032 [P] [US3] Create integration test for task lifecycle in tests/integration/test_task_lifecycle.py
- [x] T033 [P] [US3] Create integration test for session persistence in tests/integration/test_session_persistence.py

### Implementation for User Story 3

- [x] T034 [US3] Implement unique ID generation mechanism in src/models/task.py
- [x] T035 [US3] Add timestamp management (created_at, updated_at) in src/models/task.py
- [x] T036 [US3] Implement comprehensive error handling in src/services/task_manager.py
- [x] T037 [US3] Add validation for all operations in src/services/task_manager.py
- [x] T038 [US3] Improve CLI output formatting for better user experience in src/cli/commands.py
- [x] T039 [US3] Add logging capabilities for operations in src/services/task_manager.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T040 [P] Documentation updates in README.md
- [x] T041 [P] Type hint coverage for all modules in src/
- [x] T042 Code cleanup and refactoring
- [x] T043 [P] Additional unit tests in tests/unit/ (if test coverage is low)
- [x] T044 Performance validation for 100+ tasks
- [x] T045 Run quickstart.md validation

---
## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before CLI handlers
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---
## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---
## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
- Agent-generated only: Follow zero manual intervention principle from constitution
- Traceability: Each task must link back to spec requirement per constitution