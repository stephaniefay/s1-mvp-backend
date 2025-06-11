from pydantic import BaseModel
from typing import Optional

class ImageSchema (BaseModel):
    symbol: Optional[str] = ''
    logo: Optional[str] = ''
    small: Optional[str] = ''
    large: Optional[str] = ''

def build_images_set(symbol:str, logo:str):
    return {
        'symbol': symbol,
        'logo': logo
    }

def build_images_card(small:str, large:str):
    return {
        'small': small,
        'large': large
    }