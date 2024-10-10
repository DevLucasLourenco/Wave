import pandas as pd

from py.service.data.archive import Archive


class DataDeal: # fazer teste de quando nao estiver a mesma quantidade nas colunas do excel o que vai acontecer 
    TYPE_DATA_ALLOWED:dict
    
    def __init__(self, fileReceived) -> None:
        DataDeal.TYPE_DATA_ALLOWED = {'csv':DataDeal.__caseCSV,
                                      'xlsx':DataDeal.__caseXLSX,
                                      'json':DataDeal.__caseJSON}
        self.fileReceived = Archive(fileReceived)
        
    def getFile(self):
        return self.fileReceived

    def readFile(self):
        typeOf = self.fileReceived.getFileType()
        
        if typeOf in DataDeal.TYPE_DATA_ALLOWED.keys():
            self.fileReceived.setDataframe(
                DataDeal.TYPE_DATA_ALLOWED[typeOf](
                    self.fileReceived.getDesignatedFile()
                    )
                )
            
        elif typeOf not in DataDeal.TYPE_DATA_ALLOWED.keys():
            raise KeyError('Non Allowed Extension')
        
    def __caseCSV(file):
        return pd.read_csv(file, sep='\t') ## fazer possíveis escolhas para separador.
        
    def __caseXLSX(file):
        return pd.read_excel(file)
        
    def __caseJSON(file):
        return pd.read_json(file)        
        
        
if __name__ == "__main__":
    data = DataDeal(r'123.xlsx')
    fileInstance = data.getFile()
    
    data.readFile()
    print(fileInstance.getDataFrame())
    print(fileInstance.getData())
    print(fileInstance.getMetaData())
    
    