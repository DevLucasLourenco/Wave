from service.data.dataTreat import DataDeal
from service.generate.generateFiles import Generate

if __name__=="__main__":
    data = DataDeal(r'123.xlsx')
    data.readFile()
    data.getFile().setDelimiters('==')
    
    print(data.getFile().getData())
    gen = Generate(data.getFile())
    gen.generate()
    
    print(gen.getTimeToGenerate())
    
    for k in data.getFile().getData():
        print(k)
        print(data.getFile().getData()[k]['key_w/Delimiter'])
        
