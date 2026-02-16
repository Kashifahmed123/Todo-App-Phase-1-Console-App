<!--
Sync Impact Report:
- Version change: 1.0.0 → 1.1.0
- Modified principles: Added 5 specific principles for Todo App project
- Added sections: Specific constraints and workflow for Python Todo App
- Removed sections: Template placeholders
- Templates requiring updates: N/A (initial constitution)
- Follow-up TODOs: None
-->

# Todo App Constitution

## Core Principles

### Methodological Integrity
Adhere strictly to Spec-Kit Plus methodology (Spec → Plan → Tasks → Implement). All development follows the SDD approach with formal specifications, architectural planning, and structured task breakdowns before implementation begins.

### Zero Manual Intervention
100% of the codebase must be agent-generated; no manual coding allowed. All changes must be made through the AI assistant to ensure complete traceability and reproducibility of the development process.

### Traceability
Every code change must map back to a specific requirement in the specification. Each function, module, and feature must be directly linked to a documented requirement in the specification document.

### Clean Architecture
Prioritize separation of concerns and high-quality Pythonic patterns. Maintain clear boundaries between different layers of the application (presentation, business logic, data management) following established Python architectural patterns.

### Python 3.13+ Standard
Strictly use Python 3.13+ for all implementations. Follow modern Python syntax, features, and best practices specific to this version, including enhanced type hints, new syntax features, and performance improvements.

### Dependency Management with uv
Use `uv` exclusively for environment and package control. Leverage `uv` for fast dependency resolution, virtual environment management, and consistent package installation across all development environments.

## Additional Constraints
- Language: Strictly Python 3.13+
- Dependency Management: Use `uv` exclusively for environment and package control
- Documentation: Every prompt must generate a Prompt History Record (PHR) per CCR rules
- Code Quality: 100% Type Hint coverage and PEP 8 compliance
- Functionality: Implementation of all 5 core todo operations (add, list, complete, delete, archive)

## Development Workflow
- Spec-Driven Development: Complete specification before any implementation
- Architectural Planning: Document all architectural decisions before coding
- Task Generation: Create detailed, testable tasks from the plan
- Implementation: Execute tasks following red-green-refactor cycles
- Quality Assurance: Each change must pass type checking and code quality validation

## Governance
This constitution governs all development activities for the Todo App project. All team members and AI assistants must comply with these principles. Amendments require explicit documentation and approval through the formal process. Compliance is verified during each development cycle and code review process.

All development activities must align with Spec-Kit Plus methodology and maintain strict adherence to the outlined principles. Deviations require documented justification and approval.

**Version**: 1.1.0 | **Ratified**: 2026-02-06 | **Last Amended**: 2026-02-06