from unicodedata import category
from pydantic import BaseModel
from typing import Optional, List

class LegalitySchema(BaseModel):
    unlimited: bool
    standard: bool
    expanded: bool