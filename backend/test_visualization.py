from app.modules.visualization.engine import (
    VisualizationEngine
)

engine = VisualizationEngine()

chart = engine.histogram(
    "app/storage/uploads/sales.csv",
    "Price"
)

print(chart)