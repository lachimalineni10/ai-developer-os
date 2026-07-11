# ADR-0001: Use `app/` as the Application Root

## Status

Accepted

## Date

2026-07-11

## Context

The project required a clear and scalable directory structure for a production-grade FastAPI SaaS application. We evaluated whether to organize the application using the `app/` directory or the Python packaging `src/` layout.

## Decision

Use `app/` as the application root for AI Developer OS.

```
app/
├── api/
├── core/
├── services/
├── models/
├── repositories/
├── middleware/
├── workers/
└── ai/
```

## Alternatives Considered

### Option 1: `app/` (Selected)

- Simple and familiar for FastAPI applications.
- Easy onboarding for new contributors.
- Clear separation between application code and project files.

### Option 2: `src/`

- Better suited for installable Python packages.
- Helps prevent certain import issues.
- Adds unnecessary complexity for this application-focused project.

## Consequences

### Positive

- Simpler project structure.
- Easier development workflow.
- Well suited for a deployable FastAPI backend.

### Negative

- Requires disciplined import practices.
- Not intended for publishing as a reusable Python package.

## Related Documents

- docs/PROJECT_CONTEXT.md
- docs/progress/MASTER_TRACKER.md