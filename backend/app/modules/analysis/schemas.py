from datetime import datetime

from pydantic import BaseModel


class AnalysisResponse(BaseModel):

    id: int

    dataset_id: int

    row_count: int

    column_count: int

    column_names: list[str]

    missing_values: dict

    data_types: dict
    

    created_at: datetime

    class Config:

        from_attributes = True

class AnalysisListResponse(BaseModel):

    analyses: list[AnalysisResponse]