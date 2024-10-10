import time
from py.service.data.archive import Archive

def deltaTime(method):
    def wrapper(self, *args, **kwargs):
        initialTime = time.now()
        mtd = method(self, *args, **kwargs)
        self.timeToGenerate = time.now() - initialTime
        return mtd
    
    return wrapper

class Generate:
    
    def __init__(self, data:Archive) -> None:
        self.data = data
        self.timeToGenerate:int
        self.base_docx = None
        
    
    @deltaTime
    def generate(self):
        ...
        
        
 
        
        