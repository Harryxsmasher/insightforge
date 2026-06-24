from sqlalchemy.orm import Session

from app.modules.dataset.models import Dataset
from app.modules.dataset.repositories import DatasetRepository
from app.modules.dataset.constants import DatasetStatus

from app.modules.dataset.exceptions import (
    DatasetNotFoundException
)

from fastapi import UploadFile

from app.storage.storage_engine import StorageEngine
from app.modules.dataset.validators import DatasetValidator


class DatasetService:

    def __init__(self):

        self.repository = DatasetRepository()

        self.storage_engine = StorageEngine()

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
    

    
    def upload_dataset(
        self,
        db: Session,
        file: UploadFile
    ):

        DatasetValidator.validate_extension(
            file.filename
        )

        file_path = self.storage_engine.save_file(
            file
        )

        dataset = Dataset(

            name=file.filename,

            filename=file.filename,

            file_path=str(file_path),

            file_type=file.filename.split(".")[-1],

            file_size=file.size,

            status=DatasetStatus.UPLOADING

        )

        return self.repository.create(
            db,
            dataset
        )