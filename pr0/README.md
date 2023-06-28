# Практика 0
```
@startuml "Жилищное агентство ИС"
left to right direction
actor "Владелец жилья" as vj
actor "Квартиросъемщик" as ks
rectangle "Жилищное агентство" {
    usecase "Зарегистрироваться в системе"as reg
    usecase "Зарегистрировать жильё в системе" as regj
    usecase "Выставить информацию о жилье" as inf
    usecase "Найти жильё" as nait
    usecase "Убрать жильё из системы" as ubr
    usecase "Внести необходимые документы" as doc
    usecase "Внести документы о жилье" as docj
    usecase "Обсудить детали съема" as det
    usecase "Отказаться от сделки" as otkaz
    usecase "Принять сделку" as prin
}
vj --> reg
doc .> reg : include
ks --> reg
vj --> regj
docj .> regj : include
vj --> inf
ks --> nait
vj ---> det
ks --> det
det .> prin : extend
det .> otkaz : extend
ubr .> prin : include

@enduml
```

![](https://github.com/noil6000/TMP/blob/main/pr0/Жилищное%20агентство%20ИС.png)
