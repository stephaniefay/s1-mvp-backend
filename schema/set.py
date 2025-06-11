from pydantic import BaseModel
from typing import Optional, List
from model.set import Set
from schema import build_legality, build_images_set

from schema.image import ImageSchema
from schema.legality import LegalitySchema


class SetSchema(BaseModel):
    id:str = "SV10"
    name:str = "Destined Rivals"
    series:str = "Scarlet & Violet"
    printedTotal: int = 0
    legalities: Optional[LegalitySchema]
    ptcgoCode: str =  "DRI"
    releaseDate: str = "2025/05/30"
    images: Optional[ImageSchema]

class SetSearchSchema(BaseModel):
    id: str = "SV10"
    name: str = "Destined Rivals"


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
