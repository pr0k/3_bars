# Ближайшие бары
Находит и выводит в консоль:
 - наименьший по количеству сидячих мест бар
 - наибольший по количеству сидячих мест бар
 - ближайший к указанным координатам бар

# Как запустить

1. Для запуска понадобится скачать [файл данных о московских барах](https://devman.org/media/filer_public/95/74/957441dc-78df-4c99-83b2-e93dfd13c2fa/bars.json). В нём находится информация о московских барах.

   **Или**

   Скачать наиболее актуальную информацию о барах с сайта [data.mos.ru](https://data.mos.ru/), для этого необходимо:
   - Зарегистрироваться
   - Получить ключ API и скачать [список московских баров](https://data.mos.ru/opendata/7710881420-bary) в формате **.json** по ссылке    вида https://apidata.mos.ru/v1/features/1796?api_key={place_your_API_key_here}

2. Запустить скрипт со следующими обязательными параметрами:
   - ../bars.json
   - longitude
   - latitude

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Пример запуска на Linux:

```bash

$ python bars.py [-h] [-v] bars.json 37.746736 55.692729
# possibly requires call of python3 executive instead of just python

\The biggest bar\
Name:		Спорт бар «Красная машина»
Address:	Автозаводская улица, дом 23, строение 1
Seats Count:	450
Coordinates:	[37.638228501070095, 55.70111462948684]

\The smallest bar\
Name:		БАР. СОКИ
Address:	Дубравная улица, дом 34/29
Seats Count:	0
Coordinates:	[37.35805920566864, 55.84614475898795]

\The closest bar\
Name:		БАР ПРИ «ДВОРЦЕ БРАКОСОЧЕТАНИЯ»
Address:	улица Юных Ленинцев, дом 35, корпус 1
Seats Count:	60
Coordinates:	[37.74589207026713, 55.70046093781286]

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
