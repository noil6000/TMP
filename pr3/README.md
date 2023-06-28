# Стратегия

Стратегия – поведенческий шаблон, призванный для обеспечения взаимозаменяемости разных алгоритмов или вариаций алгоритма с одинаковыми интерфейсами. Стратегии – и есть эти варианты. В зависимости от условий (контекст) код выбирает подходящий алгоритм. 

Мы создаем общий интерфейс стратегий BaseStrategy – как абстрактный класс ABC. Далее в каждой стратегии реализуем этот интерфейс.

Создаем интерфейс:

```
class BaseStrategy(ABC):
    @abstractmethod
    def do_work(self, x, y):
        pass
```

Создаем классы:

```
class Adder(BaseStrategy):
    def do_work(self, x, y):
        return x + y
```

```
class Multiplicator(BaseStrategy):
    def do_work(self, x, y):
        return x * y
```

```
class Calculator:
    def set_strategy(self, strategy: BaseStrategy):
        self.strategy = strategy
    def calculate(self, x, y):
        print('Result is', self.strategy.do_work(x, y))
```

## Диаграмма

```
@startuml
class Strategy.Calculator {
~ Activity activity
+ void setActivity(Activity)
+ void executeActivity()
}
class Strategy.Adder {
+ void AddSmth()
}
interface Strategy.BaseStrategy {
+ void AddSmth()
+ void MultiplicateSmth()
}
class Strategy.Multiplicator {
+ void MultiplicateSmth()
}

Strategy.BaseStrategy <|.. Strategy.Adder
Strategy.BaseStrategy <|.. Strategy.Multiplicator

@enduml

```
![](https://github.com/Smipos/TMP/blob/main/practices/practice_3/strategy/strategy.jpg)

# Шаблонный метод
```
def get_text():
     
    return "plain_text"
 
def get_xml():
     
    return "xml"
 
def get_pdf():
     
    return "pdf"
 
def get_csv():
     
    return "csv"
 
def convert_to_text(data):
     
    print("[CONVERT]")
    return "{} as text".format(data)
 
def saver():
     
    print("[SAVE]")

def template_function(getter, converter = False, to_save = False):

    data = getter()
    print("Got `{}`".format(data))
 
    if len(data) <= 3 and converter:
        data = converter(data)
    else:
        print("Skip conversion")

    if to_save:
        saver()
 
    print("`{}` was processed".format(data))
 
if __name__ == "__main__":
 
    template_function(get_text, to_save = True)
 
    template_function(get_pdf, converter = convert_to_text)
 
    template_function(get_csv, to_save = True)
 
    template_function(get_xml, to_save = True)
```

Результат работы программы:

```
Got `plain_text`
Skip conversion
[SAVE]
`plain_text` was processed 
Got `pdf`
[CONVERT]
`pdf as text` was processed
Got `csv`
Skip conversion
[SAVE]
`csv` was processed
Got `xml`
Skip conversion
[SAVE]
`xml` was processed
```
## Диаграмма

```
@startuml
abstract class Template_Method.Template {
+ void converter()
+ void to_save()
+ {abstract}void getter() 
}
class Template_Method.XML {
+ {static} void returnXML()
}
class Template_Method.PDF {
+ void returnPDF()
}
class Template_Method.CSV {
+ void returnCSV()
}

Template_Method.Template <|-- Template_Method.XML
Template_Method.Template <|-- Template_Method.PDF
Template_Method.Template <|-- Template_Method.CSV
@enduml
```
![](https://github.com/Smipos/TMP/blob/main/practices/practice_3/template_method/template_method.png)
