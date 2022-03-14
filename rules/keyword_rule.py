from file import File

class KeywordRule:
    def __init__(self, keywords) -> None:
        self.keywords = keywords # [string]
    
    def match(self, file: File) -> bool:
        for keyword in self.keywords:
            if keyword in file.get_name():
                return True
        return False