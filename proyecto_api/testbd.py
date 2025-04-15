from sqlalchemy import create_engine, text
from config import Config


print("inicio de script")
# Crear conexión a la base de datos
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)

# Probar la conexión
try:
    with engine.connect() as conn:
        # Usar SQLAlchemy's `text` para ejecutar consultas SQL
        result = conn.execute(text("SELECT version();"))
        print("Conexión exitosa!")
        for row in result:
            print(row)
except Exception as e:
    print("Error al conectar:", e)