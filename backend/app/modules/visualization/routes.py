from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.modules.dataset.repositories import DatasetRepository
from app.modules.visualization.schemas import VisualizationResponse
from app.modules.visualization.services import VisualizationService

router = APIRouter(
    prefix="/visualizations",
    tags=["Visualizations"]
)

visualization_service = VisualizationService()
dataset_repository = DatasetRepository()


@router.post(
    "/histogram/{dataset_id}/{column}",
    response_model=VisualizationResponse
)
def create_histogram(
    dataset_id: int,
    column: str,
    db: Session = Depends(get_db)
):

    dataset = dataset_repository.get_by_id(
        db,
        dataset_id
    )

    if dataset is None:

        raise HTTPException(
            status_code=404,
            detail="Dataset not found"
        )

    return visualization_service.create_histogram(
        db,
        dataset,
        column
    )


@router.get(
    "/{dataset_id}",
    response_model=list[VisualizationResponse]
)
def get_visualizations(
    dataset_id: int,
    db: Session = Depends(get_db)
):

    return visualization_service.get_visualizations_by_dataset_id(
        db,
        dataset_id
    )