from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.api.services import get_hero_info, get_counter_hero_info

heroes_router = APIRouter()


@heroes_router.get("/info/{hero}")
def hero_info(hero: str, db: Session = Depends(get_db)):
    return get_hero_info(db, hero)


@heroes_router.get("/counter/{hero}")
def counter_hero_info(hero: str, db: Session = Depends(get_db)):
    return get_counter_hero_info(db, hero)
