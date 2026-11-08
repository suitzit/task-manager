from datetime import datetime


class Task:
    def __init__(self, id, title, discription="", priority="medium", status="todo"):
        self.id = id
        self.title = title
        self.discription = discription
        self.priority = priority
        self.status = status
        self.crated_at = datetime.now().strftime("%Y-%m-%d %H:%M")

    def to_dict(self):
        data = {"id": self.id, "title": self.title, "discription": self.discription, "priority": self.priority, "status": self.status}

        return data  

    @classmethod
    def from_dict(self, data):
        self.to_dict(data)

        return Task(id=data["id"], title=data["title"], discription=["discription"], priority=["priority"], status=["status"])

    def __str__(self):
        self.from_dict(Task)
        return f"[{self.id}] {self.title} | Статус: {self.status} | Приоритет: {self.priority} | Создано: {self.crated_at}"
    
