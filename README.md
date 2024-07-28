# Solar Backend FastAPI

Welcome to the Solar Backend FastAPI project! This project is designed to provide backend services for a LLM chat application using Solar API.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

## Introduction

This is an example project for developing an Upstage Solar API service based on FastAPI.

## Features

- FastAPI for building APIs
- Integration with OpenAI for using Upstage Solar API
- Configuration management
- Error handling and logging
- Modular structure for scalability

## Installation

To get started with this project, follow these steps:

1. **Clone the repository:**

    ```sh
    git clone https://github.com/ilevk/solar-backend-fastapi.git
    cd solar-backend-fastapi
    ```

2. **Set up a virtual environment:**
    - You can use any virtual environment tools.
    ```sh
    conda create --name solar python=3.12
    conda activate solar
    ```

3. **Install dependencies:**

    ```sh
    pip install poetry
    poetry install
    ```

4. **Set up environment variables:**

    Create a `.env` file in the root directory and add the necessary environment variables. For example:

    ```env
    API_KEY=your_upstage_api_key
    ```

## Usage

To run the application, use the following command:

```sh
$ uvicorn app.main:app --reload
```

# Project Structure
Here is an overview of the project structure:

```
solar-backend-fastapi/
├── app/
│   ├── clients/
│   │  └── openai.py
│   ├── core/
│   │   ├── errors/
│   │   ├── config.py
│   │   └── logging.py
│   ├── main.py
│   ├── models/
│   │   └── schemas/
│   ├── routers/
│   └── services/
├── .gitignore
├── .pre-commit-config.yaml
├── LICENSE
├── poetry.lock
├── pyproject.toml
├── README.md
└── start.sh
```

## FastAPI app
This directory contains the main application code.

- ### clients
  Contains client classes for interacting with external APIs.
  - `open_ai.py`: Client for interacting with the OpenAI API.
    - chat, stream_chat.

- ### core
  Contains core functionalities and configurations.
  - `errors`: Custom error classes and handlers.
  - `config.py`: Configuration settings for the application, including environment variables.
  - `logger.py`: Setup for logging.

- ### models
  Contains Pydantic models and schemas used for data validation and serialization.
    - `schemas`: Pydantic models for request and response payloads.

- ### routers
  Contains the API route definitions.
  - `chat.py`: Routes for chat operations.

- ### services
  Contains business logic and service classes.
  - `chat.py`: Services related to chat operations.
  - `service_factory.py`: Factory class for creating service instances.

## Configuration
Configuration is managed using environment variables. You can set these variables in a .env file in the root directory.


## License
This project is licensed under the MIT License. See the LICENSE file for more details.
