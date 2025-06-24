from pydantic import BaseModel, Field
from typing import Optional, List

from model import Session, Cost, Cards
from schema.ability import AbilitySchema, build_ability
from schema.attack import AttackSchema, build_attack
from schema.image import ImageSchema, build_images_card
from schema.legality import LegalitySchema, build_legality
from schema.resistance import build_resistance
from schema.weakness import WeaknessSchema, build_weakness


class CardSchema(BaseModel):
    id: str
    name: str
    supertype: str
    subtypes: List[str]
    hp: int
    types: List[str]
    attacks: List[AttackSchema]
    weaknesses: List[WeaknessSchema]
    retreatCost: List[str]
    number: str
    rarity: str
    legalities: LegalitySchema
    images: ImageSchema
    abilities: List[AbilitySchema]


class CardListSchema(BaseModel):
    cards: List[CardSchema]


class CardQuery(BaseModel):
    set_id: Optional[str]
    wish_id: Optional[str]
    search_clause: Optional[str]


class CardFetchSchema(BaseModel):
    ids: List[str] = Field(..., description='id da carta')


def build_card_list(cards: List[any], session: Session):
    result = []
    for card in cards:
        card_to_build = card.card_obj

        result.append(build_card(card_to_build, session))

    return {"cards": result}


def build_card(card: Cards, session: Session):
    if card:
        costs = (session.query(Cost).filter(Cost.id_ref == card.id).filter(Cost.type_ref == 'card').order_by(Cost.order)
                 .all())

        return {
            "id": card.id,
            "name": card.name,
            "supertype": card.supertype_obj.type,
            "subtypes": [d.subtype_obj.type for d in card.subtype_obj],
            "hp": card.hp,
            "types": [d.type_obj.type for d in card.type_obj],
            "rules": [card.rules],
            "attacks": [build_attack(d.attack_obj, session) for d in card.attack_obj],
            "weaknesses": [build_weakness(d.weakness_obj) for d in card.weakness_obj],
            "resistances": [build_resistance(d.resistance_obj) for d in card.resistance_obj],
            "retreatCost": [d.type for d in costs],
            "number": card.number,
            "rarity": card.rarity,
            "legalities": build_legality(card.unlimited, card.standard, card.expanded),
            "images": build_images_card(card.image_sm, card.image_lg),
            "abilities": [build_ability(d.ability_obj) for d in card.ability_obj],
        }
    else:
        return None
