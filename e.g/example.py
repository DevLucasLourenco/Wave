
if __name__=="__main__":
    handler = DataHandler(r'bd.xlsx')
    
    handler.getArchive().setDelimiter('==')
    handler.setDtype({"CPF":str})
    handler.readFile()
    
    
    To.changeLanguage('pt_BR')
    handler.getArchive().changeType(keyColumn="DATE", funcProvided=lambda x: To.Date().to_personalizedFormat(x, '%d de %B de %Y'))
    handler.getArchive().changeType("HOUR", To.Hour().to_hh_mm)
    handler.getArchive().setAdditionalParameters("NAME", "bold", True)
    handler.getArchive().setAdditionalParameters("DATE", "bold", True)
    
    
    build = Builder(handler.getArchive(), r'doc.docx')
    build.generate()
    build.saveAs(textAtFile='DOCS/{} - Example How-To - {}', keyColumn=['DATE', 'NAME'])
    
    print(handler.getArchive().getData())
    print('\n')
    for each, values in handler.getArchive().getData().items():
        print(each, values)
    
    print(build.getTimeToGenerate())
    