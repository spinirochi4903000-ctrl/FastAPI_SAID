import psycopg

class UserConnection:
    conn = None
    
    def __init__(self):
        try:
            self.conn = psycopg.connect("dbname=said_database user=postgres password=Sena1234 host=localhost port=5432")
        except psycopg.OperationalError as err:
            print(err)
            self.conn.close()

    def read_all(self):
        with self.conn.cursor() as cur:
            data = cur.execute("""
            SELECT * FROM usuarios
            """)
            return data.fetchall()

    def read_one(self, id_usuario: int):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                SELECT * FROM usuarios WHERE id_usuario = %s
            """, (id_usuario,))
            return data.fetchone()

    def write(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
        INSERT INTO "usuarios" (
            id_rol, 
            nombre_usuario, 
            apellido_usuario, 
            correo_usuario, 
            contrasena_hash
        ) 
        VALUES (
            %(id_rol)s, 
            %(nombre_usuario)s, 
            %(apellido_usuario)s, 
            %(correo_usuario)s, 
            %(contrasena_hash)s
        )
    """, data)
            self.conn.commit()

    def __def__(self):
        if self.conn:
            self.conn.close()