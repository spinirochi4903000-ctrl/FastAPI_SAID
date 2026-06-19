import psycopg

class UserConnection:
    conn = None
    
    def __init__(self):
        try:
            self.conn = psycopg.connect("dbname=said_database user=postgres password=Sena1234 host=localhost port=5432")
        except psycopg.OperationalError as err:
            print(err)
            self.conn.close()

    def write(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""INSERT INTO "usuarios" (id_usuario, id_rol, nombre_usuario, apellido_usuario, correo_usuario, contrasena_hash, fecha_registro, estado) VALUES (%(id)s, %(role_id)s, %(first_name)s, %(last_name)s, %(email)s, %(password_hash)s, %(registration_date)s, %(status)s)""", data)

            self.conn.commit()

    def __def__(self):
        if self.conn:
            self.conn.close()