from pydantic import BaseModel
from typing import Optional

from model import Resistances


class ResistanceSchema(BaseModel):
    type: Optional[str] = 'Grass'
    value: Optional[str] = '×2'


def build_resistance(resistance: Resistances):
    return {
        'type': resistance.type,
        'value': resistance.value,
    }
