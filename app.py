from fastapi import FastAPI
#from routes.user import user
#from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    # title="FastAPI MySQL",
    # description="API para el manejo de usuarios con FastAPI y MySQL",
    # version="1.0.0",
    # openapi_tags=[{"name": "Usuarios", "description": "Operaciones CRUD para usuarios"}]
)
origins = [
    # "http://localhost:5173",
]

# Configurar los orígenes permitidos para las solicitudes CORS
# Esto permite que el frontend acceda a la API desde los orígenes especificados
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# Agregar las rutas definidas en el módulo 'user' al objeto FastAPI
#app.include_router(user)
    