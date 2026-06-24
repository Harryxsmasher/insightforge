from sqlalchemy.orm import Session

from app.modules.dashboard.models import Dashboard


class DashboardRepository:

    def create(
        self,
        db: Session,
        dashboard: Dashboard
    ) -> Dashboard:

        db.add(dashboard)

        db.commit()

        db.refresh(dashboard)

        return dashboard

    def get_by_dataset_id(
        self,
        db: Session,
        dataset_id: int
    ):

        return (
            db.query(Dashboard)
            .filter(
                Dashboard.dataset_id == dataset_id
            )
            .all()
        )