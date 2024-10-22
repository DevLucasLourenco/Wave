from Wave import (PreRequisitesWave, To, DataHandler, Builder, Transmitter)


if __name__=="__main__":
    # Example 

    # PreRequisitesGODS.VerifyRequirements()
    
    handler = DataHandler(r'e.g/bd.xlsx')
    # handler = DataHandler(r'e.g/bd.csv', ";")
    # handler = DataHandler(r'e.g/bd.json')
    
    handler.getArchive().setDelimiter('==')
    handler.setDtype({"CPF":str, "DATA":str})
    handler.readFile()
    print(handler.getArchive().getData())
    
    
    handler.getArchive().setAdditionalParameters("NAME", "bold", True)
    handler.getArchive().setAdditionalParameters("DATE", "bold", True)
    handler.getArchive().setAdditionalParameters("COUNTRY", 'italic', True)
    
    To.languageTo('pt_BR')
    
    
    request={0:{'filesToRead':r'e.g/doc2.docx',
                'fileRename':'FirstExampleWithValue - {}',
                'formatKeys':['NAME']
                },
             
            1:{'filesToRead':r'e.g/doc.docx',
                'fileRename':'{} - {} - SecondExampleWithAlotData {}',
                'formatKeys':['DATE','NAME', 'COUNTRY']
                },
        }
    
    for i in range(len(request)):
        handler.getArchive().transformData("HOUR", To.Hour().to_hh_mm)
        handler.getArchive().transformData("DATE", lambda x: To.Date().to_personalizedFormat(x, '%d de %B de %Y'))
        # handler.getArchive().transformData("DATE", To.Date().to_dd_mm_yyyy)
        
        build = Builder(handler.getArchive(), request[i]['filesToRead'])
        build.generate()
        
        handler.getArchive().transformData("DATE", To.Date().to_dd_mm_yy_periodSep)
        keysFormatting = request[i]['formatKeys']
        keysFormatting.insert(0, 'DATE')
        
        build.saveAs(textAtFile="DOCS/{}/"+request[i]['fileRename'],
                    keyColumn=keysFormatting, ZipFile=True, 
                    saveLocally=True)
    
    
    #----
    ## Print Out Data
    print(handler.getArchive().getData())
    print('\n')
    for each, values in handler.getArchive().getData().items():
        print(each, values)
    
    print(build.getTimeToGenerate())
    
    #----
    ### Creates a .xlsx with the analysed data from .docx
    doc_files = ["e.g/doc.docx", "e.g/doc2.docx"] 
    transmitter = Transmitter(doc_files, '==')
    transmitter.export("exampleExport.xlsx")