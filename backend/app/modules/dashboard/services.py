from sqlalchemy.orm import Session

from app.modules.ai.engine import AIEngine
from app.modules.dashboard.engine import DashboardEngine
from app.modules.dashboard.models import Dashboard
from app.modules.dashboard.repositories import DashboardRepository
from app.modules.dataset.models import Dataset
from app.modules.visualization.repositories import (
    VisualizationRepository
)


class DashboardService:

    def __init__(self):

        self.dashboard_engine = DashboardEngine()

        self.dashboard_repository = DashboardRepository()

        self.visualization_repository = (
            VisualizationRepository()
        )

        self.ai_engine = AIEngine()

    def create_dashboard(
        self,
        db: Session,
        dataset: Dataset
    ):

        dashboard = self.dashboard_engine.build_dashboard(
            dataset.file_path
        )

        ai_summary = self.ai_engine.summarize(
            dashboard
        )

        visualizations = (
            self.visualization_repository
            .get_by_dataset_id(
                db,
                dataset.id
            )
        )

        dashboard_json = {

            "analysis":
                dashboard["analysis"],

            "statistics":
                dashboard["statistics"],

            "ai_summary":
                ai_summary["summary"],

            "visualizations": [

                {
                    "chart_type":
                        visualization.chart_type,

                    "column_name":
                        visualization.column_name

                }

                for visualization in visualizations

            ]

        }

        dashboard_model = Dashboard(

            dataset_id=dataset.id,

            dashboard_json=dashboard_json

        )

        return self.dashboard_repository.create(
            db,
            dashboard_model
        )

    def get_dashboard_by_dataset_id(
        self,
        db: Session,
        dataset_id: int
    ):

        return self.dashboard_repository.get_by_dataset_id(
            db,
            dataset_id
        )