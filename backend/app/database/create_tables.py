from app.database.base import Base
from app.database.session import engine

# Import all models here
from app.modules.dataset.models import Dataset
from app.modules.analysis.models import Analysis

def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")


if __name__ == "__main__":
    create_tables()