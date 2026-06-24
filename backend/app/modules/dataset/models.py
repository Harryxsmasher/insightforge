from datetime import datetime
from sqlalchemy import String, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Dataset(Base):
    __tablename__ = "datasets"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(255))

    filename: Mapped[str] = mapped_column(String(255))

    file_type: Mapped[str] = mapped_column(String(50))

    file_size: Mapped[int] = mapped_column(Integer)

    status: Mapped[str] = mapped_column(
    String(50),
    default="UPLOADING"
)

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )