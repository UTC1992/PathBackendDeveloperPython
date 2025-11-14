# Repository Guidelines

## Project Structure & Module Organization
The repo currently holds three standalone Python exercises in the root: `basico.py`, `Lists.py`, and `Tuplas.py`. Keep additional learning scripts in the root or group related topics under clearly named folders (for example, `collections/ListsAdvanced.py`). Place shared helpers inside `lib/` and import them relatively (`from lib.helpers import ...`). Add automated tests under `tests/`, mirroring the module names (`tests/test_lists.py`). Keep assets (sample CSVs, JSON fixtures) in `assets/` to avoid cluttering the top level.

## Build, Test, and Development Commands
- `python basico.py` – run the introductory example; adjust the filename to execute any other module.
- `PYTHONPATH=. python -m pytest tests` – run the test suite with the project root on the module path.
- `python -m compileall .` – optional sanity check that every script compiles before publishing.
Create a virtual environment if dependencies are added later (`python -m venv .venv && source .venv/bin/activate`).

## Coding Style & Naming Conventions
Use Python 3.11 syntax, 4-space indentation, and descriptive snake_case for variables, functions, and modules. Favor small, pure functions over inline scripts when logic grows. Type hints are encouraged for reusable helpers. Document non-obvious behavior with concise docstrings and inline comments only when they clarify intent. Format code with `ruff format` or `black` once such tooling is introduced, and lint with `ruff check`.

## Testing Guidelines
Adopt `pytest` for all new work. Name test files `test_<module>.py` and individual tests `test_<behavior>`. Cover both happy paths and edge cases (empty lists, invalid tuples, etc.). Aim for statement coverage above 80%; prioritize meaningful assertions over exhaustive mocks. Run `python -m pytest --maxfail=1 --disable-warnings -q` before opening a pull request.

## Commit & Pull Request Guidelines
Write commits in the present tense (`feat: add tuple unpacking demo`) and limit them to a single concern. Reference issues with `Refs #ID` when applicable. Pull requests should include: a short summary of the change, testing notes (commands run + results), and screenshots or console snippets when output changes. Request at least one peer review and wait for CI to pass before merging.

## Security & Configuration Tips
Never commit secrets; load credentials from environment variables or `.env` files ignored by Git. Validate and sanitize any external data before processing. When sharing the project, remove `.idea/` and other machine-specific metadata unless explicitly needed.
