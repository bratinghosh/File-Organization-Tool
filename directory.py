import os
from file import File

class Directory:
    def __init__(self, path) -> None:
        self.path = path
    
    def get_contents(self):
        files = []

        for fileName in os.listdir(self.path):
            filePath = self.path + "/" + fileName
            files.append(File(filePath))
            
        return files