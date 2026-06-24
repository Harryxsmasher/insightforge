from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.modules.dashboard.schemas import (
    DashboardResponse
)
from app.modules.dashboard.services import (
    DashboardService
)
from app.modules.dataset.repositories import (
    DatasetRepository
)

router = APIRouter(

    prefix="/dashboard",

    tags=["Dashboard"]

)

dashboard_service = DashboardService()

dataset_repository = DatasetRepository()


@router.post(
    "/{dataset_id}",
    response_model=DashboardResponse
)
def create_dashboard(
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

    return dashboard_service.create_dashboard(
        db,
        dataset
    )


@router.get(
    "/{dataset_id}",
    response_model=list[DashboardResponse]
)
def get_dashboard(
    dataset_id: int,
    db: Session = Depends(get_db)
):

    return dashboard_service.get_dashboard_by_dataset_id(
        db,
        dataset_id
    )