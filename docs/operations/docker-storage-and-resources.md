# Docker Storage & Resources

## Purpose

Understanding where Docker stores resources is essential for debugging, maintenance, and production deployments.

This document explains how Docker manages images, containers, volumes, networks, and build cache internally.

---

# Docker Architecture

```
                Docker CLI
                     │
                     ▼
            Docker Engine (Daemon)
                     │
 ┌──────────┬──────────┬──────────┬──────────┬──────────┐
 ▼          ▼          ▼          ▼          ▼
Images   Containers   Volumes   Networks   Build Cache
```

The Docker CLI is the command-line interface.

The Docker Engine performs all Docker operations.

---

# Images

Images are read-only templates used to create containers.

Example

```
python:3.12-slim

↓

ai-developer-os:dev
```

Useful commands

```bash
docker images
```

```bash
docker image inspect IMAGE_NAME
```

---

# Containers

Containers are running instances of images.

One image can create multiple containers.

```
Image

↓

Container A

Container B

Container C
```

Useful commands

```bash
docker ps
```

```bash
docker ps -a
```

```bash
docker stop
```

```bash
docker rm
```

---

# Volumes

Volumes provide persistent storage.

Without volumes

```
Delete Container

↓

Application Data Lost
```

With volumes

```
Delete Container

↓

Volume Still Exists

↓

Data Preserved
```

Useful command

```bash
docker volume ls
```

---

# Networks

Docker creates virtual networks allowing containers to communicate.

Examples

```
bridge

host

none
```

Later we will create

```
FastAPI

↓

PostgreSQL

↓

Redis

↓

RabbitMQ
```

using Docker networks.

Useful command

```bash
docker network ls
```

---

# Build Cache

Docker stores every build layer.

```
FROM python

↓

WORKDIR

↓

COPY pyproject.toml

↓

RUN uv sync

↓

COPY app
```

If only

```
COPY app
```

changes,

Docker reuses every previous layer.

This significantly speeds up builds.

---

# Where Are Docker Resources Stored?

On Windows with Docker Desktop,

Docker runs inside a lightweight Linux virtual machine provided by WSL2.

Conceptually

```
Windows

↓

Docker Desktop

↓

WSL2 Linux VM

↓

/var/lib/docker

    ├── images
    ├── containers
    ├── volumes
    ├── networks
    └── build-cache
```

Developers normally should **not** access these directories directly.

Instead, Docker provides CLI commands to inspect and manage these resources.

---

# Resource Lifecycle

```
Project

↓

docker build

↓

Image

↓

docker run

↓

Container

↓

Application Running
```

If the container is deleted,

the image remains.

If the image is deleted,

the project source code remains.

---

# AI Developer OS Example

Current resources

```
Project

↓

Dockerfile.dev

↓

Image

ai-developer-os:dev

↓

Container

FastAPI
```

During development we also created

```
ai-developer-os:latest
```

accidentally by omitting the tag.

This reinforced an important best practice:

**Always build images with explicit tags to avoid confusion.**

---

# Best Practices

- Always use meaningful image tags.
- Keep images immutable.
- Remove unused containers periodically.
- Use volumes for persistent data.
- Use `.dockerignore` to reduce build context.
- Inspect resources using Docker CLI instead of accessing Docker's internal storage.

---

# Common Mistakes

- Assuming images are stored inside the project folder.
- Confusing images with containers.
- Storing database data inside containers.
- Using the `latest` tag unintentionally.
- Deleting containers without understanding volume persistence.