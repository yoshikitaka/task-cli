"""タスクモデルと管理"""

import json
import os
from datetime import datetime
from typing import List, Optional

DATA_FILE = os.path.join(os.path.dirname(__file__), "tasks.json")

class Task:
    def __init__(self, id: int, description: str, due: Optional[str] = None, done: bool = False):
        self.id = id
        self.description = description
        self.due = due
        self.done = done

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "due": self.due,
            "done": self.done
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            description=data["description"],
            due=data.get("due"),
            done=data.get("done", False)
        )

class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = []
        self._load()

    def _load(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r") as f:
                    data = json.load(f)
                    self.tasks = [Task.from_dict(t) for t in data]
            except (json.JSONDecodeError, IOError):
                self.tasks = []
        else:
            self.tasks = []

    def _save(self):
        with open(DATA_FILE, "w") as f:
            json.dump([t.to_dict() for t in self.tasks], f, indent=2)

    def add_task(self, description: str, due: Optional[str] = None) -> Task:
        if self.tasks:
            new_id = max(t.id for t in self.tasks) + 1
        else:
            new_id = 1
        task = Task(new_id, description, due)
        self.tasks.append(task)
        self._save()
        return task

    def list_tasks(self) -> List[Task]:
        return sorted(self.tasks, key=lambda t: t.id)

    def complete_task(self, task_id: int) -> bool:
        for task in self.tasks:
            if task.id == task_id:
                task.done = True
                self._save()
                return True
        return False

    def delete_task(self, task_id: int) -> bool:
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[i]
                self._save()
                return True
        return False
