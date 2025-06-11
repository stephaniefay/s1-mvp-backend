from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Set
from logger import logger
from schema import *
from flask_cors import CORS

info = Info(title="Wish", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

default_tag = Tag(name="Documentação", description="Documentação corrente da API")
set_tag = Tag(name="Coleções", description="Endpoints de Coleção")

@app.get('/', tags=[default_tag])
def home():
    return redirect('/openapi/swagger')

@app.get('/sets', tags=[set_tag], responses={"200": SetSchema})
def get_sets():
    session = Session()
    session.query(SetSchema).filter(SetSchema.id == 2).first()

    return build_set(set), 200