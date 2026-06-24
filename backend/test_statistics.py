from app.modules.statistics.engine import StatisticsEngine

engine = StatisticsEngine()

result = engine.summary(
    "app/storage/uploads/sales.csv"
)

print(result)