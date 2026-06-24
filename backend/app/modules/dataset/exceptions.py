class DatasetNotFoundException(Exception):

    def __init__(self, dataset_id: int):

        self.message = (
            f"Dataset with id {dataset_id} not found."
        )

        super().__init__(self.message)


class InvalidFileTypeException(Exception):

    def __init__(self):

        self.message = (
            "Invalid file type."
        )

        super().__init__(self.message)


class FileStorageException(Exception):

    def __init__(self):

        self.message = (
            "Failed to store file."
        )

        super().__init__(self.message)