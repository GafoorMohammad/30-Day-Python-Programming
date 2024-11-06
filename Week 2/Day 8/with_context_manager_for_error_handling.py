# Using context manager to handle file errors
class FileOpener:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"Error: {exc_val}")
        self.file.close()

with FileOpener("sample.txt", "r") as file:
    content = file.read()
    print(content)
