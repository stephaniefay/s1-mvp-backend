from pydantic import BaseModel
from typing import Optional, List

from schema.attack import AttackSchema
from schema.image import ImageSchema
from schema.legality import LegalitySchema
from schema.weakness import WeaknessSchema


class CardSchema (BaseModel):
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


class CardQuery (BaseModel):
    set_id: Optional[str]
    wish_id: Optional[str]
    search_clause: Optional[str]