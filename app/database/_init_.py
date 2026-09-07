from app.database.database import engine, Base
from app.database import models


def initialize_database():
    Base.metadata.create_all(bind=engine)
    print("RDRS database initialized successfully.")


if __name__ == "__main__":
    initialize_database()