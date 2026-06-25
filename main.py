from fastapi import FastAPI
from model.user_connection import UserConnection
from schema.user_schema import UserSchema


app = FastAPI()
conn = UserConnection()
@app.get("/")
def read_root():
    items = []
    for data in conn.read_all():
        dictionary = {}
        dictionary["id_usuario"] = data[0]
        dictionary["id_rol"] = data[1]
        dictionary["nombre_usuario"] = data[2]
        dictionary["apellido_usuario"] = data[3]
        dictionary["correo_usuario"] = data[4]
        dictionary["contrasena_hash"] = data[5]
        dictionary["fecha_registro"] = data[6]
        dictionary["estado"] = data[7]
        items.append(dictionary)
    return items

@app.get("/api/usuarios/{id_usuario}")
def get_one(id_usuario: int):
    dictionary = {}
    data = conn.read_one(id_usuario)
    dictionary["id_usuario"] = data[0]
    dictionary["id_rol"] = data[1]
    dictionary["nombre_usuario"] = data[2]
    dictionary["apellido_usuario"] = data[3]
    dictionary["correo_usuario"] = data[4]
    dictionary["contrasena_hash"] = data[5]
    dictionary["fecha_registro"] = data[6]
    dictionary["estado"] = data[7]
    return dictionary


@app.post("/api/insert")
def insert(user_data: UserSchema):
    data = user_data.model_dump()
    conn.write(data) 

  
