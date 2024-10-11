import time
from copy import deepcopy

import docx
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

from service.data.archive import Archive


def deltaTime(method):
    def wrapper(self, *args, **kwargs):
        initialTime = time.time()
        mtd = method(self, *args, **kwargs)
        self._timeToGenerate = time.time() - initialTime
        return mtd
    return wrapper


class Generate:
    
    def __init__(self, archive:Archive, baseDocx) -> None:
        self.__archive = archive
        self._timeToGenerate:int
        self.__baseDocx = docx.Document(baseDocx)
        
    
    @deltaTime
    def generate(self):
        ...        
                
        # for par in doc_base.paragraphs:
        #     for key, value in 
    
    def __replaceInfos(self):
        doc_base = deepcopy(self.__baseDocx)
        
    
    def buildPDFs(self):
        ...
    
    
    def getTimeToGenerate(self):
        if self._timeToGenerate:
            return self._timeToGenerate
        