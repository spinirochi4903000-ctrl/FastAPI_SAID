from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserSchema(BaseModel):
        id_usuario: Optional[int] = None
        id_rol: Optional[int] = None
        nombre_usuario: str
        apellido_usuario: str
        correo_usuario: str
        contrasena_hash: str
        fecha_registro: Optional[datetime] = None
        estado: Optional[bool] = None
