from app.db.session import Base, engine
from app.db.base import *  # noqa: F401, F403


def initialize_database() -> None:
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    initialize_database()
    print("Database initialized")
