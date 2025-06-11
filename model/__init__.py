from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text
import os

# importando os elementos definidos no modelo
from model.base import Base
from model.abilities import Abilities
from model.attacks import Attacks
from model.card_abilities import CardAbilities
from model.card_attacks import CardAttacks
from model.card_resistances import CardResistances
from model.card_subtypes import CardSubtypes
from model.card_types import CardTypes
from model.card_weaknesses import CardWeaknesses
from model.cards import Cards
from model.cost import Cost
from model.resistances import Resistances
from model.series import Series
from model.set import Set
from model.set_cards import SetCards
from model.subtype import Subtype
from model.supertype import Supertype
from model.type import Type
from model.weaknesses import Weaknesses
from model.wish_cards import WishCards

db_path = "database/"
# Verifica se o diretorio não existe
if not os.path.exists(db_path):
    # então cria o diretorio
    os.makedirs(db_path)

# url de acesso ao banco (essa é uma url de acesso ao sqlite local)
db_url = 'sqlite:///%s/db.sqlite3' % db_path

# cria a engine de conexão com o banco
engine = create_engine(db_url, echo=False)

# Instancia um criador de seção com o banco
Session = sessionmaker(bind=engine)

# cria o banco se ele não existir
empty_db = False
if not database_exists(engine.url):
    empty_db = True
    create_database(engine.url)

# cria as tabelas do banco, caso não existam
Base.metadata.create_all(engine)

if empty_db:
    with engine.connect() as connection:
        with open('database/sets.sql', 'r', encoding='utf-8') as sets:
            for line in sets:
                line = line.replace('\n', '')
                connection.execute(text(line))
                connection.commit()
        sets.close()

        with open('database/cards.sql', 'r', encoding='utf-8') as cards:
            for line in cards:
                line = line.replace('\n', '')
                connection.execute(text(line))
                connection.commit()
        cards.close()


