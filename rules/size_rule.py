from file import File

class SizeRule:
    def __init__(self, type, size) -> None:
        self.type = type # greater or less
        self.size = size
    
    def match(self, file: File) -> bool:
        if self.type == "greater":
            if int(file.get_size()) >= int(self.size):
                return True
        
        if self.type == "less":
            if int(file.get_size()) <= int(self.size):
                return True
                
        return False