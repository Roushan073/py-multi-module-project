from utils import validation


class FileReader:
    def __init__(self, path):
        self.path = path
        validation.validate_file(path)

    def read(self):

        print("Reading file: \n" + self.path)


if __name__ == "__main__":
    fr = FileReader("")
    fr.read()
