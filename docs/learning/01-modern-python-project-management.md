# Modern Python Project Management

---

## 1. Overview

Modern Python development has evolved from using multiple configuration files (`requirements.txt`, `setup.py`, `setup.cfg`) to a standardized approach centered around `pyproject.toml`.

In AI Developer OS, we use **uv** for dependency management and virtual environment management because it provides a fast, reproducible, and modern workflow.

This document explains the concepts, implementation, best practices, and lessons learned while setting up AI Developer OS.

---

## 2. Problem Statement

Older Python projects commonly suffered from:

- Configuration spread across multiple files.
- Manual virtual environment management.
- Inconsistent dependency versions.
- "Works on my machine" issues.
- Difficult onboarding for new developers.

Modern Python tooling solves these problems by standardizing project configuration and dependency management.

---

## 3. Why This Approach?

For AI Developer OS, we wanted:

- Fast dependency installation.
- Reproducible environments.
- Easy onboarding.
- Modern tooling.
- Clean project configuration.
- Production-ready workflow.

After evaluating the available options, we selected **uv**.

Reasons:

- Extremely fast.
- Built-in virtual environment management.
- Modern packaging standards.
- Lock file support.
- Excellent developer experience.

> **Project Decision**
>
> Refer: **ADR-0002 – Use uv for Dependency Management**

---

## 4. Core Concepts

### 4.1 pyproject.toml

The central configuration file for a modern Python project.

Stores:

- Project metadata
- Python version
- Runtime dependencies
- Development dependencies
- Tool configuration

---

### 4.2 uv

A modern Python package manager.

Responsibilities:

- Create virtual environments
- Install packages
- Resolve dependencies
- Generate lock files
- Execute project commands

---

### 4.3 Virtual Environment (.venv)

An isolated Python environment dedicated to a single project.

Benefits:

- Prevents dependency conflicts.
- Protects system Python.
- Makes projects reproducible.

---

### 4.4 uv.lock

Stores the exact dependency versions.

Purpose:

- Reproducible builds
- Consistent CI/CD
- Consistent production deployments

> Always commit `uv.lock`.

---

### 4.5 Runtime Dependencies

Packages required to run the application.

Examples:

- FastAPI
- Uvicorn
- Pydantic Settings

---

### 4.6 Development Dependencies

Packages required only during development.

Examples:

- Ruff
- Pytest

---

## 5. How It Works

```
          Developer
               │
               ▼
      Edit pyproject.toml
               │
               ▼
      uv resolves packages
               │
               ▼
      Updates uv.lock
               │
               ▼
     Creates/Updates .venv
               │
               ▼
      Install packages
               │
               ▼
        Run application
```

Workflow:

1. Define dependencies in `pyproject.toml`.
2. Run a `uv` command.
3. `uv` resolves dependencies.
4. `uv.lock` is updated.
5. `.venv` is synchronized.
6. Application runs inside the project environment.

---

## 6. AI Developer OS Implementation

### Project Structure Decision

Two layouts were evaluated.

**Option 1**

```
src/
```

Suitable for reusable Python packages.

**Option 2 (Selected)**

```
app/
```

Suitable for production FastAPI applications.

We selected **app/** because AI Developer OS is a SaaS application rather than a reusable Python library.

Refer:

- ADR-0001

---

### Dependency Management

Current runtime dependencies:

- FastAPI
- Uvicorn
- Pydantic Settings

Current development dependencies:

- Ruff
- Pytest

Managed using:

- uv
- pyproject.toml
- uv.lock

---

### Current Workflow

```
Developer
    │
    ▼
pyproject.toml
    │
    ▼
uv
    │
    ▼
uv.lock
    │
    ▼
.venv
    │
    ▼
Application
```

---

## 7. Best Practices

- Keep `pyproject.toml` as the single source of truth.
- Commit `uv.lock`.
- Never commit `.venv`.
- Separate runtime and development dependencies.
- Use `uv` instead of installing packages globally.
- Use `uv run` to execute project commands.
- Keep dependencies minimal.
- Pin the Python version.
- Review dependency updates before upgrading.
- Document major engineering decisions using ADRs.

---

## 8. Common Mistakes

- Mixing application and package layouts.
- Forgetting to commit `uv.lock`.
- Committing `.venv`.
- Installing packages globally.
- Editing `uv.lock` manually.
- Mixing runtime and development dependencies.
- Adding unnecessary packages.
- Updating dependencies without testing.

---

## 9. Lessons Learned During AI Developer OS

### Lesson 1

We initially ran:

```bash
uv init --package
```

This created a package-oriented project that expected a `src/` layout.

**Learning**

Understand whether you're building:

- a Python package
- or a deployable application

before initializing the project.

---

### Lesson 2

We chose to keep the existing `app/` structure.

Reason:

AI Developer OS is a FastAPI SaaS application.

---

### Lesson 3

The project initially contained a build backend configuration.

Since we are building an application rather than publishing a package, we removed the build backend to simplify dependency management.

---

### Lesson 4

`uv.lock` should always be committed.

`.venv` should never be committed.

---

### Lesson 5

Modern Python development is not only about writing code.

Project structure, tooling, reproducibility, and documentation are equally important.

---

## 10. Interview Questions

### Basic

1. What is `pyproject.toml`?
2. Why was it introduced?
3. What is `uv`?
4. What is a virtual environment?
5. Why should `.venv` not be committed?

### Intermediate

6. What is a lock file?
7. Why commit `uv.lock`?
8. Difference between runtime and development dependencies?
9. Why use `uv run`?
10. Why use `app/` instead of `src/`?

### Advanced

11. How does dependency resolution work?
12. What happens internally when running `uv add fastapi`?
13. How do lock files improve CI/CD?
14. Why are reproducible builds important?
15. How would you migrate an existing `pip` project to `uv`?

---

## 11. Key Takeaways

- `pyproject.toml` is the central configuration file.
- `uv` manages dependencies and virtual environments.
- `uv.lock` guarantees reproducible environments.
- `.venv` isolates project dependencies.
- Separate runtime and development dependencies.
- Keep project configuration simple and consistent.
- Document engineering decisions using ADRs.
- Choose the project structure before writing code.
- Build projects with maintainability in mind, not just functionality.

---

## Related Documents

### ADRs

- ADR-0001 — Use `app/` as the Application Root
- ADR-0002 — Use `uv` for Dependency Management

### Project Files

- `pyproject.toml`
- `uv.lock`
- `.gitignore`

### Last Updated

2026-07-11