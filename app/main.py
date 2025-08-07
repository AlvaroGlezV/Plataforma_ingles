from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.writing import router as writing_router
from app.routes.reading import router as reading_router

app = FastAPI()

# Configurar CORS para permitir peticiones desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # en producción, reemplaza "*" por tu dominio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rutas
app.include_router(writing_router)
app.include_router(reading_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=True, port=8000)  # Cambia el puerto si es necesario
