from unicodedata import category
from pydantic import BaseModel
from typing import Optional, List

class AttackSchema (BaseModel):
    name: str
    cost: List[str]
    damage: str
    text: str