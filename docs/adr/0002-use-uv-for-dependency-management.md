# ADR-0002: Use `uv` for Dependency Management

## Status

Accepted

## Date

2026-07-11

## Context

AI Developer OS requires a modern, fast, and reproducible dependency management solution. The project will be developed over a long period, involve multiple environments, and eventually include CI/CD pipelines and containerized deployments.

The chosen tool should simplify dependency management while ensuring consistent environments across development, testing, and production.

## Decision

Use **uv** as the project's dependency and virtual environment manager.

The project will use:

- `pyproject.toml` for project metadata and dependency definitions.
- `uv.lock` to lock exact dependency versions.
- `uv` commands for dependency management and project execution.

## Alternatives Considered

### Option 1: uv (Selected)

- Extremely fast dependency resolution.
- Built-in virtual environment management.
- Uses modern Python packaging standards.
- Produces reproducible environments using `uv.lock`.

### Option 2: pip + venv

- Standard Python tooling.
- Requires managing multiple tools manually.
- No built-in dependency locking.

### Option 3: Poetry

- Mature dependency management.
- Supports packaging and publishing.
- More opinionated and slower than `uv` for our use case.

### Option 4: Conda

- Excellent for scientific computing.
- Larger ecosystem than required for a backend SaaS application.

## Consequences

### Positive

- Faster dependency installation.
- Reproducible environments across all stages.
- Simpler developer workflow.
- Modern Python tooling.

### Negative

- Smaller ecosystem compared to traditional tools.
- Team members unfamiliar with `uv` may require a short onboarding.

## Related Documents

- docs/PROJECT_CONTEXT.md
- docs/progress/MASTER_TRACKER.md
- docs/learning/01-modern-python-project-management.md