import os
import shutil
from datetime import datetime
import logging

class File:
    def __init__(self, path) -> None:
        self.path = path

    def get_path(self):
        return self.path

    def get_name(self):
        return self.path[self.path.rfind("/") + 1 : self.path.rfind(".")]

    def get_full_name(self):
        return self.path[self.path.rfind("/") + 1 : ]
    
    def get_created_time(self):
        ctime = os.path.getctime(self.path)
        return datetime.fromtimestamp(ctime).strftime('%Y-%m-%d %H:%M:%S')

    def get_modified_time(self):
        mtime = os.path.getmtime(self.path)
        return datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S')

    def get_extension(self):
        return self.path[self.path.rfind(".") + 1 : ]

    def get_size(self):
        return os.path.getsize(self.path) # size in bytes

    def move(self, newPath) -> None:
        self.log(self.get_full_name() + " moved to " + newPath[ : newPath.rfind("/") + 1])
        shutil.move(self.path, newPath)
        self.path = newPath
    
    def log(self, message) -> None:
        Log_Format = "%(asctime)s - %(message)s"
        logging.basicConfig(filename = "history.log",
                            filemode = "a",
                            format = Log_Format, 
                            level = logging.INFO)
        logger = logging.getLogger()
        logger.info(message)