from random import randint

from app.db.models import Heroes, CounterHeroes


def test_get_hero_empty_result(client):
    response = client.get("/counter/axe")
    assert response.status_code == 404


def test_get_hero(client, db_session):
    hero = Heroes(name="axe", id=randint(1, 1000))
    counter_hero = Heroes(name="ursa", id=randint(1, 1000))
    db_session.add(CounterHeroes(
        hero_id=hero.id,
        counter_hero_id=counter_hero.id,
        winrate=53.1,
    ))
    db_session.add(hero)
    db_session.add(counter_hero)
    db_session.commit()
    response = client.get("/counter/axe")
    assert response.status_code == 200
    assert response.json() == [
        {
            'dotabuff_link': 'https://ru.dotabuff.com/heroes/ursa',
            'name': 'ursa',
            'winrate': 53.1,
        }
    ]
