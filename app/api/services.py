import os
from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session
from pydantic import TypeAdapter
from dotenv import load_dotenv

from app.api.schemas import RolePresenceSchema, HeroInfoSchema, CounterHeroSchema
from app.db.queries import get_hero, get_roles, get_counter_heroes

load_dotenv()


def get_hero_info(db: Session, hero: str):
    hero = get_hero(db, hero)
    if not hero:
        raise HTTPException(404, "Hero not found")

    roles = get_roles(db, hero.id)
    lines_schema = TypeAdapter.validate_python(TypeAdapter(List[RolePresenceSchema]), roles)
    hero_schema = HeroInfoSchema(
        hero=hero,
        lines=lines_schema,
    )
    return hero_schema


def get_counter_hero_info(db: Session, hero: str):
    heroes = get_counter_heroes(db, hero)
    if not heroes:
        raise HTTPException(404, "Counter heroes not found")

    counter_heroes = [CounterHeroSchema(
        winrate=hero.winrate,
        dotabuff_link=f'{os.getenv("DOTABUFF_LINK")}{hero.counter_hero.name}',
        name=hero.counter_hero.name,
    ) for hero in heroes]

    return counter_heroes
