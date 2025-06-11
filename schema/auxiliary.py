from pydantic import BaseModel

class EmptySchema (BaseModel):
    message: str


class ErrorSchema (BaseModel):
    code: int
    message: str