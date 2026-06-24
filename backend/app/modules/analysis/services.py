from sqlalchemy.orm import Session

from app.modules.analysis.engine import AnalysisEngine
from app.modules.analysis.models import Analysis
from app.modules.analysis.repositories import AnalysisRepository
from app.modules.dataset.models import Dataset


class AnalysisService:

    def __init__(self):

        self.engine = AnalysisEngine()

        self.repository = AnalysisRepository()

    def analyze_dataset(
        self,
        db: Session,
        dataset: Dataset
    ):

        result = self.engine.analyze(
            dataset.file_path
        )

        analysis = Analysis(

            dataset_id=dataset.id,

            row_count=result["row_count"],

            column_count=result["column_count"],

            column_names=result["column_names"],

            missing_values=result["missing_values"],

            data_types=result["data_types"]

        )

        return self.repository.create(
            db,
            analysis
        )

    def get_analysis_by_dataset_id(
        self,
        db: Session,
        dataset_id: int
    ):

        return self.repository.get_by_dataset_id(
            db,
            dataset_id
        )