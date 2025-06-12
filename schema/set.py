from pydantic import BaseModel, Field
from typing import Optional, List
from model.set import Set
from schema import build_legality, build_images_set

from schema.image import ImageSchema
from schema.legality import LegalitySchema


class SetSchema(BaseModel):
    id:str = ''
    name:str = ''
    series:str = ''
    printedTotal: int
    legalities: Optional[LegalitySchema]
    ptcgoCode: str =  ''
    releaseDate: str = ''
    images: Optional[ImageSchema]

class SetFetchSchema(BaseModel):
    id: str = Field(..., description='id da coleção')

class SetSearchSchema(BaseModel):
    name: Optional[str] = Field(None, description='nome da coleção')


class SetListSchema(BaseModel):
    sets:List[SetSchema]


def build_set_list(sets: List[Set]):
    result = []
    for set in sets:
        result.append({
            "id": set.id,
            "name": set.name,
            "series": set.series_obj.name,
            "printedTotal": set.collection_total,
            "legalities": build_legality(set.unlimited, set.standard, set.expanded),
            "ptcgoCode": set.ptcgo_code,
            "releaseDate": set.release_date,
            "images":build_images_set(set.image_symbol, set.image_logo)
        })
    return {"sets": result}


def build_set(set: Set):
    return {
        "id": set.id,
        "name": set.name,
        "series": set.series_obj.name,
        "printedTotal": set.collection_total,
        "legalities": build_legality(set.unlimited, set.standard, set.expanded),
        "ptcgoCode": set.ptcgo_code,
        "releaseDate": set.release_date,
        "images":build_images_set(set.image_symbol, set.image_logo)
    }
