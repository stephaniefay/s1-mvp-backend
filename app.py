from flask_openapi3 import OpenAPI, Info, Tag, request
from flask import redirect

from sqlalchemy.exc import IntegrityError, NoResultFound

from model import Session, Set, SetCards, Cards, WishCards, CardTypes, Type
from logger import logger
from schema import *
from flask_cors import CORS

info = Info(title="Wish", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

default_tag = Tag(name="Documentação", description="Documentação corrente da API")
set_tag = Tag(name="Coleções", description="Endpoints para visualizar as coleções")
wish_tag = Tag(name="Wish", description="Endpoints para manipular sua lista de desejos")


@app.get('/', tags=[default_tag], summary="Documentação Swagger")
def home():
    return redirect('/openapi/swagger')


@app.get('/sets', tags=[set_tag], responses={"200": SetListSchema, "204": EmptySchema, "400": ErrorSchema},
         summary="Lista todos as coleções")
def get_sets(query: SetSearchSchema):
    with Session() as session:
        if query.name:
            logger.info('searching by name')
            sets = session.query(Set).filter(Set.name.like("%{}%".format(query.name))).all()
        else:
            logger.info('get all')
            sets = session.query(Set).all()

        if not sets:
            return {'message': 'Nenhuma coleção encontrada'}, 204
        else:
            return build_set_list(sets), 200


@app.get('/sets/<string:id>/cards', tags=[set_tag],
         responses={"200": CardListSchema, "204": EmptySchema, "400": ErrorSchema},
         summary="Lista todas as cartas de uma coleção")
def get_set_cards(path: SetFetchSchema, query: SearchSchema):
    with Session() as session:
        q = session.query(SetCards).filter(SetCards.set_id == path.id)

        if query.search:
            q = q.join(SetCards.card_obj)
            q = q.filter(Cards.name.like("%{}%".format(query.search)))

        cards = q.all()

        if not cards:
            return {'message': 'Nenhuma carta encontrada'}, 204
        else:
            return build_card_list(cards, session), 200


@app.get('/wishes', tags=[wish_tag], responses={"200": WishListSchema, "204": EmptySchema, "400": ErrorSchema},
         summary="Lista todos as listas de desejo")
def get_wishes(query: WishSearchSchema):
    with Session() as session:
        if query.card_id:
            subquery = session.query(WishCards.wish_id).filter(WishCards.card_id == query.card_id)
            wishes = session.query(Wish).filter(Wish.id.not_in(subquery)).all()
        else:
            wishes = session.query(Wish).all()

        if not wishes:
            return {'message': 'Nenhuma lista de desejos encontrada'}, 204
        else:
            return build_wish_list(wishes), 200


@app.get('/wishes/<int:id>/cards', tags=[wish_tag],
         responses={"200": CardListSchema, "204": EmptySchema, "400": ErrorSchema},
         summary="Lista todas as cartas de uma lista de desejo")
def get_wish_cards(path: WishFetchSchema, query: SearchSchema):
    with Session() as session:
        q = session.query(WishCards).filter(WishCards.wish_id == path.id)

        if query.search:
            q = q.join(WishCards.card_obj)
            q = q.filter(Cards.name.like("%{}%".format(query.search)))

        cards = q.all()

        if not cards:
            return {'message': 'Nenhuma carta encontrada'}, 204
        else:
            print(cards[0].card_obj.id)
            return build_card_list(cards, session), 200


@app.post('/wishes', tags=[wish_tag], responses={"201": WishSchema, "400": ErrorSchema},
          summary="Criação de uma nova lista de desejos")
def create_wish(body: NewWishSchema):
    wish_to_create = Wish(name=body.name, description=body.description, color=body.color)

    with Session() as session:
        logger.info('trying to create wish')
        try:
            session.add(wish_to_create)
            session.commit()
            logger.info('wish created successfully')
            return build_wish(wish_to_create), 201
        except IntegrityError:
            logger.info('wish already exists')
            return {'message': 'Já existe uma lista de desejos com esse nome'}, 400


@app.put('/wishes/<int:id>', tags=[wish_tag], responses={"200": EmptySchema, "400": ErrorSchema},
         summary="Inserir cartas na lista de desejos")
def insert_card(path: WishFetchSchema, body: CardFetchSchema):
    with Session() as session:
        success = []
        for card_id in body.ids:
            try:
                card_to_insert = session.query(Cards).filter(Cards.id == card_id).one()
                if card_to_insert:
                    card_to_add = WishCards(wish_id=path.id, card_id=card_id)
                    session.add(card_to_add)
                    session.commit()
                    logger.info('card inserted successfully')
                    success.append(card_id)
            except IntegrityError:
                logger.info('wish already contains card {}'.format(card_id))

        return {'message': 'Cartas {} adicionadas com sucesso'.format(', '.join(success))}, 200


@app.delete('/wishes/<int:id>/card', tags=[wish_tag], responses={"200": EmptySchema, "400": ErrorSchema},
            summary="Remover cartas da lista de desejos")
def remove_card(path: WishFetchSchema, body: CardFetchSchema):
    with (Session() as session):
        success = []
        for card_id in body.ids:
            try:
                card_to_delete = session.query(WishCards).filter(WishCards.card_id == card_id
                                                                 ).filter(WishCards.wish_id == path.id).one()
                session.delete(card_to_delete)
                session.commit()
                success.append(card_id)
            except NoResultFound:
                logger.warn('card {} not in wish'.format(card_id))

        return {'message': 'Cartas {} removidas com sucesso'.format(', '.join(success))}, 200
