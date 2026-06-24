from datetime import datetime

from pydantic import BaseModel


class VisualizationResponse(BaseModel):

    id: int

    dataset_id: int

    chart_type: str

    column_name: str

    chart_json: dict

    created_at: datetime

    class Config:

        from_attributes = True