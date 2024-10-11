import time
from service.data.archive import Archive


def deltaTime(method):
    def wrapper(self, *args, **kwargs):
        initialTime = time.time()
        mtd = method(self, *args, **kwargs)
        self._timeToGenerate = time.time() - initialTime
        return mtd
    return wrapper


class Generate:
    
    def __init__(self, data:Archive) -> None:
        self.__data = data
        self._timeToGenerate:int
        self.__baseDocx = None
        
    
    @deltaTime
    def generate(self):
        ...
        
        
    def inputPatternDocx(self):
        ...
    
        
    def buildPDFs(self, ):
        ...
    
    
    def getTimeToGenerate(self):
        return self._timeToGenerate
        