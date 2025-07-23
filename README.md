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

Sync the environment[^syncing]

```bash
uv sync # Create the .venv folder and sync dependencies
```

(Optional for manual activation, if needed)

```bash
source .venv/bin/activate    # Linux/macOS
# .venv\Scripts\activate     # Windows
```

## Running the backend[^running_fastapi]

To start the backend, run:

```bash
app
```

If you want to configure the port and/or host:

```bash
HOST=0.0.0.0 PORT=8080 app
```

## Swagger[^swagger]

The swagger documentation is available under [http://localhost:8000/docs](http://localhost:8000/docs)

It allows you to send requests and view the responses using the default UI from fastapi.

## Development

### Managing dependencies[^dependencies]

- Adding dependencies:

```bash
uv add <package>                      # Add to main dependencies
uv add --dev <package>                # Add to dev dependencies
uv add <package> --optional <group>   # Add to optional dependency group
```

- Removing dependencies:

```bash
uv remove <package>                      # Remove from main dependencies
uv remove --dev <package>                # Remove from dev dependencies
uv remove <package> --optional <group>   # Remove from optional group
```

- Syncing the environment

```bash
uv sync                  # Sync all (main + dev dependencies)
uv sync --dev            # Same as above (explicit)
uv sync --only-dev       # Sync only dev dependencies
uv sync --no-dev         # Sync only main dependencies
uv sync --extra <group>  # Include optional group dependencies
```


[^syncing]: [https://docs.astral.sh/uv/concepts/projects/sync/](https://docs.astral.sh/uv/concepts/projects/sync/)
[^running_fastapi]: [https://fastapi.tiangolo.com/tutorial/first-steps/#run-it](https://fastapi.tiangolo.com/tutorial/first-steps/#run-it)
[^swagger]: [https://fastapi.tiangolo.com/how-to/configure-swagger-ui/](https://fastapi.tiangolo.com/how-to/configure-swagger-ui/)
[^dependencies]: [https://docs.astral.sh/uv/concepts/projects/dependencies/](https://docs.astral.sh/uv/concepts/projects/dependencies/)
