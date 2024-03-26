from typing import List

from pydantic import BaseModel, Field, ConfigDict


class HeroSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field()
    name: str = Field()


class CounterHeroSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    winrate: float = Field()
    name: str = Field()
    dotabuff_link: str = Field()


class RoleSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field()
    name: str = Field()


class RolePresenceSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    role: RoleSchema = Field()
    presence: float = Field(ge=0, le=100)
    winrate: float = Field(ge=0, le=100)


class HeroInfoSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    hero: HeroSchema = Field()
    lines: List[RolePresenceSchema] = Field()
