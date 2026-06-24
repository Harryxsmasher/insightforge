from pathlib import Path

from app.modules.dataset.exceptions import (
    InvalidFileTypeException
)


class DatasetValidator:

    ALLOWED_EXTENSIONS = {
        ".csv",
        ".xlsx",
        ".xls"
    }

    @classmethod
    def validate_extension(
        cls,
        filename: str
    ):

        extension = Path(filename).suffix.lower()

        if extension not in cls.ALLOWED_EXTENSIONS:

            raise InvalidFileTypeException()