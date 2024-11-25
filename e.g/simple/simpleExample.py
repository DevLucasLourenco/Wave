from WaveFlow import (PreRequisitesWave, To, DataHandler, Builder, Transmitter)


handler = DataHandler(r'e.g/simple/simple.xlsx')
handler.getArchive().setDelimiter('==')
handler.readFile()

build = Builder(handler.getArchive(), r'e.g./simple/simple.docx')
build.generate()

build.saveAs('{} - Document', 
             keyColumn=['NAME'])
