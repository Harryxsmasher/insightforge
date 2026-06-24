from app.modules.report.engine import ReportEngine

engine = ReportEngine()

report = engine.generate_report(
    "app/storage/uploads/sales.csv"
)

print(report)