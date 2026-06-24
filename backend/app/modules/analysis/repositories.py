from sqlalchemy.orm import Session

from app.modules.analysis.models import Analysis


class AnalysisRepository:

    def create(
        self,
        db: Session,
        analysis: Analysis
    ) -> Analysis:

        db.add(analysis)

        db.commit()

        db.refresh(analysis)

        return analysis

    def get_by_dataset_id(
        self,
        db: Session,
        dataset_id: int
    ):

        return (
            db.query(Analysis)
            .filter(
                Analysis.dataset_id == dataset_id
            )
            .all()
        )