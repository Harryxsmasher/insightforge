from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.modules.analysis.schemas import (
    AnalysisResponse
)
from app.modules.analysis.services import AnalysisService
from app.modules.dataset.repositories import DatasetRepository

router = APIRouter(
    prefix="/analysis",
    tags=["Analysis"]
)

analysis_service = AnalysisService()
dataset_repository = DatasetRepository()


@router.post(
    "/{dataset_id}",
    response_model=AnalysisResponse
)
def analyze_dataset(
    dataset_id: int,
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

    return analysis_service.analyze_dataset(
        db,
        dataset
    )


@router.get(
    "/{dataset_id}",
    response_model=list[AnalysisResponse]
)
def get_analysis(
    dataset_id: int,
    db: Session = Depends(get_db)
):

    return analysis_service.get_analysis_by_dataset_id(
        db,
        dataset_id
    )