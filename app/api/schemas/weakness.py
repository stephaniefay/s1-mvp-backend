from unicodedata import category
from pydantic import BaseModel
from typing import Optional, List

class WeaknessSchema(BaseModel):
    type: str
    value: str