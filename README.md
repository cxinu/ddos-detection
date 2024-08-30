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

