from pydantic import BaseModel
from typing import Optional, List

from model import Attacks, Session, Cost


class AttackSchema (BaseModel):
    name: str = 'Night Joker'
    cost: Optional[List[str]] = ["Darkness", "Darkness"]
    damage: Optional[str] = ''
    text: Optional[str] = "Choose 1 of your Benched N's Pokémon's attacks and use it as this attack."

def build_attack(attack: Attacks, session:Session):
    costs = (session.query(Cost).filter(Cost.id_ref == attack.id).filter(Cost.type_ref == 'attack').order_by(Cost.order)
             .all())

    return {
        'name': attack.name,
        'cost': [d.type for d in costs],
        'damage': attack.damage,
        'text': attack.text
    }