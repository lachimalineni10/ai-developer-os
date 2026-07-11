# Project Configuration & Environment Management

---

## 1. Overview

Every application needs configuration to run. Examples include database credentials, API keys, host information, logging levels, and feature flags.

Hardcoding these values inside the source code makes applications difficult to maintain, insecure, and environment-dependent.

Modern applications separate configuration from business logic by storing environment-specific values outside the codebase. In AI Developer OS, we use environment variables with `pydantic-settings` to create a secure, type-safe, and maintainable configuration system.

---

## 2. Problem Statement

Imagine an application with the following values hardcoded:

- Database password
- JWT secret
- API keys
- Redis URL
- RabbitMQ URL
- Debug mode

This approach creates several problems:

- Secrets become part of the source code.
- Different environments require code changes.
- Developers accidentally commit sensitive information.
- Deployments become difficult to automate.
- Testing multiple environments becomes error-prone.

Modern applications solve this by separating configuration from application logic.

---

## 3. Why This Approach?

AI Developer OS will eventually run in multiple environments:

- Local Development
- Testing
- Staging
- Production

Each environment requires different configuration values while the application code remains unchanged.

To achieve this, we use:

- Environment variables
- `.env` files for local development
- `pydantic-settings` for validation
- A centralized `config.py`

This provides:

- Security
- Type safety
- Validation
- Scalability
- Easier deployments

---

## 4. Core Concepts

### 4.1 Configuration

Configuration is any value that controls how an application behaves without modifying the source code.

Examples:

- Database URL
- API keys
- Port number
- Log level
- Debug mode

---

### 4.2 Environment Variables

Environment variables are key-value pairs provided by the operating system or deployment platform.

Example:

```
DATABASE_URL=postgresql://...
```

Advantages:

- Keeps secrets out of the codebase.
- Different values for different environments.
- Standard practice across modern applications.

---

### 4.3 `.env` File

A `.env` file stores environment variables for local development.

Example:

```
APP_NAME=AI Developer OS
DEBUG=True
HOST=0.0.0.0
PORT=8000
```

Important:

- Use `.env.example` as a template.
- Never commit the real `.env` file.

---

### 4.4 `pydantic-settings`

`pydantic-settings` loads environment variables into Python objects with validation and type conversion.

Benefits:

- Automatic parsing
- Default values
- Type safety
- Validation
- Cleaner code

---

### 4.5 `config.py`

`config.py` acts as the single entry point for accessing application settings.

Instead of reading environment variables throughout the application, every module imports configuration from one centralized location.

---

### 4.6 Settings Object

A Settings object represents all application configuration.

Example categories:

- Application
- Database
- Authentication
- Redis
- RabbitMQ
- AI Providers
- Logging

---

## 5. How It Works

```
Developer
      │
      ▼
   .env File
      │
      ▼
Environment Variables
      │
      ▼
pydantic-settings
      │
      ▼
 Settings Object
      │
      ▼
config.py
      │
      ▼
Application Components
```

Workflow:

1. Configuration is defined in `.env`.
2. Environment variables are loaded.
3. `pydantic-settings` validates and converts values.
4. A Settings object is created.
5. `config.py` exposes the settings.
6. The application imports the centralized configuration.

---

## 6. AI Developer OS Implementation

The project will maintain a single configuration module:

```
app/
└── core/
    └── config.py
```

Responsibilities:

- Load environment variables.
- Validate configuration.
- Provide default values.
- Expose a shared settings instance.

Current configuration categories include:

- Application
- API
- Logging

Future categories:

- PostgreSQL
- Redis
- RabbitMQ
- JWT
- AWS
- Gemini
- OpenAI
- Feature Flags

This design allows new configuration options to be added without changing existing modules.

---

## 7. Best Practices

- Keep secrets outside the source code.
- Commit `.env.example`, not `.env`.
- Validate configuration during application startup.
- Keep all configuration in one place.
- Use meaningful variable names.
- Provide sensible default values where appropriate.
- Fail fast if required configuration is missing.
- Group related settings together.
- Document every configuration option.

---

## 8. Common Mistakes

- Hardcoding secrets.
- Committing `.env` to Git.
- Reading environment variables throughout the application.
- Using inconsistent variable names.
- Not validating configuration.
- Mixing configuration with business logic.
- Duplicating configuration values.
- Forgetting to update `.env.example`.

---

## 9. Lessons Learned During AI Developer OS

### Lesson 1

Configuration should be designed before application development begins.

A centralized configuration system prevents future refactoring.

---

### Lesson 2

The Settings object should be treated as read-only.

Application code should consume configuration rather than modify it.

---

### Lesson 3

Even in the early stages of development, using `pydantic-settings` establishes production-ready practices.

---

### Lesson 4

Keeping configuration categories organized from the beginning makes it easier to introduce new infrastructure components such as databases, caches, message brokers, and cloud services.

---

## 10. Interview Questions

### Basic

1. What is application configuration?
2. What are environment variables?
3. Why use a `.env` file?
4. What is `pydantic-settings`?
5. Why centralize configuration?

### Intermediate

6. Why should secrets not be committed to Git?
7. How does `pydantic-settings` improve reliability?
8. What is the purpose of a Settings object?
9. Why validate configuration at startup?
10. Why use `.env.example`?

### Advanced

11. How would you manage configuration across development, staging, and production?
12. How would you securely store API keys in AWS?
13. How would you rotate secrets without changing application code?
14. How would you structure configuration for a microservices architecture?
15. What happens if a required environment variable is missing?

---

## 11. Key Takeaways

- Configuration should be separate from business logic.
- Environment variables are the industry standard.
- `.env` files simplify local development.
- `pydantic-settings` provides validation and type safety.
- `config.py` acts as the application's configuration gateway.
- Centralized configuration improves maintainability and scalability.
- Secure configuration management is essential for production systems.

---

## References

### Related Learning Documents

- 01 - Modern Python Project Management
- 03 - FastAPI Fundamentals
- 07 - Logging & Monitoring
- 15 - Authentication (JWT)

### Related ADRs

- ADR-0002 — Use `uv` for Dependency Management

### Related Project Files

- `app/core/config.py`
- `.env`
- `.env.example`
- `pyproject.toml`
- `docs/development/ENVIRONMENT_STRATEGY.md`

### Last Updated

2026-07-11