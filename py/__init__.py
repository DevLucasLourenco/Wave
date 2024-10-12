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

    gen = Generate(data.getArchive(), r'base teste.docx')
    gen.generate()

    
    print(data.getArchive().getData())
    print(gen.getTimeToGenerate())
    