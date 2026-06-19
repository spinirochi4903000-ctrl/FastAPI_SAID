from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
        id_usuario: Optional[int]
        id_rol: int
        nombre_usuario: str
        apellido_usuario: str
        correo_usuario: str
        contrasena_hash: str
        fecha_registro: str
        estado: str
