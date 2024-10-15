from preRequisite.preRequisites import PreRequisitesGODS
from service.data.To import To
from service.data.handler import DataHandler 
from service.generate.generator import Builder

if __name__=="__main__":
    # PreRequisitesGODS.VerifyRequirements()
    
    handler = DataHandler(r'e.g/bd.xlsx')
    # handler = DataHandler(r'e.g/bd.csv')
    # handler = DataHandler(r'e.g/bd.json')
    
    handler.getArchive().setDelimiter('==')
    handler.setDtype({"CPF":str, "DATA":str})
    handler.readFile()
    
    print(handler.getArchive().getData())
    
    
    To.languageTo('pt_BR')
    handler.getArchive().changeType(keyColumn="DATE", funcProvided=lambda x: To.Date().to_personalizedFormat(x, '%d de %B de %Y'))
    # handler.getArchive().changeType(keyColumn="DATE", funcProvided=To.Date().to_dd_MM_yyyy_in_full)
    
    handler.getArchive().changeType("HOUR", To.Hour().to_hh_mm)
    handler.getArchive().setAdditionalParameters("NAME", "bold", True)
    handler.getArchive().setAdditionalParameters("DATE", "bold", True)
    
    
    build = Builder(handler.getArchive(), r'e.g/doc.docx')
    build.generate()
    build.saveAs(textAtFile='DOCS/{} - Example How-To',
                 keyColumn=['NAME'], ZipFile=True, 
                 saveLocally=True)
    
    
    print(handler.getArchive().getData())
    print('\n')
    for each, values in handler.getArchive().getData().items():
        print(each, values)
    
    print(build.getTimeToGenerate())
    
    # tratar quando for csv agora
    
    