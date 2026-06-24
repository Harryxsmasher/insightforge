from app.modules.analysis.engine import AnalysisEngine

engine = AnalysisEngine()

result = engine.analyze(
    "app/storage/uploads/sales.csv"
)

print(result)