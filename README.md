# Simple API Service

A lightweight FastAPI service containerized with Docker. This service provides a basic greeting and a health check endpoint.

## Project Structure

```text
.
├── main.py           # The FastAPI application code
├── Dockerfile        # Docker configuration
├── requirements.txt  # Python dependencies
└── README.md         # Documentation

```

## Prerequisites

* [Docker](https://docs.docker.com/get-docker/) installed on your machine.
* A `requirements.txt` file in the root directory containing:
```text
fastapi[standard]

```
---

## Getting Started

### 1. Build the Docker Image

Open your terminal in the project root and run:

```bash
docker build -t simple-api-service .

```

### 2. Run the Container

Map the container's port 8000 to your local machine:

```bash
docker run -p 8000:8000 simple-api-service

```

### 3. Verify the Service

Once the container is running, you can access the API at the following URLs:

* **Greeting:** [http://localhost:8000/](http://localhost:8000/)
* **Health Check:** [http://localhost:8000/health](http://localhost:8000/health)

---

## API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/` | Returns a "Hello World" message. |
| `GET` | `/health` | Returns the current status of the API. |

---

## Useful Commands

* **Run in Background:** Add `-d` to the run command: `docker run -d -p 8000:8000 simple-api-service`
* **Stop the Container:** `docker stop <container_id>`
* **View Logs:** `docker logs -f <container_id>`
