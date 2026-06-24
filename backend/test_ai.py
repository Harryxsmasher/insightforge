from app.modules.dashboard.engine import DashboardEngine
from app.modules.ai.engine import AIEngine


dashboard_engine = DashboardEngine()

dashboard = dashboard_engine.build_dashboard(
    "app/storage/uploads/sales.csv"
)

ai_engine = AIEngine()

result = ai_engine.summarize(
    dashboard
)

print(result)