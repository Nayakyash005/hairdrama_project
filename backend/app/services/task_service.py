from app.models.task import TaskCreate, TaskUpdate


class TaskService:
    def __init__(self):
        self.tasks_db = []

    def create_task(self, task: TaskCreate):
        pass

    def get_tasks(self):
        pass

    def get_task(self, task_id: int):
        pass

    def update_task(self, task_id: int, task: TaskUpdate):
        pass

    def delete_task(self, task_id: int):
        pass
