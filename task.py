from directory import Directory
from file import File

from rules.keyword_rule import KeywordRule
from rules.extension_rule import ExtensionRule
from rules.size_rule import SizeRule
from rules.created_time_rule import CreatedTimeRule
from rules.modified_time_rule import ModifiedTimeRule


class Task:
    def __init__(self, sourceDirectoryPath, destinationDirectoryPath) -> None:
        self.sourceDirectory = Directory(sourceDirectoryPath)
        self.destinationDirectory = Directory(destinationDirectoryPath)
        self.files = self.sourceDirectory.get_contents()
        self.rules = []

    def match_all_rules(self, file: File) -> bool:
        for rule in self.rules:
            if not rule.match(file):
                return False
        return True
    
    def seive(self) -> None:
        temp_files = []

        for file in self.files:
            if self.match_all_rules(file):
                temp_files.append(file)
        
        self.files = temp_files
    
    def move_all_files_to_destination_directory(self) -> None:
        for file in self.files:
            destinationFilePath = self.destinationDirectory.path + "/" + file.get_full_name()
            file.move(destinationFilePath)
    
    def run(self) -> None:
        self.seive()
        self.move_all_files_to_destination_directory()
    
    def add_keyword_rule(self, keywords) -> None:
        self.rules.append(KeywordRule(keywords))
    
    def add_extension_rule(self, extensions) -> None:
        self.rules.append(ExtensionRule(extensions))

    def add_greater_size_rule(self, size) -> None:
        self.rules.append(SizeRule("greater", size))
    
    def add_less_size_rule(self, size) -> None:
        self.rules.append(SizeRule("less", size))
    
    def add_on_created_time_rule(self, date) -> None:
        self.rules.append(CreatedTimeRule("on", date))
    
    def add_before_created_time_rule(self, date) -> None:
        self.rules.append(CreatedTimeRule("before", date))
    
    def add_after_created_time_rule(self, date) -> None:
        self.rules.append(CreatedTimeRule("after", date))
    
    def add_between_created_time_rule(self, startDate, endDate) -> None:
        self.rules.append(CreatedTimeRule("between", startDate, endDate))
    
    def add_on_modified_time_rule(self, date) -> None:
        self.rules.append(ModifiedTimeRule("on", date))
    
    def add_before_modified_time_rule(self, date) -> None:
        self.rules.append(ModifiedTimeRule("before", date))
    
    def add_after_modified_time_rule(self, date) -> None:
        self.rules.append(ModifiedTimeRule("after", date))
    
    def add_between_modified_time_rule(self, startDate, endDate) -> None:
        self.rules.append(ModifiedTimeRule("between", startDate, endDate))