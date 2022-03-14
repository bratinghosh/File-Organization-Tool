from file import File

class ExtensionRule:
    def __init__(self, extensions) -> None:
        self.extensions = extensions # [string]
    
    def match(self, file: File) -> bool:
        for extension in self.extensions:
            if extension == file.get_extension():
                return True
        return False