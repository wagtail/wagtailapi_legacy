# Task runner: https://github.com/casey/just
# Requires: `uv`, `prek`, and `just`.
# Editable package path under `src/` (passed to `coverage run --source`).

# List all the justfile recipes.
help:
    just --list --list-prefix 'just '

# Remove all the Python cache files.
clean-pyc:
    find . -name '*.pyc' -exec rm -f {} +
    find . -name '*.pyo' -exec rm -f {} +
    find . -name '*~' -exec rm -f {} +

# Install the dependencies.
install: clean-pyc
    uv sync --dev
    uv run prek

# Run all linters.
lint:
    uv run ruff format --check .
    uv run ruff check .
    SKIP=ruff-check,ruff-format uv run prek run --all-files

# Run all formatters.
format:
    uv run ruff check . --fix
    uv run ruff format .
    SKIP=ruff-check,ruff-format uv run prek run --all-files

# Run tests with pytest.
test:
    uv run pytest

test-lowest-deps:
    #!/usr/bin/env bash
    set -euo pipefail
    lowest_python=$(uv run python -c 'import tomllib; print(tomllib.load(open("pyproject.toml","rb"))["project"]["requires-python"].removeprefix(">=").strip())')
    uv run --isolated --python "$lowest_python" --resolution lowest-direct pytest

test-highest-deps:
    uv run --isolated --with 'Django, Wagtail' pytest

# Run tests with coverage.
coverage:
    uv run pytest --cov src/wagtailapi_legacy
    uv run coverage report -m
    uv run coverage html

# Make migrations and migrate the database.
migrate:
    uv run ./demo/manage.py makemigrations
    uv run ./demo/manage.py migrate

# Run the development server at the given host and port.
runserver:
    uv run ./demo/manage.py runserver

# Load the initial data into the database.
load_initial_data:
    uv run ./demo/manage.py load_initial_data

# Open a shell to the demo application.
shell:
    uv run ./demo/manage.py shell

# Run the demo application.
demo: migrate load_initial_data runserver
