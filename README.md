# Docker Cron Environment

A sample Docker container with Python 3.12 and cron that supports environment variables.

## Features

- Python 3.12
- Environment variable management with python-dotenv
- Package management with uv
- Two-phase build Dockerfile
- Logging functionality
- Docker Compose support

## Prerequisites

- Docker
- Docker Compose v2

## Usage

### Using Docker Compose (Recommended)

1. Prepare environment variables:
```bash
cp .env.example .env
```

2. Start the container:
```bash
docker compose up -d --build
```

3. Check logs:
```bash
# Logs are directly output to the logs directory on the host machine
tail -f logs/cron.log
```

### Using Docker Standalone

1. Prepare environment variables:
```bash
cp .env.example .env
```

2. Build Docker image:
```bash
docker build -t cron-env -f docker/Dockerfile .
```

3. Run container:
```bash
docker run -d \
  --name cron-container \
  -v "$(pwd)/.env:/app/.env:ro" \
  -v "$(pwd)/logs:/var/log" \
  cron-env
```

4. Check logs:
```bash
tail -f logs/cron.log
```

### Stopping and Removing Containers

```bash
# For Docker Compose
docker compose down

# For standalone Docker
docker stop cron-container
docker rm cron-container
```

## Environment Variables

- `CRON_MESSAGE`: Message displayed by the cron job (default: "default message")

## Troubleshooting

### If Logs Are Not Being Output

1. Verify the container is running properly:
```bash
docker ps
```

2. Check cron daemon status:
```bash
docker exec cron-container service cron status
```

3. Check crontab configuration:
```bash
docker exec cron-container crontab -l
```

## Directory Structure

```
.
├── docker/
│   ├── Dockerfile     # Dockerfile for multi-stage build
│   ├── crontab        # Cron job configuration file
│   └── entrypoint.sh  # Initialization script for container startup
├── logs/              # Log output directory
├── cron_job.py        # Python script to be executed
├── docker-compose.yml # Docker Compose configuration file
├── requirements.txt   # Python package dependencies
├── .env.example       # Sample environment variables file
└── README.md         # This file
```

## Notes

- The log directory (`logs/`) is created automatically
- The environment variable file (`.env`) must be prepared
- The container automatically restarts with the `unless-stopped` setting
