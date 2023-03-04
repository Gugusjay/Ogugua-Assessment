import pytest
from app import app, db
from models import planets, stars

@pytest.fixture(scope='module')
def test_client():
    flask_app = app.create_app('test')
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client

@pytest.fixture(scope='module')
def init_database():
    db.create_all()
    planets = Planet(name="Kepler-186f", mass="1.11", radius="1.11", star_name="Kepler-186", discovery_year="2014")
    stars = Star(name="Kepler-186", temperature="3755")
    db.session.add(planet)
    db.session.add(stars)
    db.session.commit()
    yield db
    db.drop_all()

def test_home_page(test_client):
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"NASA Exoplanet Search" in response.data

def test_search_page(test_client, init_database):
    response = test_client.get('/search?planet_name=Kepler-186f')
    assert response.status_code == 200
    assert b"Results for planet Kepler-186f" in response.data

def test_invalid_search(test_client):
    response = test_client.get('/search?planet_name=InvalidName')
    assert response.status_code == 404
    assert b"404 Not Found" in response.data
