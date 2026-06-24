from datetime import datetime
from pydantic import BaseModel

class DatasetCreate(BaseModel):
    name: str
    filename: str
    file_type: str
    file_size: int
    file_path: str



class DatasetResponse(BaseModel):
    id: int
    name: str
    filename: str
    file_path: str
    file_type: str
    file_size: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True