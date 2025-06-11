from pydantic import BaseModel
from typing import Optional

class LegalitySchema(BaseModel):
    unlimited: Optional[bool] = False
    standard: Optional[bool] = False
    expanded: Optional[bool] = False