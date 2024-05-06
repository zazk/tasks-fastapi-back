from fastapi import FastAPI, Depends, HTTPException, Path, status
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated
from sqlalchemy.orm import Session

import models
from models import Tasks, Base, Users
from database import engine, get_db
from schema import TaskSchema, UserSchema

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/")
def home():
    return {"Message": "Welcome to Message App"}

# Tasks Requests
@app.post("/tasks", status_code=status.HTTP_201_CREATED)
async def create_task(task_request: TaskSchema, db: Session = Depends(get_db)):
    task = Tasks(**task_request.model_dump())
    db.add(task) 
    db.commit()
    db.refresh(task)
    return task

@app.get('/tasks', status_code=status.HTTP_200_OK)
async def get_tasks(db: db_dependency):
    return db.query(Tasks).all()

@app.put('/tasks/{task_id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_task(db: db_dependency, task_request: TaskSchema, task_id: int = Path(gt=0)):
    task = db.query(Tasks).filter(Tasks.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task not found')
        
    for var, value in vars(task_request).items():
        setattr(task, var, value) if value else None
    db.commit()

@app.delete('/tasks/{task_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(db: db_dependency, task_id: int = Path(gt=0)):
    task = db.query(Tasks).filter(Tasks.id == task_id).first()

    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task not found')
    
    db.delete(task)
    db.commit()

# User Requests
@app.post("/users", status_code=status.HTTP_201_CREATED)
async def create_task(user_request: UserSchema, db: Session = Depends(get_db)):
    task = Users(**user_request.model_dump())
    db.add(task) 
    db.commit()
    db.refresh(task)
    return task

@app.get('/users', status_code=status.HTTP_200_OK)
async def read_all_products(db: db_dependency):
    return db.query(Users).all()

@app.delete('/users/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(db: db_dependency, user_id: int = Path(gt=0)):
    user = db.query(Users).filter(Users.id == user_id).first()

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    
    db.delete(user)
    db.commit()