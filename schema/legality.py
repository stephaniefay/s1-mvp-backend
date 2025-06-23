from pydantic import BaseModel
from typing import Optional


class LegalitySchema(BaseModel):
    unlimited: Optional[bool] = False
    standard: Optional[bool] = False
    expanded: Optional[bool] = False


def build_legality(unlimited: int, standard: int, expanded: int):
    unlimited = bool(unlimited)
    standard = bool(standard)
    expanded = bool(expanded)

    return {
        "unlimited": unlimited,
        "standard": standard,
        "expanded": expanded,
    }
