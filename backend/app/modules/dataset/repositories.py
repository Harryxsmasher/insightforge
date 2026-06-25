from sqlalchemy.orm import Session

from app.modules.dataset.models import Dataset

 
class DatasetRepository:

    def create(self, db: Session, dataset: Dataset) -> Dataset:
        db.add(dataset)
        db.commit()
        db.refresh(dataset)

        return dataset

    def get_all(self, db: Session):
        return db.query(Dataset).all()

    def get_by_id(self, db: Session, dataset_id: int):
        return db.query(Dataset).filter(
            Dataset.id == dataset_id
        ).first()