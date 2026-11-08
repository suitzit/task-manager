class TaskManager:
    def __init__(self):
        self.task = []
        self.next_id = 1

    def add_task(self, title, discription, priority):
        if priority != ["low", "medium", "high"]:
            raise ValueError("Неверный ввод")
        else:
            Task = (self.next_id, title, discription, priority)
            self.task.append(Task)
            self.next_id += 1
            