from app.modules.report.engine import ReportEngine


class KnowledgeEngine:

    def __init__(self):

        self.report_engine = ReportEngine()

    def build_knowledge(
        self,
        file_path: str
    ):

        report = self.report_engine.generate_report(
            file_path
        )

        knowledge = {

            "report": report

        }

        return knowledge