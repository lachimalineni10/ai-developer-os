# ADR-0003: Git Branching Strategy

## Status

Accepted

## Date

2026-07-11

## Context

AI Developer OS is being developed as a long-term production-grade SaaS project. As the codebase grows, changes should be isolated, reviewed, and integrated in a controlled manner.

A clear branching strategy improves code quality, simplifies collaboration, and supports future CI/CD workflows.

## Decision

Adopt a lightweight Git workflow with the following branches:

- `main` – Stable, production-ready code.
- `develop` – Primary integration branch for ongoing development.
- `feature/*` – Individual feature branches created from `develop`.

All feature development will be completed on feature branches, reviewed, and merged into `develop`. Stable milestones will then be merged from `develop` into `main`.

## Alternatives Considered

### Option 1: main only

- Simple workflow.
- Suitable for small personal projects.
- Increases the risk of unstable code reaching the primary branch.

### Option 2: Git Flow

- Well-structured release process.
- Includes release and hotfix branches.
- More complex than required for the current project stage.

### Option 3: main + develop + feature branches (Selected)

- Easy to understand.
- Supports incremental development.
- Integrates well with pull requests and CI/CD pipelines.
- Can evolve into a more advanced workflow if needed.

## Consequences

### Positive

- Stable production branch.
- Isolated feature development.
- Easier code reviews.
- Cleaner Git history.

### Negative

- Requires discipline to avoid direct commits to `main`.
- Slightly more branch management compared to a single-branch workflow.

## Related Documents

- docs/PROJECT_CONTEXT.md
- docs/progress/MASTER_TRACKER.md