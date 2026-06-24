from app.modules.dashboard.engine import DashboardEngine
from app.modules.ai.engine import AIEngine


class ReportEngine:

    def __init__(self):

        self.dashboard_engine = DashboardEngine()

        self.ai_engine = AIEngine()

    def generate_report(
        self,
        file_path: str
    ):

        dashboard = self.dashboard_engine.build_dashboard(
            file_path
        )

        ai_summary = self.ai_engine.summarize(
            dashboard
        )

        analysis = dashboard["analysis"]

        statistics = dashboard["statistics"]

        report = f"""
# Dataset Report

## Overview

Rows: {analysis["row_count"]}

Columns: {analysis["column_count"]}

Column Names:

{", ".join(analysis["column_names"])}

## AI Summary

{ai_summary["summary"]}

## Statistics

Mean Values:

{statistics["mean"]}

Median Values:

{statistics["median"]}

Minimum Values:

{statistics["min"]}

Maximum Values:

{statistics["max"]}

"""

        return report