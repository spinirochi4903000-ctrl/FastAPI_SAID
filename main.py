from fastapi import FastAPI
from model.user_connection import UserConnection
from schema.user_schema import UserSchema


app = FastAPI()
conn = UserConnection()
@app.get("/")
def read_root():
    conn
    return {"Hello": "World"}


@app.post("/api/insert")
def insert(user_data: UserSchema):
    data = user_data.model_dump()
    conn.write(data) 

  
