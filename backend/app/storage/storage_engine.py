from pathlib import Path

from fastapi import UploadFile


class StorageEngine:

    ALLOWED_EXTENSIONS = {
        ".csv",
        ".xlsx",
        ".xls"
    }

    UPLOAD_DIRECTORY = Path(
        "app/storage/uploads"
    )

    def __init__(self):

        self.UPLOAD_DIRECTORY.mkdir(
            parents=True,
            exist_ok=True
        )

    def is_valid_extension(
        self,
        filename: str
    ) -> bool:

        extension = Path(filename).suffix.lower()

        return extension in self.ALLOWED_EXTENSIONS

    def get_upload_path(
        self,
        filename: str
    ) -> Path:

        return self.UPLOAD_DIRECTORY / filename

    def save_file(
        self,
        upload_file: UploadFile
    ) -> Path:

        destination = self.get_upload_path(
            upload_file.filename
        )

        with destination.open(
            "wb"
        ) as buffer:

            buffer.write(
                upload_file.file.read()
            )

        return destination

    def delete_file(
        self,
        filename: str
    ):

        path = self.get_upload_path(
            filename
        )

        if path.exists():

            path.unlink()