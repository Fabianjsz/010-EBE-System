from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI(title="Hintergrundsystem API", version="1.0.0")



@app.get("/")
def read_root():
    return {"message": "Welcome to the Hintergrundsystem API"}

@app.get("/users")
def get_user():
    cur.execute

