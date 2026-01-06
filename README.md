# Todo CLI

A minimal Python command-line todo application that stores tasks in a local `tasks.json` file. This project is intended as a tiny sample to demonstrate a simple Python CLI.

Usage

- List tasks: `python todo.py list` or `python todo.py`
- Add a task: `python todo.py add "Buy milk"`
- Mark done: `python todo.py done 1`
- Remove a task: `python todo.py rm 1`

Notes

- No external dependencies required; runs with Python 3.7+
- Tasks are stored in `tasks.json` next to `todo.py` (this file is gitignored)
