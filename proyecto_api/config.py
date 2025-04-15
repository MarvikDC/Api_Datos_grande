class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg://postgres:Qwerty1234@localhost/db10a"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CHARSET = "latin1"  # Codificación de la base de datos
    PAGE_SIZE = 100     # Tamaño máximo de página para paginación