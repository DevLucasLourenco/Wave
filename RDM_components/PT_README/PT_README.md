# WAVE
> # Workflow Automation and Versatile Engine


<div align=“center”>
<img src="RDM_components/img/wave.jpeg" alt=“WAVE” width=“450px”/>
</div>

> Propriedade de Lucas Lourenço

> Manutenido por Lucas Lourenço
----

# Iniciando no WAVE
Para usar WAVE, execute o comando abaixo no seu terminal.

##### ```pip install -U wave-flow```



# Exemplos

<details open>
<summary>
Practical Examples
</summary>

<p>

 - [Exemplo Simple](e.g/simple/simpleExample.py)
 
 - [Exemplo Complexo](e.g/complex/complexExample.py)

</p>
</details>


<details open>
<summary>
Exemplo de Uso das Classes
</summary>

<p>

 - [DataHandler](#-datahandler)

 - [Builder](#-builder)
 
 - [To](#-to)
 
 - [Transmitter](#-transmitter)


</p>
</details>


---

# Como Usar


## | **DataHandler**
A classe `DataHandler` é a primeira etapa quando você está usando o WAVE. Com ela, você poderá usar vários recursos, inclusive a maneira exclusiva de acessar a classe `Archive` (conforme mostrado no próximo tópico). Abaixo estão os métodos e sua explicação.


* #### **DType**
>Como [Pandas](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dtypes.html), você pode passar um _DType_ como parâmetro. O _KEYS_ nesse dict deve ser um dos cabeçalhos da coluna que você deseja ler como o dado _VALUE_.

Por exemplo:
```python
handler = DataHandler(r'example.xlsx')
handler.getArchive().setDelimiter('==') # parte importante do código que será mostrado abaixo.
handler.setDtype({“ID”:str, “DATE”:str})
```


* #### **Acessar Archive**
>Para acessar a classe [Archive](#-archive), a única maneira de acessá-la é usando o código abaixo.

Por exemplo:
```python
handler = DataHandler(r'example.xlsx')
handler.getArchive() # e seus métodos, conforme mostrado
```


* #### **Leitura de Arquivo**
>Depois de informar o [Delimiter](#-delimiter) e, se achar necessário, informar o [Dtype](#dtype), você deve ler o arquivo.

Por exemplo:
```python
from WaveFlow import (PreRequisitesWave, To, DataHandler, Builder, Transmitter)

handler = DataHandler(r'example.xlsx')
handler.getArchive().setDelimiter('==')
handler.setDtype({“ID”:str, “DATE”:str})
handler.readFile()

print(handler.getArchive().getData()) # -> dict
```

## | **Archive**
Depois de ser acessado pelo método em [DataHandler (Acessar Archive)](#acessar-archive), você pode gerenciar várias informações de dados. Quais delas serão expressas a seguir.

* ### **Delimitador**
Uma das partes mais importantes da orquestra. É necessário e primordial para identificar onde estão os espaços reservados.

Por exemplo:
```python
from WaveFlow import (PreRequisitesWave, To, DataHandler, Builder, Transmitter)

handler = DataHandler(r'example.xlsx')
handler.getArchive().setDelimiter('==')

[...]

```


* ### **Transformar dados**
Esse método coopera com a classe [To](#-to). Para lidar com os dados, a classe `To` tem uma série de gerenciamentos sobre ela. Você pode ler mais sobre isso [clicando aqui](#-to).

Seguindo a harmonia da estrutura, é apropriado que você use esse método para processar qualquer tipo de dados.



Por exemplo:
```python
handler.getArchive().transformData(“HOUR”, To.Hour().to_hh_mm)
handler.getArchive().transformData(“DATE”, To.Date().to_dd_mm_yyyy)
handler.getArchive().transformData(“FINALDATE”, lambda x: To.Date().to_personalizedFormat(x, '%d de %B de %Y'))
```



* ### **Parâmetro adicional**
Usando esse método, você pode personalizar as configurações de formatação para cada informação que será colocada.
Assumindo os parâmetros obrigatórios `keyColumn`, `parameterToChange`, `newValueToParameter`, preste atenção aos dados necessários abaixo.

| **possibilidades** | **tipo de dados apropriado** | 
|-----------------------------|------------------------------|
| bold | bool |
| italic | bool |
| font | string |
| size | int |


`keyColumn`: Coloque aqui o cabeçalho que você deseja operar.

`parameterToChange`: Selecione uma das quatro possibilidades.

`newValueToParameter`: coloque os dados apropriados para o que você deseja formatar.

Por exemplo:
```python
from WaveFlow import (PreRequisitesWave, To, DataHandler, Builder, Transmitter)

    handler = DataHandler(r'example.xlsx')
    
    handler.getArchive().setDelimiter('==')
    handler.readFile()
    

    handler.getArchive().setAdditionalParameters(“NAME”, “size”, 12)
    handler.getArchive().setAdditionalParameters(“NAME”, “bold”, True)
    handler.getArchive().setAdditionalParameters(“COUNTRY”, 'italic', True)
    handler.getArchive().setAdditionalParameters(“DATE”, “font”, 'Times New Roman')
    
    [...]

```

<!-- 
   def setAdditionalParameters(self, keyColumn:str, parameterToChange:Literal[“font”, “size”, “italic”, “bold”], newValueToParameter):
        self.__DictWithData[keyColumn]['additional_parameters'][parameterToChange] = newValueToParameter -->


* ### **Getters**


| **Nome do método** | **Tipo de retorno** | **Descrição** |
|------------------------------|-------------------------|---------------------------------------------------------------------------------|
| `getData()` | `dict` | Retorna o dicionário de dados, gera `ReferenceError` se não houver dados disponíveis. **(talvez seja isso que você esteja procurando)**|
| `getFileType()` | `str` | Retorna o tipo de arquivo do archive.                                          |
| `getMetaData()` | `list[str]` | Retorna uma lista de metadados associados ao arquivo.                           |
| `getFilename()` | `str` | Retorna o nome do arquivo.                                                |
| `getDesignatedFile()` | `docx.Document` | Retorna o objeto do arquivo designado.                                            |
| `getDataFrame()` | `pd.DataFrame` | Retorna os dados como um DataFrame, gera `ReferenceError` se não houver DataFrame.
| `getDelimiter()` | `str` | Retorna o delimitador atual usado para a formatação de chaves.                         |
| `getFilesGenerated()` | `list[docx.Document]` | | Retorna uma lista de arquivos gerados pelo sistema.                               |

---
## | **Builder**
A classe `Builder` requer apenas dois parâmetros obrigatórios. São eles a _instância_ do Archive, o que significa que você **tem** que informar “handler.getArchive()” como primeiro parâmetro (parâmetro archive). Como segundo, você deve informar o documento base (parâmetro baseDocx) com o qual deseja lidar.

Por exemplo:
```python
from WaveFlow import (PreRequisitesWave, To, DataHandler, Builder, Transmitter)


handler = DataHandler(r'example.xlsx')
handler.getArchive().setDelimiter('==')
handler.readFile()

build = Builder(handler.getArchive(), r'example.docx')

[...]
```


* ### **Geração**
`.generate()`

Método usado para gerar os documentos. Não há parâmetros, basta executá-lo.

Por exemplo:
```python
from WaveFlow import (PreRequisitesWave, To, DataHandler, Builder, Transmitter)


handler = DataHandler(r'example.xlsx')
handler.getArchive().setDelimiter('==')
handler.readFile()

build = Builder(handler.getArchive(), r'example.docx')
build.generate()

[...]

```


* ### **Salvando arquivos gerados**
`.saveAs()`

Para salvar em um arquivo zip ou localmente, primeiro é necessário gerar como mostrado acima.

Esse método tem várias formas de personalização. Abaixo você encontrará informações.


| Parâmetro | Tipo necessário |
|---------------|-------------------------|
| `textAtFile` | str |
| `keyColumn` | list[str] |
| `ZipFile` | bool -> False como padrão|
| `saveLocally` | bool -> True como padrão |



### Explicação

- **textAtFile**

>Esse é o nome do padrão do arquivo que será gerado. <p>
Como, por exemplo: “ {} - Documento Gerado - {}”. <p>
O “{}” na string está presente porque você pode personalizar a saída com o próximo parâmetro - keyColumn


- keyColumn**

> Com os cabeçalhos (chaves) que você informa nessa lista como string, você pode fornecer o atual

- ZipFile & saveLocally**

> Ele criará um conteúdo ZipFile (no caso de ZipFile receber True) e criará arquivos localmente (no caso de saveLocally receber True)


Por exemplo:
```python
from WaveFlow import (PreRequisitesWave, To, DataHandler, Builder, Transmitter)


handler = DataHandler(r'example.xlsx')
handler.getArchive().setDelimiter('==')
handler.readFile()

build = Builder(handler.getArchive(), r'example.docx')
build.generate()

build.saveAs(textAtFile=“DOCS/{}/{} - Document”,
                    keyColumn=['Date', 'Name'], 
                    ZipFile=True, 
                    saveLocally=True)
```


* ### **Getters**
| Método | Saída |
|-------------------------|---------------------------------------------|
| `getTimeToGenerate` | _o tempo necessária para gerar_ |
| `getIndexSequence` | _a sequência real de todos os documentos_ |

---


## | **To**

A classe `To` fornece vários utilitários para transformar datas, horas e valores monetários em diferentes formatos. Veja a seguir os métodos disponíveis e seus exemplos de uso.

---


> ### **1. Configuração de idioma**
***Antes*** de usar os utilitários `Date`, `Hour` ou `Money`, você pode definir o idioma usando o método `To.languageTo()`.

#### **Idiomas suportados**
- `'pt_BR'` - Português (Brasil)
- `'es_ES'` - Espanhol
- `'en_US'` - Inglês
- `'fr_FR'` - Francês
- Você pode usar outro idioma com o qual o `locale` possa lidar.

#### **Exemplo**
```python
from WaveFlow import (PreRequisitesWave, To, DataHandler, Builder, Transmitter)

[...]

To.languageTo('pt_BR') # Define o idioma como português
handler.getArchive().transformData(“HOUR”, To.Hour().to_hh_mm)

[...]
```
---

> ### **2. Manipulação de data**
O `To.Date()` fornece vários métodos para manipular e transformar objetos de data.

#### **Available Methods**
<!-- | Método | Formato de saída | Exemplo de entrada | Exemplo de saída | Formato de saída
|---------------------------------|---------------------|------------------------------|-------------------------------| -->
| Method                          | Output Format       | Example Input                | Example Output                |
|---------------------------------|---------------------|------------------------------|-------------------------------|
| `to_dd_mm`                      | `dd/m`             | `Timestamp('2024-01-01')`   | `01/1`                        |
| `to_dd_MM`                      | `dd/M`             | `Timestamp('2024-01-01')`   | `01/Janeiro`                  |
| `to_MM_yy`                      | `MM/y`             | `Timestamp('2024-01-01')`   | `Janeiro/24`                  |
| `to_MM_yyyy`                    | `MM/Y`             | `Timestamp('2024-01-01')`   | `Janeiro/2024`                |
| `to_dd_mm_yy`                   | `dd/mm/yy`         | `Timestamp('2024-01-01')`   | `01/01/24`                    |
| `to_dd_mm_yy_periodSep`         | `dd.mm.yy`         | `Timestamp('2024-01-01')`   | `01.01.24`                    |
| `to_dd_MM_yyyy`                 | `dd/MM/yyyy`       | `Timestamp('2024-01-01')`   | `01/Janeiro/2024`             |
| `to_dd_mm_yyyy`                 | `dd/mm/yyyy`       | `Timestamp('2024-01-01')`   | `01/01/2024`                  |
| `to_mm_dd_yyyy`                 | `mm/dd/yyyy`       | `Timestamp('2024-01-01')`   | `01/01/2024`                  |
| `to_yyyy_mm_dd`                 | `yyyy-mm-dd`       | `Timestamp('2024-01-01')`   | `2024-01-01`                  |
| `to_full_date`                  | Data Completa (string)   | `Timestamp('2024-01-01')`   | `Segunda-feira, 01 Janeiro 2024`     |
| `to_dd_MM_yyyy_in_full`         | Data Completa (string)   | `Timestamp('2024-01-01')`   | `01 Janeiro 2024`             |
| `to_personalizedFormat`         | Formatação Customizada      | `Timestamp('2024-01-01')`   | Baseado no formato informado      |


> O tipo de entrada deve ser da classe ***Timestamp***
#### **Exemplo**
* **método padrão de uso**:
```python
[...]

handler.getArchive().transformData(“DATE”, To.Date().to_dd_mm_yy_periodSep)

[...]
```
* **to_personalizedFormat**:

    É um método exclusivo da classe < To > que fornece uma personalização sobre os dados tratados. Você pode usar o mesmo `.strftime()` que [usado no pandas](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.strftime.html).
```python
[...]

handler.getArchive().transformData(“DATE”,lambda x:To.Date().to_personalizedFormat(x,'%d de %B de %Y'))

[...]
```
---
> ### **3. Manipulação de tempo**
O `To.Hour()` fornece métodos para transformar objetos de tempo em formatos desejados.

#### **Métodos disponíveis**
| Método | Formato de saída | Exemplo de entrada | Exemplo de saída
|----------------------|---------------------|------------------------|--------------------|
| `to_hh_mm_ss` | `HH:MM:SS` | `datetime(11, 30)` | `11:30:00` |
| `to_hh_mm` | `HH:MM` | `datetime(11, 30)` | `11:30` |
| `to_12_hour_format` | `HH:MM AM/PM` | `datetime(23, 30)` | `11:30 PM` |
| `to_24_hour_format` | `HH:MM` | `datetime(23, 30)` | `23:30` |

> O tipo de entrada deve ser ***datetime class***

#### **Exemplo**
* **método padrão de uso**:
```python
[...]

To.languageTo('pt_BR')
handler.getArchive().transformData(“HOUR”, To.Hour().to_hh_mm)

[...]
```
---


> ### **4. Manipulação de formatação de dinheiro**
O `To.Money()` fornece métodos para formatar valores monetários em várias moedas.

#### **Métodos disponíveis**
| Método | Formato de saída | Exemplo de entrada | Exemplo de saída
|------------------|--------------------------|----------------|------------------------|
| `to_dollars` | `$ {valor}` | `1234.56` | `$ 1,234.56` |
| `to_euros` | `€ {valor}` | `1234.56` | `€ 1.234,56` |
| `to_pounds` | `£ {valor}` | `1234.56` | `£ 1.234.56` |
| `to_brl` | `R$ {valor}` | `1234.56` | `R$ 1.234,56` |

> O tipo de entrada deve ser ***float*** ou ***int***

#### **Exemplo**
* **método padrão de uso**:
```python
[...]

To.languageTo('pt_BR')
handler.getArchive().transformData(“VALUE”, To.Money().to_brl)

[...]
```

---

## | **Transmissor**
Essa classe pode ser o primeiro passo para seu uso no WAVE, pois ela pode analisar um arquivo .docx e retornar um arquivo .xlsx com todos os cabeçalhos definidos no docx.

Tudo o que você precisa fazer é informar o documento (ele **deve** ser uma lista) e passar o delimitador. Depois disso, basta usar o método `export`.
Siga o exemplo:

```python
from WaveFlow import Transmitter

transmitter = Transmitter(['example.xlsx'], '==')
transmitter.export(“exampleExport.xlsx”)

```