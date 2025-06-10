from unicodedata import category
from pydantic import BaseModel
from typing import Optional, List

from app.api.schemas.attack import AttackSchema
from app.api.schemas.image import ImageSchema
from app.api.schemas.legality import LegalitySchema
from app.api.schemas.weakness import WeaknessSchema


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


class SearchCardSchema (BaseModel):
    set_id: Optional[str]
    wish_id: Optional[str]
    search_clause: Optional[str]