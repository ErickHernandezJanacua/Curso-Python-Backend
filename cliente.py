import requests

URL_BASE = "http://127.0.0.1:8000"


def get_tarea1():
    respuesta = requests.get(URL_BASE + "/tarea-1")
    print(respuesta.json())


if __name__ == "__main__":
    get_tarea1()