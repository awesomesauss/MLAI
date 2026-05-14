import sys
import os


class FileHandler:
    def __init__(self, filepath):
        self.filepath = filepath

    def filesize(self):
        """Return file size in bytes."""
        return os.path.getsize(self.filepath)

    def read(self):
        """Child classes must implement this method."""
        raise NotImplementedError("Subclasses must implement read()")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 FileHandler.py <file_path>")
        return

    filepath = sys.argv[1]

    if not os.path.exists(filepath):
        print("Error: File does not exist")
        return

    ext = os.path.splitext(filepath)[1].lower()

    from JsonFile import JsonFile
    from CsvFile import CsvFile
    from LogFile import LogFile

    # TODO:
    # Choose the correct child class based on file extension
    # .json -> JsonFile
    # .csv  -> CsvFile
    # .log  -> LogFile
    # otherwise raise an exception

    # Write your code here
    if ext == '.json':
        handler = JsonFile(filepath)
    elif ext == '.csv':
        return CsvFile(filepath)
    elif ext == '.log':
        return LogFile(filepath)
    else:
        raise Exception (f"This is not a valid file extension. {ext}")
        
    print("=== File Handler ===")
    print("File:", filepath)
    print("Size (bytes):", handler.filesize())
    print("\n--- Content ---")
    print(handler.read())


if __name__ == "__main__":
    main()
