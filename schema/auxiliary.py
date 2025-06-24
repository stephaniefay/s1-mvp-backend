from pydantic import BaseModel, Field
from typing import Optional


class EmptySchema(BaseModel):
    message: str


class ErrorSchema(BaseModel):
    code: int
    message: str


class SearchSchema(BaseModel):
    search: Optional[str] = Field(None, description='termo a ser buscado')
