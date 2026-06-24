from datetime import datetime

from pydantic import BaseModel


class DashboardResponse(BaseModel):

    id: int

    dataset_id: int

    dashboard_json: dict

    created_at: datetime

    class Config:

        from_attributes = True