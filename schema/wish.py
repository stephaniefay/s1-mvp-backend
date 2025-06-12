from typing import List, Optional

from pydantic import BaseModel, Field
from model.wish import Wish



class WishSchema(BaseModel):
    id:str = '1'
    name:str = 'MyWish'
    description:str = 'Minha primeira MyWish'

class WishListSchema(BaseModel):
    sets:List[WishSchema]

class WishFetchSchema(BaseModel):
    id: int = Field(..., description='id da lista de desejos')

class NewWishSchema(BaseModel):
    name:str
    description:Optional[str]


def build_wish_list(wishs: List[Wish]):
    result = []
    for wish in wishs:
        result.append({
            "id": wish.id,
            "name": wish.name,
            "description": wish.description,
        })
    return {"sets": result}


def build_wish(wish: Wish):
    return {
        "id": wish.id,
        "name": wish.name,
        "description": wish.description
    }
