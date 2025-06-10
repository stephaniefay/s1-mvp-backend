from http.client import responses
from typing import List

from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from flask_cors import CORS

from app.api.schemas.auxiliary import EmptySchema
from app.api.schemas.card import SearchCardSchema
from app.api.schemas.set import SetSchema

info = Info(title="Wish", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

default_tag = Tag(name="Documentação", description="Documentação corrente da API")
set_tag = Tag(name="Coleções", description="Endpoints de Coleção")

@app.get('/', tags=[default_tag])
def home():
    return redirect('/openapi/swagger')

@app.get('/sets', tags=[set_tag], responses={"200": SetSchema, "204": EmptySchema})
def get_sets():

    return "Hello World", 200
