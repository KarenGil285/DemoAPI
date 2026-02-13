from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app=FastAPI()
#CORS: Mecanismo de seguridad, si desde mi pagina web quiero acceder a una API, normalmente bloquea las 
# peticiones de afuera, pero con esto se habilitan peticiones desde clientes que no estan en el dominio. 
# Debe hacerse de manera explicita Middleware, es el que se impone entre la API y el programa
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods = ["*"],
    allow_headers=["*"]
)
@app.get("/sumar")
def sumar_numeros(a:float,b:float):
    return a+b
@app.get("/restar")
def restar_numeros(c:float,d:float):
    return c-d