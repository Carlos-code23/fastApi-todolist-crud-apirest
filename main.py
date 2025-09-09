from fastapi import FastAPI, HTTPException
from models.todo import Todo 
from db import session
#uvicorn main:app --reload
app = FastAPI()

@app.post("/")
async def create_todo(text:str, is_done:bool=False):
    todo = Todo(text=text, is_done=is_done)
    session.add(todo)
    session.commit()
    return {"todo added": todo.text}

@app.get("/{id}")
async def get_todo(id: int):
    todo_query = session.query(Todo).filter(Todo.id == id)
    todo = todo_query.first()
    if todo is None:
        raise HTTPException(status_code=404, detail="todo not found") 
    return todo

@app.put("/{id}")
async def update_todo(id: int, new_text:str, is_done: bool=False):
    todo_query = session.query(Todo).filter(Todo.id == id)
    todo = todo_query.first()
    if new_text:
        todo.text = new_text
    todo.is_done = is_done
    session.add(todo)
    session.commit()

@app.delete("/{id}")
async def delete_todo(id: int):
    todo_query = session.query(Todo).filter(Todo.id == id)
    todo = todo_query.first()
    session.delete(todo)
    session.commit()
    return {"todo  deleted": id}