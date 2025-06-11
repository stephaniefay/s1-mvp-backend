from pydantic import BaseModel
from typing import Optional

class WeaknessSchema(BaseModel):
    type: Optional[str] = 'Grass'
    value: Optional[str] = '×2'