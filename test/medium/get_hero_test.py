from app.db.models import Heroes


def test_get_hero_empty_result(client):
    response = client.get("/info/axe")
    assert response.status_code == 404


def test_get_hero(client, db_session):
    hero = Heroes(name="axe")
    db_session.add(hero)
    db_session.commit()
    response = client.get("/info/axe")
    assert response.status_code == 200
    assert response.json() == {'hero': {'id': 1, 'name': 'axe'}, 'lines': []}

