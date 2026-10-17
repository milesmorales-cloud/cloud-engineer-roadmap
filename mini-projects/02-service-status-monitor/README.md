# Service Status Monitor

## Overview

The Service Status Monitor is a Python tool that checks the availability of multiple web services. It sends HTTP requests, records response status codes, measures response times, and reports whether each service is online or offline.

The project currently monitors the deployed QuizLive application and Google's website.

## Features

- Monitor multiple web services in one run.
- Report HTTP status codes.
- Measure response time in milliseconds.
- Handle HTTP errors, connection failures, and timeouts.
- Configure a request timeout to avoid waiting indefinitely.
- Run automated tests without relying on live services.

## Technologies

- Python 3
- `urllib` for HTTP requests
- `time` for response-time measurement
- `unittest` and `unittest.mock` for automated testing

The project uses Python's standard library and requires no third-party packages.

## Project Structure

```text
02-service-status-monitor/
├── main.py
├── README.md
└── tests/
    └── test_main.py
```

## Usage

Run the monitor:

```bash
python3 main.py
```

The program checks each configured service and displays its name, URL, online/offline status, HTTP status code, and response time.

To monitor another service, add its name and URL to the `services` list in `main.py`.

## Testing

Run the automated tests:

```bash
python3 -m unittest discover -s tests -v
```

The tests cover successful responses, HTTP errors, and connection failures using mocked HTTP requests.

## Learning Outcomes

This project provides practical experience with HTTP requests, status codes, response-time measurement, timeouts, exception handling, multi-service monitoring, and automated testing.

These skills are useful when monitoring web applications and troubleshooting services deployed in cloud environments.

## Current Limitations

- Services are checked once per program run.
- The monitor does not yet send alerts.
- An HTTP success response does not necessarily guarantee that an application's internal functionality is healthy.
