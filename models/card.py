from pydantic import BaseModel


class Card(BaseModel):
    id: int
    name: str
    icon: str
    cost: int
    rarity: str
    type: str
    arena: int
    hash: str

    class Config:
        extra = 'forbid'
