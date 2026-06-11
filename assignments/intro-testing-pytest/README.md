# Intro to Testing with pytest

## Objective
Students will learn how to write unit tests using `pytest`, organize tests, and configure a GitHub Actions workflow to run tests automatically.

## Tasks

1. Write unit tests for the provided starter code using `pytest`.
   - Description: Add tests that verify the correctness of the functions in `starter-code.py`.
   - Requirements:
     - Create tests covering normal cases and edge cases.
     - Use `pytest` features such as `parametrize` where appropriate.
     - Ensure all tests pass locally.

2. Configure CI to run tests automatically with GitHub Actions.
   - Description: Use the provided workflow file to run `pytest` on `push` and `pull_request` events.
   - Requirements:
     - The workflow should install dependencies from `requirements.txt`.
     - The workflow should run tests from the `assignments/intro-testing-pytest` directory.

## Starter files

- `starter-code.py` — contains the functions to be tested.
- `tests/test_basic.py` — example tests students can use as a reference.
- `requirements.txt` — lists `pytest`.

## How to run tests locally

From the repository root:

```bash
cd assignments/intro-testing-pytest
python3 -m pip install --user -r requirements.txt
pytest -q
```

## Deliverables

- A set of passing tests under `tests/`.
- (Optional) Any notes on design decisions or edge cases in a short `notes.md`.
