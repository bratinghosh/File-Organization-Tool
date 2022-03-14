from file import File

class ModifiedTimeRule:
    def __init__(self, type, date) -> None:
        self.type = type # on, before, after
        self.date = date
    
    def __init__(self, startDate, endDate) -> None:
        self.type = "between"
        self.startDate = startDate
        self.endDate = endDate
    
    def match(self, file: File) -> bool:
        if self.type == "on":
            if file.get_modified_time() == self.date:
                return True
        
        if self.type == "before":
            if file.get_modified_time() < self.date:
                return True

        if self.type == "after":
            if file.get_modified_time() > self.date:
                return True
        
        if self.type == "between":
            if self.startDate <= file.get_modified_time() and file.get_modified_time() <= self.endDate:
                return True

        return False