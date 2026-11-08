import json
from pathlib import Path

from app.task import Task


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title, description, priority):
        if priority not in ["low", "medium", "high"]:
            raise ValueError("Неверный ввод")
        else:
            new_task = Task(self.next_id, title, description, priority)
            self.tasks.append(new_task)
            self.next_id += 1

    def get_all_tasks(self):
        return self.tasks

    def get_task_by_id(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task

        raise ValueError("Задание не найдено")

    def update_task(
        self, task_id, title=None, description=None, priority=None, status=None
    ):
        task = self.get_task_by_id(task_id)

        if title is not None:
            task.title = title

        if description is not None:
            task.description = description

        if priority is not None:
            if priority not in ["low", "medium", "high"]:
                raise ValueError("Неверный ввод")
            else:
                task.priority = priority

        if status is not None:
            if status not in ["todo", "in_progress", "done"]:
                raise ValueError("Неверный ввод")
            else:
                task.status = status

    def delete_task(self, task_id):
        task = self.get_task_by_id(task_id)

        self.tasks.remove(task)

    def save_to_json(self, filename="data/tasks.json"):
        data = [task.to_dict() for task in self.tasks]

        folder_patch = Path("data")
        if not folder_patch.is_dir():
            folder_patch.mkdir()

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def load_from_json(self, filename="data/tasks.json"):
        path = Path(filename)

        if path.exists():
            with open(filename, "r", encoding="utf-8") as f:
                data_list = json.load(f)

                for item in data_list:
                    self.tasks.append(Task.from_dict(item))

            if self.tasks:
                heighest_id = max(task.id for task in self.tasks)

                self.next_id = heighest_id + 1
