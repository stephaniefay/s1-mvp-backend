from pydantic import BaseModel
from typing import Optional, List

from model import Abilities


class AbilitySchema(BaseModel):
    name: str = ''
    text: str = ''
    type: str = ''


def build_ability(ability: Abilities):
    return {
        'name': ability.name,
        'text': ability.text,
        'type': ability.type
    }
