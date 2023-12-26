from utils import validation


class FileWriter:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode
        validation.validate_file(path)

    def write(self, data: str):
        print(f"Writing to: {self.path} in {self.mode} mode")
