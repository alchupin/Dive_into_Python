class FileReader():
    def __init__(self, filepath):
        self.filepath = filepath
        
    def read(self):
        try:
            with open(self.filepath) as f:
                file_text = f.read()
                return file_text
        except IOError:
            return ""
