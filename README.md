### :octocat: mse_robot_checks_reports
# Проверка формата присылаемых архивов

## :warning: Требования

**Python 3+**

[:link: Get here!](https://www.python.org/downloads/release/python-363/)

**Mongo DB**

[:link: Get here!](https://www.mongodb.com/)

## :warning: Установка

```
git clone git@github.com:moevm/mse_robot_checks_reports.git
```

## :warning: Установка зависимостей

```
./setup_dependencies.sh
```

## :warning: Настройка

**Конфиг расположен в:**
```
reportChecker/resources/config.json
```

**Параметры пользователя**

*email, password* ящика:

```
"authentication": {
    "email": "myemail@mail.com",
    "password": "mydogsname"
  }
```

**Информация о предметах**

Массив *groups* с элементами структуры:

```
{
      "group_number": 5303,
      "disciplines": [
        {
          "name": "ПРОГ",
          "course_works": 1,
          "labs": 2,
          "ind_tasks": 7
        },
        {
          "name": "БД",
          "course_works": 1,
          "labs": 2,
          "ind_tasks": 5
        }
      ]
    }
```

- *group_number* - номер группы

- *name* - название дисциплины [отсюда](http://se.moevm.info/doku.php/start:report_submission) 

- *course_works* - количество курсовых работ

- *labs* - количество лабораторных работ

- *ind_tasks* - количество индивидуальных заданий



## Запуск

```
./runReportChecker
```

## Настройка демона для регулярного запуска

Добавьте скрипт в `/etc/cron.hourly` для запуска каждый час:

```
#!/bin/bash

sh ./path/to/runReportChecker
```







[:+1::ok_hand::clap::ok_hand::+1:](https://www.youtube.com/watch?v=vjUqUVrXclE)
