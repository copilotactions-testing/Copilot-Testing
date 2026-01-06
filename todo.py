#!/usr/bin/env python3
"""
A tiny todo CLI that stores tasks in a local JSON file.
Usage examples:
  python todo.py add "Buy milk"
  python todo.py list
  python todo.py done 1
  python todo.py rm 1
"""

import os
import json
import argparse

TASKS_FILE = os.path.join(os.path.dirname(__file__), "tasks.json")


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except Exception:
            return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks.")
        return
    for i, t in enumerate(tasks, 1):
        status = "✓" if t.get("done") else " "
        print(f"{i}. [{status}] {t.get('title')}")


def add_task(title):
    tasks = load_tasks()
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Added:", title)


def complete_task(idx):
    tasks = load_tasks()
    if idx < 1 or idx > len(tasks):
        print("Invalid index")
        return
    tasks[idx - 1]["done"] = True
    save_tasks(tasks)
    print("Completed:", tasks[idx - 1]["title"])


def remove_task(idx):
    tasks = load_tasks()
    if idx < 1 or idx > len(tasks):
        print("Invalid index")
        return
    t = tasks.pop(idx - 1)
    save_tasks(tasks)
    print("Removed:", t["title"])


def main():
    p = argparse.ArgumentParser(prog="todo", description="Simple todo CLI")
    sub = p.add_subparsers(dest="cmd")

    sub.add_parser("list", help="List tasks")

    a = sub.add_parser("add", help="Add a task")
    a.add_argument("title", nargs="+", help="Task title")

    c = sub.add_parser("done", help="Mark task as done")
    c.add_argument("index", type=int, help="Task index (from `list`)")

    r = sub.add_parser("rm", help="Remove a task")
    r.add_argument("index", type=int, help="Task index to remove")

    args = p.parse_args()

    if args.cmd == "list" or args.cmd is None:
        list_tasks()
    elif args.cmd == "add":
        add_task(" ".join(args.title))
    elif args.cmd == "done":
        complete_task(args.index)
    elif args.cmd == "rm":
        remove_task(args.index)
    else:
        p.print_help()


if __name__ == "__main__":
    main()
