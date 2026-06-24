from app.modules.analysis.engine import AnalysisEngine
from app.modules.statistics.engine import StatisticsEngine
from app.modules.visualization.engine import VisualizationEngine


class DashboardEngine:

    def __init__(self):

        self.analysis_engine = AnalysisEngine()

        self.statistics_engine = StatisticsEngine()

        self.visualization_engine = VisualizationEngine()

    def build_dashboard(
        self,
        file_path: str
    ):

        analysis = self.analysis_engine.analyze(
            file_path
        )

        statistics = self.statistics_engine.summary(
            file_path
        )

        dashboard = {

            "analysis": analysis,

            "statistics": statistics

        }

        return dashboard