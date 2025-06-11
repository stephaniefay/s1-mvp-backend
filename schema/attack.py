from pydantic import BaseModel
from typing import Optional, List


class AttackSchema (BaseModel):
    name: str = 'Night Joker'
    cost: List[str] = ["Darkness", "Darkness"]
    damage: Optional[str] = ''
    text: Optional[str] = "Choose 1 of your Benched N's Pokémon's attacks and use it as this attack."