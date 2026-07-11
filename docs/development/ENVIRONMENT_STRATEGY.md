# Environment Strategy

## Purpose

This document defines how AI Developer OS manages configuration across development, testing, staging, and production environments.

The objective is to ensure that the same application code can run in multiple environments by changing only the configuration.

---

# Environments

| Environment | Purpose |
|-------------|---------|
| Development | Local development |
| Testing | Automated testing and CI |
| Staging | Pre-production validation |
| Production | Live application |

---

# Configuration Flow

                .env
                  │
                  ▼
        Environment Variables
                  │
                  ▼
         pydantic-settings
                  │
                  ▼
          app/core/config.py
                  │
                  ▼
             Application

The application never reads environment variables directly.

All configuration is accessed through the shared `settings` object.

---

# Configuration Files

| File | Commit | Purpose |
|------|--------|---------|
| .env.example | ✅ Yes | Template for developers |
| .env | ❌ No | Local development |
| .env.test | ❌ No | Test environment |
| .env.staging | ❌ No | Staging |
| .env.production | ❌ No | Production |

---

# Local Development

Local development uses:

.env

Example:

APP_NAME=AI Developer OS
APP_ENV=development
DEBUG=true
HOST=127.0.0.1
PORT=8000

---

# Docker

Docker will load variables using:

env_file:

or

environment:

inside docker-compose.yml.

---

# CI/CD

GitHub Actions will inject configuration through GitHub Secrets.

No secret files will exist inside the repository.

---

# Production

Production environments (AWS, Azure, GCP, etc.) will provide configuration using:

- Environment Variables
- AWS Secrets Manager
- AWS Systems Manager Parameter Store

No production secrets are committed to Git.

---

# Engineering Rules

- Never hardcode secrets.
- Never commit .env.
- Always commit .env.example.
- Keep configuration centralized in config.py.
- Validate configuration during application startup.
- Fail fast if required configuration is missing.

---

# Future Configuration Categories

Configuration will eventually include:

- Application
- API
- Logging
- PostgreSQL
- Redis
- RabbitMQ
- JWT
- AWS
- Gemini
- OpenAI
- Feature Flags

---

# Related Documents

- docs/learning/02-project-configuration-and-environment-management.md
- app/core/config.py