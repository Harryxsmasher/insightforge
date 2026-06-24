from pathlib import Path
import shutil


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
        source_path: str,
        filename: str
    ):

        destination = self.get_upload_path(
            filename
        )

        shutil.copy(
            source_path,
            destination
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