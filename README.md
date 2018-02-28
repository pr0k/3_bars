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

The biggest bar:

{
    "geometry": {
        "type": "Point",
        "coordinates": [
            37.638228501070095,
            55.70111462948684
        ]
    },
    "type": "Feature",
    "properties": {
        "RowId": "fbe6c340-4707-4d74-b7ca-2b84a23bf3a8",
        "Attributes": {
            "PublicPhone": [
                {
                    "PublicPhone": "(905) 795-15-84"
                }
            ],
            "Name": "Спорт бар «Красная машина»",
            "District": "Даниловский район",
            "OperatingCompany": null,
            "global_id": 169375059,
            "IsNetObject": "нет",
            "Address": "Автозаводская улица, дом 23, строение 1",
            "SocialPrivileges": "нет",
            "AdmArea": "Южный административный округ",
            "SeatsCount": 450
        },
        "VersionNumber": 2,
        "ReleaseNumber": 2,
        "DatasetId": 1796
    }
}

The smallest bar:

{
    "geometry": {
        "type": "Point",
        "coordinates": [
            37.35805920566864,
            55.84614475898795
        ]
    },
    "type": "Feature",
    "properties": {
        "RowId": "17adc22c-5c41-4e4b-872f-815b521f2b53",
        "Attributes": {
            "PublicPhone": [
                {
                    "PublicPhone": "(495) 258-94-19"
                }
            ],
            "Name": "БАР. СОКИ",
            "District": "район Митино",
            "OperatingCompany": null,
            "global_id": 20675518,
            "IsNetObject": "нет",
            "Address": "Дубравная улица, дом 34/29",
            "SocialPrivileges": "нет",
            "AdmArea": "Северо-Западный административный округ",
            "SeatsCount": 0
        },
        "VersionNumber": 2,
        "ReleaseNumber": 2,
        "DatasetId": 1796
    }
}

The closest bar:

{
    "geometry": {
        "type": "Point",
        "coordinates": [
            37.567301976489944,
            55.88344720035491
        ]
    },
    "type": "Feature",
    "properties": {
        "RowId": "2da068bf-ebb4-442d-a4d5-2884f7f81218",
        "Attributes": {
            "PublicPhone": [
                {
                    "PublicPhone": "(499) 481-14-62"
                }
            ],
            "Name": "Терем",
            "District": "район Восточное Дегунино",
            "OperatingCompany": null,
            "global_id": 20735486,
            "IsNetObject": "нет",
            "Address": "Керамический проезд, дом 8А",
            "SocialPrivileges": "нет",
            "AdmArea": "Северный административный округ",
            "SeatsCount": 30
        },
        "VersionNumber": 2,
        "ReleaseNumber": 2,
        "DatasetId": 1796
    }
}

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
