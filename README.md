# Backend template 
FastAPI backend template for developing tools, demos, projects that involve LLMs. 

# Prerequisites

- Python 3.13
- uv

# Installation

Clone the repo:

```
git clone https://github.com/aihpi/backend-template.git
cd backend-template
```

Create virtual environment:

```
python3 -m venv .venv
source .venv/bin/activate    # Linux/macOS
# .venv\Scripts\activate     # Windows
```
Install dependencies with uv:
```
uv sync
```

# Running the backend

To start the backend, run:
```
app
```

If you want to configure the port and/or host:

```
HOST=0.0.0.0 PORT=8080 app 
```

# Swagger 

The swagger documentation is available under http://localhost:8000/docs

It allows you to send requests and view the responses using the default UI from fastapi.

# Development

Activating the virtual environment:

```
. .venv/bin/activate
```

Adding dependencies:

```
uv add <dependency1> <dependency2> <dependency3>
```



