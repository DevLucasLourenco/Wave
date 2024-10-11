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
        self.__allKeys :str = list(self.__archive.getMetaData()['columns'].values())[0]
        self.__firstKey:str = self.__allKeys[0]
    
    
    @deltaTime
    def generate(self):
        for i, _ in enumerate(self.__archive.getData()[self.__firstKey]['data_column']):
            listageOfIndex = self.__getRecordsFromSameIndex(i)
            print(listageOfIndex)
            
    
    def __replaceInfosAtDoc(self):
        doc_base = deepcopy(self.__baseDocx)
    
    
    # mudar dicionário com o key_w/Delimiter
    def __getRecordsFromSameIndex(self, index) -> dict: 
        d_aux=dict()
        for keyHeader in self.__allKeys:
                information = self.__archive.getData()[keyHeader]['data_column'][index]
                KeyWithDelimiter = self.__archive.getData()[keyHeader]['key_w/Delimiter']
                d_aux.update({KeyWithDelimiter:information})
        return d_aux
    
    
    def buildPDFs(self):
        ...
    
    
    def getTimeToGenerate(self):
        if self._timeToGenerate:
            return self._timeToGenerate
        