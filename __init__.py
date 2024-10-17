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
    
    
    To.languageTo('pt_BR')
    handler.getArchive().changeType(keyColumn="DATE", funcProvided=lambda x: To.Date().to_personalizedFormat(x, '%d de %B de %Y'))
    # handler.getArchive().changeType(keyColumn="DATE", funcProvided=To.Date().to_dd_MM_yyyy_in_full)
    
    handler.getArchive().changeType("HOUR", To.Hour().to_hh_mm)
    handler.getArchive().setAdditionalParameters("NAME", "bold", True)
    handler.getArchive().setAdditionalParameters("DATE", "bold", True)
    handler.getArchive().setAdditionalParameters("COUNTRY", 'italic', True)
    
    filesToRead = [r'e.g/doc.docx', r'e.g/doc2.docx']
    possibleFileNames = ['{} Example How-To', 'teste {}']
    for i in range(len(filesToRead)):
        build = Builder(handler.getArchive(), filesToRead[i])
        build.generate()
        
        build.saveAs(textAtFile='DOCS/'+possibleFileNames[i],
                    keyColumn=['NAME'], ZipFile=False, 
                    saveLocally=True)
        
    
    # print(handler.getArchive().getData())
    # print('\n')
    # for each, values in handler.getArchive().getData().items():
    #     print(each, values)
    
    # print(build.getTimeToGenerate())
    
    # ARRUMAR ZIP EM LOOP