from fastapi import FastAPI
app = FastAPI()
from metodos import Search
from metodos import Insert
from pydantic import BaseModel

class Item(BaseModel):
    id: int
    name: str
    age: int

@app.get('/user')
def select_all():
    instancia = Search()
    result=instancia.search_users()
    return result


@app.get('/username/{name}')
def select_name(name):
    instancia = Search()
    result=instancia.search_name(name)
    return result


@app.get('/userid/{id}')
def select_id(id):
    instancia = Search()
    result=instancia.search_id(id)
    return result

@app.get('/userage/{age}')
def select_age(age):
    instancia = Search()
    result=instancia.search_age(age)
    return result


@app.post('/adduser/')
def adduser(usuario:Item):
    instancia = Insert()
    result = instancia.insert_into(usuario)
    return result














