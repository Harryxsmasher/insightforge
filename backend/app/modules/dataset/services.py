from sqlalchemy.orm import Session

from app.modules.dataset.models import Dataset
from app.modules.dataset.repositories import DatasetRepository
from app.modules.dataset.constants import DatasetStatus

from app.modules.dataset.exceptions import (
    DatasetNotFoundException
)


class DatasetService:

    def __init__(self):
        self.repository = DatasetRepository()

    def create_dataset(
        self,
        db: Session,
        name: str,
        filename: str,
        file_type: str,
        file_size: int,
        status: str = DatasetStatus.UPLOADING
    ) -> Dataset:

        dataset = Dataset(
            name=name,
            filename=filename,
            file_type=file_type,
            file_size=file_size,
            status=status
        )

        return self.repository.create(db, dataset)

    def get_all_datasets(self, db: Session):

        return self.repository.get_all(db)

    
    def get_dataset_by_id(
    self,
    db: Session,
    dataset_id: int
    ):

        dataset = self.repository.get_by_id(
        db,
        dataset_id
    )

        if dataset is None:

            raise DatasetNotFoundException(
                dataset_id
        )

        return dataset