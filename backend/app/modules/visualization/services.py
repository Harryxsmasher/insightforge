from sqlalchemy.orm import Session

from app.modules.dataset.models import Dataset
from app.modules.visualization.engine import VisualizationEngine
from app.modules.visualization.models import Visualization
from app.modules.visualization.repositories import (
    VisualizationRepository
)


class VisualizationService:

    def __init__(self):

        self.engine = VisualizationEngine()

        self.repository = VisualizationRepository()

    def create_histogram(
        self,
        db: Session,
        dataset: Dataset,
        column: str
    ):

        chart_json = self.engine.histogram(
            dataset.file_path,
            column
        )

        visualization = Visualization(

            dataset_id=dataset.id,

            chart_type="histogram",

            column_name=column,

            chart_json=chart_json

        )

        return self.repository.create(
            db,
            visualization
        )

    def get_visualizations_by_dataset_id(
        self,
        db: Session,
        dataset_id: int
    ):

        return self.repository.get_by_dataset_id(
            db,
            dataset_id
        )