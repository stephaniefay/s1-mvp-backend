from pydantic import BaseModel
from typing import Optional

class ImageSchema (BaseModel):
    symbol: Optional[str] = ''
    logo: Optional[str] = ''
    small: Optional[str] = ''
    large: Optional[str] = ''