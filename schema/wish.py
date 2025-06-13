from typing import List, Optional

from pydantic import BaseModel, Field
from model.wish import Wish


class WishSchema(BaseModel):
    id: str = '1'
    name: str = 'MyWish'
    description: str = 'Minha primeira MyWish'
    color: Optional[str] = '#ffffff'


class WishListSchema(BaseModel):
    wishs: List[WishSchema]


class WishFetchSchema(BaseModel):
    id: int = Field(..., description='id da lista de desejos')

class WishSearchSchema(BaseModel):
    card_id: Optional[str] = Field(None, description='id da carta')



class NewWishSchema(BaseModel):
    name: str
    description: Optional[str]
    color: Optional[str] = Field(None, description='cor em código hexadecimal')


def build_wish_list(wishes: List[Wish]):
    result = []
    for wish in wishes:
        result.append({
            "id": wish.id,
            "name": wish.name,
            "description": wish.description,
            "color": wish.color,
        })
    return {"wishes": result}


def build_wish(wish: Wish):
    return {
        "id": wish.id,
        "name": wish.name,
        "description": wish.description,
        "color": wish.color,
    }
