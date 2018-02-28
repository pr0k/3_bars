# Ближайшие бары

Скрипт находит и распечатывает в формате json:
 - наименьший по количеству сидячих мест бар
 - наибольший по количеству сидячих мест бар
 - ближайший к указанным координатам бар

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash

$ python bars.py <path to data_of_bars.json> <longitude> <latitude>
# possibly requires call of python3 executive instead of just python

 **********The biggest bar***********

 {
    "properties": {
        "DatasetId": 1796,
        "ReleaseNumber": 2,
        "Attributes": {
            "Name": "Спорт бар «Красная машина»",
            "IsNetObject": "нет",
            "Address": "Автозаводская улица, дом 23, строение 1",
            "SeatsCount": 450,
            "OperatingCompany": null,
            "global_id": 169375059,
            "PublicPhone": [
                {
                    "PublicPhone": "(905) 795-15-84"
                }
            ],
            "AdmArea": "Южный административный округ",
            "District": "Даниловский район",
            "SocialPrivileges": "нет"
        },
        "VersionNumber": 2,
        "RowId": "fbe6c340-4707-4d74-b7ca-2b84a23bf3a8"
    },
    "type": "Feature",
    "geometry": {
        "coordinates": [
            37.638228501070095,
            55.70111462948684
        ],
        "type": "Point"
    }
}

 **********The smallest bar**********

 {
    "properties": {
        "DatasetId": 1796,
        "ReleaseNumber": 2,
        "Attributes": {
            "Name": "БАР. СОКИ",
            "IsNetObject": "нет",
            "Address": "Дубравная улица, дом 34/29",
            "SeatsCount": 0,
            "OperatingCompany": null,
            "global_id": 20675518,
            "PublicPhone": [
                {
                    "PublicPhone": "(495) 258-94-19"
                }
            ],
            "AdmArea": "Северо-Западный административный округ",
            "District": "район Митино",
            "SocialPrivileges": "нет"
        },
        "VersionNumber": 2,
        "RowId": "17adc22c-5c41-4e4b-872f-815b521f2b53"
    },
    "type": "Feature",
    "geometry": {
        "coordinates": [
            37.35805920566864,
            55.84614475898795
        ],
        "type": "Point"
    }
}

 **********The closest bar***********

 {
    "properties": {
        "DatasetId": 1796,
        "ReleaseNumber": 2,
        "Attributes": {
            "Name": "Терем",
            "IsNetObject": "нет",
            "Address": "Керамический проезд, дом 8А",
            "SeatsCount": 30,
            "OperatingCompany": null,
            "global_id": 20735486,
            "PublicPhone": [
                {
                    "PublicPhone": "(499) 481-14-62"
                }
            ],
            "AdmArea": "Северный административный округ",
            "District": "район Восточное Дегунино",
            "SocialPrivileges": "нет"
        },
        "VersionNumber": 2,
        "RowId": "2da068bf-ebb4-442d-a4d5-2884f7f81218"
    },
    "type": "Feature",
    "geometry": {
        "coordinates": [
            37.567301976489944,
            55.88344720035491
        ],
        "type": "Point"
    }
}
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
