from service.data.To import To
from service.data.dataTreat import DataDeal
from service.generate.generateFiles import Generate

if __name__=="__main__":
    
    data = DataDeal(r'123.xlsx')
    data.getArchive().setDelimiters('==')
    
    data.setDtype({"CPF":str})
    
    data.readFile()
    
    data.getArchive().changeType("DATA", To.Date().to_full_date)
    data.getArchive().changeType("HORA", To.Hour().to_hh_mm)
    
    data.getArchive().setAdditionalParameters("DATA", "bold", True)
    data.getArchive().setAdditionalParameters("DATA", "size", 10)
    
     
    
    gen = Generate(data.getArchive(), r'base teste.docx')
    gen.generate()

    
    for each, values in data.getArchive().getData().items():
        print(each, values)
    
    print(gen.getTimeToGenerate())
    