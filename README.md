# Project README - FastAPI Endpoint for Information Retrieval

This project aims to create and host an HTTP endpoint that provides specific information in JSON format based on query parameters. The endpoint is built using FastAPI, a modern, fast (high-performance) web framework for building APIs with Python.

## Table of Contents

- [Requirements](#requirements)
- [Acceptance Criteria](#acceptance-criteria)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Requirements

The endpoint is expected to provide the following information in JSON format:

```json
{
  "slack_name": "example_name",
  "current_day": "Monday",
  "utc_time": "2023-08-21T15:04:05Z",
  "track": "backend",
  "github_file_url": "https://github.com/username/repo/blob/main/file_name.ext",
  "github_repo_url": "https://github.com/username/repo",
  "status_code": 200
}



