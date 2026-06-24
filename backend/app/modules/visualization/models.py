from datetime import datetime

from sqlalchemy import (
    DateTime,
    ForeignKey,
    String,
    JSON
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from app.database.base import Base


class Visualization(Base):

    __tablename__ = "visualizations"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    dataset_id: Mapped[int] = mapped_column(
        ForeignKey("datasets.id")
    )

    chart_type: Mapped[str] = mapped_column(
        String(50)
    )

    column_name: Mapped[str] = mapped_column(
        String(255)
    )

    chart_json: Mapped[dict] = mapped_column(
        JSON
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )