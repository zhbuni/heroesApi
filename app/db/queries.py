from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from app.db.models import Heroes, RolePresences, CounterHeroes


def get_hero(db: Session, hero: str) -> list:
    return db.scalars(select(Heroes).where(Heroes.name == hero)).first()


def get_roles(db: Session, hero_id: int) -> list:
    statement = select(RolePresences).where(RolePresences.hero_id == hero_id).options(joinedload(RolePresences.role))
    return db.scalars(statement).all()


def get_counter_heroes(db: Session, hero: str) -> list:
    # Кринж
    hero = get_hero(db, hero)
    if not hero:
        return []

    statement = (select(CounterHeroes)
                 .options(joinedload(CounterHeroes.counter_hero), joinedload(CounterHeroes.hero))
                 .where(CounterHeroes.hero_id == hero.id)
                 .order_by(CounterHeroes.winrate.desc())
                 .limit(5)
                 )
    return db.scalars(statement).all()
