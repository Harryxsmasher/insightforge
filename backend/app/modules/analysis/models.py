from datetime import datetime

from sqlalchemy import (
    DateTime,
    ForeignKey,
    Integer,
    JSON
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from app.database.base import Base


class Analysis(Base):

    __tablename__ = "analysis"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    dataset_id: Mapped[int] = mapped_column(
        ForeignKey("datasets.id")
    )

    row_count: Mapped[int] = mapped_column(
        Integer
    )

    column_count: Mapped[int] = mapped_column(
        Integer
    )

    column_names: Mapped[list] = mapped_column(
        JSON
    )

    missing_values: Mapped[dict] = mapped_column(
        JSON
    )

    data_types: Mapped[dict] = mapped_column(
        JSON
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )