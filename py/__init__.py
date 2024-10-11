from service.data.dataTreat import DataDeal
from service.generate.generateFiles import Generate

if __name__=="__main__":
    data = DataDeal(r'123.xlsx')
    data.readFile()
    data.getFile().setDelimiters('==')
    print(data.getFile().getData())
    
    data.setDtype({"CPF":str})
    data.readFile()
    print('\n')
    print(data.getFile().getData())
    print(data.getFile().getMetaData())    
    
    
    gen = Generate(data.getFile(), r'base teste.docx')
    # gen.generate()
    
    # print(gen.getTimeToGenerate())
    
    
    