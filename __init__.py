from preRequisite.preRequisites import PreRequisitesGODS
from service.data.To import To
from service.data.handler import DataHandler 
from service.generate.generator import Builder

if __name__=="__main__":
    PreRequisitesGODS.VerifyRequirements()
    
    handler = DataHandler(r'123.xlsx')
    
    handler.getArchive().setDelimiter('==')
    handler.setDtype({"CPF":str})
    handler.readFile()
    
    
    To.changeLanguage('pt_BR')
    handler.getArchive().changeType(keyColumn="DATA", funcProvided=lambda x: To.Date().to_personalizedFormat(x, '%d de %B de %Y'))
    # handler.getArchive().changeType("DATA", To.Date().to_dd_MM_yyyy_in_full)
    handler.getArchive().changeType("HORA", To.Hour().to_hh_mm)
    handler.getArchive().setAdditionalParameters("NOME", "bold", True)
    # handler.getArchive().setAdditionalParameters("NOME", "italic", True)
    handler.getArchive().setAdditionalParameters("DATA", "bold", True)
    # handler.getArchive().setAdditionalParameters("DATA", "size", 10)
     
    
    gen = Builder(handler.getArchive(), r'base teste.docx')
    gen.generate()

    
    # print(handler.getArchive().getData())    
    # print('\n')
    # for each, values in handler.getArchive().getData().items():
    #     print(each, values)
    
    # print(gen.getTimeToGenerate())
    
    
    # funções para salvar personalizadas
    # zippar arquivos
    