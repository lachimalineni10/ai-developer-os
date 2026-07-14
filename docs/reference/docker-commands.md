# Docker Commands Reference

## Purpose

This document serves as a quick reference for Docker commands used throughout the AI Developer OS project.

Unlike the learning documents, this file focuses on **how to use Docker commands**, their syntax, available options, and practical usage during development.

---

# Docker Build

## Build an Image

```bash
docker build -f docker/Dockerfile.dev -t ai-developer-os:dev .
```

### What does it do?

Builds a Docker image from a Dockerfile.

---

### Syntax

```bash
docker build [OPTIONS] PATH
```

---

### Command Breakdown

```bash
docker build
```

Starts the Docker image build process.

---

```bash
-f docker/Dockerfile.dev
```

Specifies which Dockerfile should be used.

Without this option Docker searches for

```
Dockerfile
```

in the current directory.

Use `-f` when:

- Multiple Dockerfiles exist
- Development and Production Dockerfiles are separate

Example:

```
docker/
    Dockerfile.dev
    Dockerfile.prod
```

---

```bash
-t ai-developer-os:dev
```

Assigns a tag to the built image.

Syntax

```
image_name:tag
```

Example

```
ai-developer-os:dev
```

Where

- image name = ai-developer-os
- tag = dev

If no tag is supplied,

Docker automatically uses

```
latest
```

Example

```bash
docker build -t ai-developer-os .
```

becomes

```
ai-developer-os:latest
```

---

```
.
```

The build context.

Docker sends everything inside the current directory to the Docker Engine.

The build context includes

- application code
- Dockerfile
- configuration files

Anything excluded using `.dockerignore` will not be sent.

---

### Best Practice

Always use explicit tags.

Good

```bash
docker build -f docker/Dockerfile.dev -t ai-developer-os:dev .
```

Avoid

```bash
docker build -t ai-developer-os .
```

because Docker automatically creates the `latest` tag.

---

# Docker Images

## List Images

```bash
docker images
```

Shows all locally available images.

Useful for

- checking image names
- checking tags
- checking image size
- checking image IDs

---

## Remove Image

```bash
docker rmi IMAGE_NAME
```

Example

```bash
docker rmi ai-developer-os:latest
```

Removes an image.

If containers are using the image, Docker will refuse to delete it.

---

# Containers

## Run a Container

```bash
docker run -p 8000:8000 ai-developer-os:dev
```

Creates and starts a container from an image.

---

### Parameter Explanation

```
-p
```

Port Mapping

Syntax

```
HOST_PORT:CONTAINER_PORT
```

Example

```
8000:8000
```

Meaning

```
Browser
localhost:8000

↓

Docker Host Port 8000

↓

Container Port 8000

↓

FastAPI
```

Without `-p`, the application cannot be accessed from outside the container.

---

## List Running Containers

```bash
docker ps
```

Shows only running containers.

Useful for

- checking container IDs
- checking running status
- checking mapped ports

---

## List All Containers

```bash
docker ps -a
```

Parameter

```
-a
```

means

```
All
```

Shows

- Running containers
- Stopped containers
- Exited containers

---

## Stop Container

```bash
docker stop CONTAINER_ID
```

Gracefully stops a running container.

---

## Remove Container

```bash
docker rm CONTAINER_ID
```

Deletes a stopped container.

Docker will not remove a running container.

---

# Inspection

## Inspect Image

```bash
docker image inspect IMAGE_NAME
```

Displays detailed JSON metadata.

Useful for debugging.

---

## Inspect Container

```bash
docker container inspect CONTAINER_ID
```

Displays

- Environment Variables
- Mounts
- Networks
- IP Address
- Configuration

---

# Volumes

## List Volumes

```bash
docker volume ls
```

Lists all Docker-managed volumes.

---

# Networks

## List Networks

```bash
docker network ls
```

Shows all available Docker networks.

---

# Useful Commands We Used

Build

```bash
docker build -f docker/Dockerfile.dev -t ai-developer-os:dev .
```

Run

```bash
docker run -p 8000:8000 ai-developer-os:dev
```

List Images

```bash
docker images
```

Running Containers

```bash
docker ps
```

All Containers

```bash
docker ps -a
```

Remove Container

```bash
docker rm CONTAINER_ID
```

Remove Image

```bash
docker rmi IMAGE_NAME
```