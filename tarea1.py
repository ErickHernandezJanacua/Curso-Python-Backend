from fastapi import FastAPI

app = FastAPI()


@app.get("/tarea-1")
def get_tarea1():
    return {"respuesta": "Primer tarea realizada"}
