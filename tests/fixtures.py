from typing import Generator

import pytest
from alembic import command
from alembic.config import Config
from starlette.config import environ
from starlette.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database, drop_database

environ['TESTING'] = 'True'

from app.db import db_url, metadata  # noqa: E402
from app import app  # noqa: E402


@pytest.fixture(scope='session', autouse=True)
def create_test_database() -> Generator[None, None, None]:
    engine = create_engine(db_url)
    assert not database_exists(db_url), 'Test database already exists. Aborting tests.'
    create_database(db_url)  # Create the test database.
    config = Config('alembic.ini')   # Run the migrations.
    command.upgrade(config, 'head')
    metadata.create_all(engine)  # Create the tables.
    yield  # Run the tests.
    drop_database(db_url)  # Drop the test database.


@pytest.fixture()
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as client:
        yield client