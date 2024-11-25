# WAVE
> # Workflow Automation and Versatile Engine


<div align="center">
<img src="RDM_components/img/wave.jpeg" alt="WAVE" width="450px"/>
</div>

> Owned by Lucas Lourenço

> Maintained by Lucas Lourenço
----

# Getting Started on WAVE
To use WAVE, execute the following command in your terminal

##### ```pip install -U wave-flow```



# Examples

<details open>
<summary>
Practical Examples
</summary>

<p>

 - [Simple e.g.](e.g/simple/simpleExample.py)
 
 - [Complex e.g.](e.g/complex/complexExample.py)

</p>
</details>


<details open>
<summary>
Class Use Case Example
</summary>

<p>

 - [DataHandler](#-datahandler)

 - [Builder]()
 
 - [To](#-to)
 
 - [Transmitter](#-transmitter)


</p>
</details>

---

# How To Use

## | **DataHandler**
```python
from WaveFlow import (PreRequisitesWave, To, DataHandler, Builder, Transmitter)

handler = DataHandler(r'bd.xlsx')
handler.getArchive().setDelimiter('==')
handler.readFile()

print(handler.getArchive().getData()) # -> dict
```

## | **Builder**



---
## | **To**

The `To` class provides multiple utilities for transforming dates, times, and monetary values into different formats. Below are the available methods and their usage examples.

---

### **1. Language Configuration**
***Before*** using the `Date`, `Hour`, or `Money` utilities, you can set the language using the `To.languageTo()` method.

#### **Languages Supported**
- `'pt_BR'` - Portuguese (Brazil)
- `'es_ES'` - Spanish
- `'en_US'` - English
- `'fr_FR'` - French
- You can use another language too.

#### **Example**
```python
from WaveFlow import (PreRequisitesWave, To, DataHandler, Builder, Transmitter)

[...]

To.languageTo('pt_BR')  # Set language to Portuguese
handler.getArchive().transformData("HOUR", To.Hour().to_hh_mm)

[...]
```


---

### **2. Date Manipulation**
The `To.Date()` provides various methods to handle and transform date objects.

#### **Available Methods**
| Method                          | Output Format       | Example Input                | Example Output                |
|---------------------------------|---------------------|------------------------------|-------------------------------|
| `to_dd_mm`                      | `dd/m`             | `Timestamp('2024-01-01')`   | `01/1`                        |
| `to_dd_MM`                      | `dd/M`             | `Timestamp('2024-01-01')`   | `01/January`                  |
| `to_MM_yy`                      | `MM/y`             | `Timestamp('2024-01-01')`   | `January/24`                  |
| `to_MM_yyyy`                    | `MM/Y`             | `Timestamp('2024-01-01')`   | `January/2024`                |
| `to_dd_mm_yy`                   | `dd/mm/yy`         | `Timestamp('2024-01-01')`   | `01/01/24`                    |
| `to_dd_mm_yy_periodSep`         | `dd.mm.yy`         | `Timestamp('2024-01-01')`   | `01.01.24`                    |
| `to_dd_MM_yyyy`                 | `dd/MM/yyyy`       | `Timestamp('2024-01-01')`   | `01/January/2024`             |
| `to_dd_mm_yyyy`                 | `dd/mm/yyyy`       | `Timestamp('2024-01-01')`   | `01/01/2024`                  |
| `to_mm_dd_yyyy`                 | `mm/dd/yyyy`       | `Timestamp('2024-01-01')`   | `01/01/2024`                  |
| `to_yyyy_mm_dd`                 | `yyyy-mm-dd`       | `Timestamp('2024-01-01')`   | `2024-01-01`                  |
| `to_full_date`                  | Full Date String   | `Timestamp('2024-01-01')`   | `Monday, 01 January 2024`     |
| `to_dd_MM_yyyy_in_full`         | Full Date String   | `Timestamp('2024-01-01')`   | `01 January 2024`             |
| `to_personalizedFormat`         | Custom Format      | `Timestamp('2024-01-01')`   | Based on format provided      |

> Input type must be ***Timestamp class***
#### **Example**
* **pattern method use**:
```python
[...]

handler.getArchive().transformData("DATE", To.Date().to_dd_mm_yy_periodSep)

[...]
```
* **to_personalizedFormat**:

    It's an exclusive method in < To > that provides a personalization about data been treated
```python
[...]

handler.getArchive().transformData("DATE", lambda x: To.Date().to_personalizedFormat(x, '%d de %B de %Y'))

[...]
```


---

### **3. Time Manipulation**
The `To.Hour()` provides methods for transforming time objects into desired formats.

#### **Available Methods**
| Method               | Output Format       | Example Input          | Example Output     |
|----------------------|---------------------|------------------------|--------------------|
| `to_hh_mm_ss`        | `HH:MM:SS`         | `datetime(11, 30)`     | `11:30:00`         |
| `to_hh_mm`           | `HH:MM`            | `datetime(11, 30)`     | `11:30`            |
| `to_12_hour_format`  | `HH:MM AM/PM`      | `datetime(23, 30)`     | `11:30 PM`         |
| `to_24_hour_format`  | `HH:MM`            | `datetime(23, 30)`     | `23:30`            |

> Input type must be ***datetime class***

#### **Example**
* **pattern method use**:
```python
[...]

To.languageTo('pt_BR')
handler.getArchive().transformData("HOUR", To.Hour().to_hh_mm)

[...]
```

---

### **4. Money Formatting Manipulation**
The `To.Money()` provides methods for formatting monetary values into various currencies.

#### **Available Methods**
| Method           | Output Format            | Example Input  | Example Output         |
|------------------|--------------------------|----------------|------------------------|
| `to_dollars`     | `$ {value}`             | `1234.56`      | `$ 1,234.56`          |
| `to_euros`       | `€ {value}`             | `1234.56`      | `€ 1.234,56`          |
| `to_pounds`      | `£ {value}`             | `1234.56`      | `£ 1,234.56`          |
| `to_brl`         | `R$ {value}`            | `1234.56`      | `R$ 1.234,56`         |

> Input type must be ***float*** or ***int***

#### **Example**
* **pattern method use**:
```python
[...]

To.languageTo('pt_BR')
handler.getArchive().transformData("VALUE", To.Money().to_brl)

[...]
```

---

## | **Transmitter**

