# Backend template

FastAPI backend template for developing tools, demos, projects that involve LLMs.

## Prerequisites

- Python 3.13
- uv

## Installation

Clone the repo:

```bash
git clone https://github.com/aihpi/backend-template.git
cd backend-template
```

Sync the environment

```bash
uv sync # Create the .venv folder and sync dependencies
```

(Optional for manual activation, if needed)

```bash
source .venv/bin/activate    # Linux/macOS
# .venv\Scripts\activate     # Windows
```

## Running the backend

To start the backend, run:

```bash
app
```

If you want to configure the port and/or host:

```bash
HOST=0.0.0.0 PORT=8080 app
```

## Swagger

The swagger documentation is available under [http://localhost:8000/docs](http://localhost:8000/docs)

It allows you to send requests and view the responses using the default UI from fastapi.

## Development

### Managing dependencies [^dependencies]

- Adding dependencies:

```bash
uv add <dependency1> <dependency2> <dependency3> # In the .venv environment
uv add --dev <dependency1> <dependency2> <dependency3> # As dev dependencies
uv add <dependency1> <dependency2> <dependency3> --optional <group_name> # In an optional group
```

- Removing dependencies:

```bash
uv remove <dependency1> <dependency2> <dependency3> # From the .venv environment
uv remove --dev <dependency1> <dependency2> <dependency3> # From dev dependencies
uv remove <dependency1> <dependency2> <dependency3> --optional <group_name> # From an optional group
```

- Syncing the environment

```bash
uv sync # Sync the main .venv environment with dev dependencies
uv sync --dev # Similar to the previous
uv sync --only-dev # Sync only the dev dependencies
uv sync --no-dev # Sync the main .venv environment with no dev dependencies
uv sync --extra <group_name> # Like uv sync plus the the dependencies from an optional group
```

[^dependencies]: [https://docs.astral.sh/uv/concepts/projects/dependencies/](https://docs.astral.sh/uv/concepts/projects/dependencies/)
