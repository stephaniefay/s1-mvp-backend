from unicodedata import category
from pydantic import BaseModel
from typing import Optional, List

from app.api.schemas.image import ImageSchema
from app.api.schemas.legality import LegalitySchema


class SetSchema(BaseModel):
    id: str
    name: str
    series: str
    printedTotal: int
    legalities: LegalitySchema
    ptcgoCode: str
    releaseDate: str
    images: ImageSchema

