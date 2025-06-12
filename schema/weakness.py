from pydantic import BaseModel
from typing import Optional

from model import Weaknesses

class WeaknessSchema(BaseModel):
    type: Optional[str] = 'Grass'
    value: Optional[str] = '×2'

def build_weakness(weakness: Weaknesses):
    return {
        'type': weakness.type,
        'value': weakness.value,
    }