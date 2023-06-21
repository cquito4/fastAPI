from sqlalchemy import create_engine

# Crear el motor de SQLAlchemy sin especificar una base de datos específica
engine = create_engine("mysql+pymysql://<usuario>:<password>@localhost:3306/?charset=utf8", echo=True)



