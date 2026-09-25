from fastapi import FastAPI, HTTPException
from app.models.user import UserCreate, UserLogin
from app.models.task import TaskCreate, TaskUpdate
from app.services.auth_service import AuthService
from app.services.task_service import TaskService
from app.services.gmail_service import GmailService

app = FastAPI(title="HairDrama API")

auth_service = AuthService()
task_service = TaskService()
gmail_service = GmailService()


@app.get("/")
def root():
    return {"message": "HairDrama API is running"}


@app.post("/register")
def register_user(user: UserCreate):
    created_user = auth_service.register_user(user)
    gmail_service.send_welcome_email(user.email, user.full_name or "User")
    return {"message": "User registered successfully", "user": created_user}


@app.post("/login")
def login_user(user: UserLogin):
    result = auth_service.login_user(user.email, user.password)
    if result["message"] == "Invalid credentials":
        raise HTTPException(status_code=401, detail=result["message"])
    return result


@app.post("/tasks")
def create_task(task: TaskCreate):
    created_task = task_service.create_task(task)
    return {"message": "Task created", "task": created_task}


@app.get("/tasks")
def get_tasks():
    return {"tasks": task_service.get_tasks()}


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = task_service.get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskUpdate):
    updated_task = task_service.update_task(task_id, task)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task updated", "task": updated_task}


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    deleted = task_service.delete_task(task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted"}
