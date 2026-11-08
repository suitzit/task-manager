from datetime import datetime


class Task:
    def __init__(self, id, title, description="", priority="medium", status="todo"):
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status
        self.crated_at = datetime.now().strftime("%Y-%m-%d %H:%M")

    def to_dict(self):
        data = {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "status": self.status,
            "created_at": self.crated_at,
        }

        return data

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            title=data["title"],
            description=data["description"],
            priority=data["priority"],
            status=data["status"],
            created_at=data["creared_at"],
        )

    def __str__(self):
        return f"[{self.id}] {self.title} | Статус: {self.status} | Приоритет: {self.priority} | Создано: {self.crated_at}"
