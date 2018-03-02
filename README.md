# Ближайшие бары
Находит и выводит в консоль:
 - наименьший по количеству сидячих мест бар
 - наибольший по количеству сидячих мест бар
 - ближайший к указанным координатам бар

# Как запустить


1. Зарегистрироваться на сайте [data.mos.ru](https://data.mos.ru/)
2. получить ключ API и скачать [список московских баров](https://data.mos.ru/opendata/7710881420-bary) в формате **.json** по ссылке вида https://apidata.mos.ru/v1/features/1796?api_key={place_your_API_key_here}

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash

$ python bars.py [-h] [-v] bars_json longitude latitude
# possibly requires call of python3 executive instead of just python

 *******The biggest bar:*******

Name:          Спорт бар «Красная машина»
Address:       Автозаводская улица, дом 23, строение 1
Seats Count:   450
Coordinates:   [37.638228501070095, 55.70111462948684]

******The smallest bar:*******

Name:          БАР. СОКИ
Address:       Дубравная улица, дом 34/29
Seats Count:   0
Coordinates:   [37.35805920566864, 55.84614475898795]

*******The closest bar********

Name:          Staropramen
Address:       Садовая-Спасская улица, дом 19, корпус 1
Seats Count:   50
Coordinates:   [36.900000000253, 55.303299999814]


```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
