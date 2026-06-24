from app.modules.dashboard.engine import DashboardEngine

engine = DashboardEngine()

dashboard = engine.build_dashboard(
    "app/storage/uploads/sales.csv"
)

print(dashboard)