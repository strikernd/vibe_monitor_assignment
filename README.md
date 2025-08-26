# Vibe Monitor: Observability Demo

## Quick Start

To start the entire observability stack, run:

```sh
docker-compose up --build -d
```
This will build and launch all services in detached mode.

## Project Structure & File Descriptions

- **docker-compose.yml**: Orchestrates all services (FastAPI app, Prometheus, Loki, Tempo, Grafana, Alloy) as Docker containers.
- **app/**
	- **main.py**: Defines FastAPI endpoints (`/`, `/slow`, `/error`, `/health`). Each endpoint responds with a random delay. Integrates Prometheus metrics using `prometheus_fastapi_instrumentator`.
	- **generate_traffic.py**: Continuously generates random requests to the FastAPI endpoints, simulating traffic for metrics and logs.
	- **Dockerfile**: Specifies how to build the FastAPI app container.
	- **requirements.txt**: Lists Python dependencies for the FastAPI app.
- **grafana/**
	- **datasources/ds.yaml**: Configures Grafana data sources for Prometheus (metrics), Loki (logs), and Tempo (traces).
	- **dashboards/**: (Optional) Place custom Grafana dashboards here for provisioning.
	- **data/**: Persists Grafana data (e.g., database, plugins).
- **alloy/**
	- **config.alloy**: Configures Grafana Alloy to scrape metrics from FastAPI and logs from Docker containers, forwarding them to Prometheus and Loki respectively.
- **prometheus/**
	- **config.yml**: Prometheus configuration for scraping metrics.
	- **data/**: Persists Prometheus metrics data.
- **loki/**
	- **data/**: Persists Loki log data.
- **tempo/**
	- **config.yml**: Tempo configuration for traces.
	- **data/**: Persists Tempo trace data.

## Services Overview

- **FastAPI**: Web API with instrumented endpoints for metrics and logs.
- **Prometheus**: Collects and stores metrics from FastAPI.
- **Loki**: Collects and stores logs from Docker containers.
- **Tempo**: Collects and stores traces (if instrumented).
- **Grafana**: Visualizes metrics, logs, and traces using configured data sources.
- **Alloy**: Scrapes metrics and logs, forwarding them to Prometheus and Loki.

## Usage

1. Start all services: `docker-compose up --build -d`
2. Access Grafana at [http://localhost:3000](http://localhost:3000) (default admin password: `admin`).
3. View metrics (Prometheus), logs (Loki), and traces (Tempo) in Grafana dashboards.
4. Run `generate_traffic.py` to simulate API traffic and generate observability data.

---

