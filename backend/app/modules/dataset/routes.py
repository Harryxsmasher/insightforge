from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.modules.dataset.schemas import (
    DatasetCreate,
    DatasetResponse
)
from app.modules.dataset.services import DatasetService
from fastapi import UploadFile, File

router = APIRouter(
    prefix="/datasets",
    tags=["Datasets"]
)

service = DatasetService()

# @router.post("/upload")
@router.post(
    "/upload",
    response_model=DatasetResponse
)
def upload_dataset(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    return service.upload_dataset(
        db,
        file
    )

@router.post(
    "/",
    response_model=DatasetResponse
)
def create_dataset(
    dataset: DatasetCreate,
    db: Session = Depends(get_db)
):

    return service.create_dataset(
        db=db,
        name=dataset.name,
        filename=dataset.filename,
        file_type=dataset.file_type,
        file_size=dataset.file_size
    )


@router.get(
    "/",
    response_model=list[DatasetResponse]
)
def get_all_datasets(
    db: Session = Depends(get_db)
):

    return service.get_all_datasets(db)


@router.get(
    "/{dataset_id}",
    response_model=DatasetResponse
)
def get_dataset_by_id(
    dataset_id: int,
    db: Session = Depends(get_db)
):

    return service.get_dataset_by_id(
        db,
        dataset_id
    )

