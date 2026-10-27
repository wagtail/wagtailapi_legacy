# Agents

Important context for AI coding agents working on this project.

## Project overview

wagtailapi_legacy provides the Wagtail v2 API, extracted from Wagtail core (`wagtail.api.v2`) after its deprecation. The source code is in `src/wagtailapi_legacy/v2/`, with tests in `tests/`, docs in `docs/`, and a demo Wagtail site in `demo/`. The code is kept close to the original Wagtail code, to make it easy to port fixes between the two.

This project was created from the [cookiecutter-wagtail-package](https://github.com/wagtail/cookiecutter-wagtail-package) template and follows the [Wagtail package maintenance guidelines](https://wagtail.org/package-guidelines/).

## Key commands

```sh
just help            # View all commands
just install         # Install dependencies and git hooks
just demo            # Run the demo Wagtail site (migrate + load data + runserver)
just test            # Run tests with pytest
just lint            # Run all linters (Ruff, prek)
just format          # Run all formatters (Ruff, prek)
just coverage        # Run tests with coverage report
```

## Quality assurance

- Python: Ruff for linting and formatting (`ruff.toml`), prek hooks (`prek.toml`).
- Tests: pytest with pytest-django. Test settings are in `src/wagtailapi_legacy/test/settings.py`, and extend Wagtail's own test settings (`wagtail.test.settings`).
- CI: GitHub Actions in `.github/workflows/`.

Always run `just lint` and `just test` before considering work complete.

## Project layout

```
src/wagtailapi_legacy/v2/    # Package source code
src/wagtailapi_legacy/test/  # Test settings and URLs
tests/                       # Test modules (pytest)
docs/                        # Configuration and usage guides
demo/                        # Demo Wagtail site for development
.github/workflows/           # CI: linting, tests, nightly builds, publishing
```

## Guidelines

- Follow [Semantic Versioning](https://semver.org/) for releases.
- Use [Keep a Changelog](https://keepachangelog.com/) format for CHANGELOG.md.
- Refer to [CONTRIBUTING.md](CONTRIBUTING.md) for the full contribution workflow.
