# DDoS Detection System

## Overview
This project implements a basic DDoS detection system in Go. It monitors incoming traffic, detects potential DDoS attacks, and sends alerts.

## Setup
1. Clone the repository.
2. Update `config/config.go` with your SMTP server details and alert recipient.
3. Run `go run main.go` to start the server.

## Files
- `main.go`: Entry point of the application.
- `config/config.go`: Configuration settings.
- `alert/email.go`: Functions for sending email alerts.
- `monitor/traffic.go`: Request monitoring and detection logic.
- `mitigation/actions.go`: Mitigation strategies.

## Docker Instructions to Run Load Balancers and Servers

Directory Structure
```
ddos-prototype/
├── Docker/
│   ├── backend/
│   │   ├── Dockerfile
│   │   └── index.html
│   └── loadbalancer/
│       ├── Dockerfile
│       └── nginx.conf
├── Python
│   ├── analyze.py
│   ├── ip_detect.py
│   ├── ip_syndetect.py
│   ├── ip_testing.py
│   ├── network_logs.pcap
│   └── traffic_log.txt
├── alert
│   └── email.go
├── config
│   └── config.go
├── mitigation
│   └── actions.go
├── monitor
│   └── traffic.go
├── go.mod
├── main.go
├── network_logs.pcap
└── README.md
```

Create a Docker network
```shell
docker network create ddos-net
```

Build the backend server image
```shell
# Build the Docker image
docker build -t nginx-backend Docker/backend

# Run the Docker container
docker run -d --name backend1 --network ddos-net nginx-backend
docker run -d --name backend2 --network ddos-net nginx-backend
```

Build the load balancer image
```shell
# Build the Docker image
docker build -t nginx-lb Docker/loadbalancer

# Run the Docker container
docker run -d --name loadbalancer --network ddos-net -p 8080:80 nginx-lb
```

Access the load balancer
```shell
curl http://localhost:8080
```

Or visit `http://localhost:8080` in your browser.
