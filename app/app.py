from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from flask_cors import CORS

info = Info(title="Wish", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

default_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger")

@app.get('/', tags=[default_tag])
def home():
    return redirect('/openapi/swagger')

@app.get('/produtos')
def get_produtos():

    return "Hello World", 200
