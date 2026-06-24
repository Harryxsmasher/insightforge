from sqlalchemy.orm import Session

from app.modules.visualization.models import Visualization


class VisualizationRepository:

    def create(
        self,
        db: Session,
        visualization: Visualization
    ) -> Visualization:

        db.add(visualization)

        db.commit()

        db.refresh(visualization)

        return visualization

    def get_by_dataset_id(
        self,
        db: Session,
        dataset_id: int
    ):

        return (
            db.query(Visualization)
            .filter(
                Visualization.dataset_id == dataset_id
            )
            .all()
        )