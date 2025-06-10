from unicodedata import category
from pydantic import BaseModel
from typing import Optional, List

class ImageSchema (BaseModel):
    symbol: str
    logo: str
    small: str
    large: str