# Практика 0
```
@startuml "Практическая работа 0"
left to right direction
title Информационная система жилищного агенства
skinparam backgroundcolor PowderBlue
actor Квартиросъемщик AS kvr
actor Владелец AS vld
rectangle Система {
    vld ---> (Предоставить информацию о жилье)
    kvr ---> (Поиск жилья)
    (Поиск жилья) <... (Зарегистрироваться в системе):<<include>>
    (Поиск жилья) ...> (Снять жилье):<<include>>
    (Предоставить информацию о жилье) <... (Зарегистрироваться в системе):<<include>>
    (Предоставить информацию о жилье) ...> (Сдать жилье):<<include>>
}
@enduml
```

![](https://github.com/Smipos/TMP/blob/main/practices/practice_0/Практическая%20работа%201.png)
