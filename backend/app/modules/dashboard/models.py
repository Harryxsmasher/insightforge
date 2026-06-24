from datetime import datetime

from sqlalchemy import (
    DateTime,
    ForeignKey,
    JSON
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from app.database.base import Base


class Dashboard(Base):

    __tablename__ = "dashboards"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    dataset_id: Mapped[int] = mapped_column(
        ForeignKey("datasets.id")
    )

    dashboard_json: Mapped[dict] = mapped_column(
        JSON
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )