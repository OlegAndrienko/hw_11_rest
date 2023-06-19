from fastapi import FastAPI, Depends, HTTPException, status, Path, APIRouter, Request, Query
from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import List

from src.database.db import get_db
from src.routers import users


app = FastAPI() #create app object from FastAPI class 

@app.get("/")           #decorator route
async def root():
    return {"message": "Hello World"}

@app.get("/api/healthchecker") #decorator route
def healthchecker(db: Session = Depends(get_db)): #db: Session = Depends(get_db) - db is a variable, Session is a class
    try:
        # Make request
        result = db.execute(text("SELECT 1")).fetchone()
        if result is None:
            raise HTTPException(status_code=500, detail="Database is not configured correctly")
        return {"message": "Welcome to FastAPI!"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error connecting to the database")
    
    

app.include_router(users.router, prefix='/api') #include router from users.py  #from src\routers\users.py