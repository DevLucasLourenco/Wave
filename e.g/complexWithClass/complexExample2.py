from WaveFlow import PreRequisitesWave, To, DataHandler, Builder, Transmitter


class Request:
    def __init__(self, filePath:str, filename:str, formatKey:list[str], zipFile, saveLocally):
        self.filePath:str = filePath
        self.filename:str = filename
        self.formatKeys:list[str] = formatKey
        self.zipFile:bool = zipFile
        self.saveLocally:bool = saveLocally



request1 = Request(filePath=r'e.g\complex\doc.docx', 
                   filename='D1/{} - Example 1', 
                   formatKey=['NAME'], 
                   zipFile=	True, 
                   saveLocally=True)

request2 = Request(filePath=r'e.g\complex\doc2.docx',
                   filename='D2/{} - {} - Example 2',
                   formatKey=['COUNTRY', 'NAME'],
                   zipFile=	True, 
                   saveLocally=True)

requestListage = [request1, request2]


handler = DataHandler(r'e.g\complex\bd.xlsx')
handler.getArchive().setDelimiter('==')
handler.readFile()


To.languageTo('pt_BR')
for request in requestListage:
    handler.getArchive().transformData("HOUR", To.Hour().to_hh_mm)
    handler.getArchive().transformData("DATE", lambda x: To.Date().to_personalizedFormat(x, '%d de %B de %Y'))
    
    build = Builder(handler.getArchive(), request.filePath)
    build.generate()
    
    build.saveAs(textAtFile=request.filename, 
            keyColumn=request.formatKeys, 
            ZipFile=request.zipFile, 
            saveLocally=request.saveLocally)

