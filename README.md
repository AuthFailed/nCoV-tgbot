[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/AuthFailed/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Corona Virus Stats bot</h3>

  <p align="center">
    Удобное отслеживание статистики по инфицированным, вылечившимся и умерших от 2019-nCoV!
    <br />
    <a href="https://github.com/AuthFailed/Best-README-Template"><strong>Документация »</strong></a>
    <br />
    <br />
    <a href="https://github.com/AuthFailed/Best-README-Template">Демо</a>
    ·
    <a href="https://github.com/AuthFailed/Best-README-Template/issues">Зарепортить</a>
    ·
    <a href="https://github.com/AuthFailed/Best-README-Template/issues">Запросить функцию</a>
  </p>
</p>



<!-- КОНТЕНТ -->
## Контент

* [О проекте](#о-проекте)
  * [Собрано с использованием](#собрано-с-использованием)
* [Для начала](#для-начала)
  * [Зависимости](#зависимости)
  * [Установка](#установка)
* [Использование](#использование)
* [Лицензия](#лицензия)
* [Контакты](#контакты)
* [Благодарности](#благодарности)



<!-- О ПРОЕКТЕ -->
## О проекте

[![Product Name Screen Shot][product-screenshot]](https://t.me/NovelCoV_bot)

Создано уже много много сервисов для отслеживания текущего состояния, но не всегда удобно открывать браузер и смотреть графики. Телеграм бот частично решает эту проблему.

Преимущества:
* В мессенджере вы можете не отвлекаясь от бесед посмотреть статистику по вирусу
* Всегда актуальная информация
* Инлайн режим для удобного шаринга информации
* Конечно, ни один шаблон не сможет подходить под все ваши проекты, так как ваши потребности могут меняться. Так что в ближайшем будущем появяться новые шаблоны. Вы так же можете форкнуть этот репозиторий и присылать пул реквесты.

Список часто используемых ресурсов, которые я нахожу полезными, приведен в благодарностях.

### Собрано с использованием
* [Python](https://www.python.org/)


### Зависимости


* Python 3.7+
```sh
apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
curl -O https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tar.xz
tar -xf Python-3.7.3.tar.xz
cd Python-3.7.3
./configure --enable-optimizations
make -j 8
make altinstall
```

### Установка

1. Создайте бота в [BotFather](https://t.me/BotFather) и получите токен
2. Клонируйте репозиторий
```sh
git clone https://github.com/AuthFailed/nCoV-tgbot.git
```
3. Установите модули
```sh
python3.7 -m pip install -r  requirements.txt
```
4. Вставьте ваш API ключ в `config.py`
```PY
token = 'your token'
```



<!-- ИСПОЛЬЗОВАНИЕ -->
## Использование

В боте присутствуют следующие функции:
* Статистика на текущий момент (Зараженные, на подозрении, на карантине, вылечившиеся, смерти, смертность)
* Прогноз заболеваемости по Китаю
* Города на карантине
* Заражения по странам

_Для большего кол-ва информации перейдите в [бота](htpps://t.me/NovelCov_bot)_



<!-- ЛИЦЕНЗИЯ -->
## Лицензия

Распространяется по лицензии MIT. Просмотрите `LICENSE` для большей информации.



<!-- КОНТАКТ -->
## Контакты

Ссылка на проект: [https://github.com/AuthFailed/nCoV-tgbot](https://github.com/AuthFailed/nCoV-tgbot)



<!-- БЛАГОДАРНОСТИ -->
## Благодарности
* [Wuhanpneumonia](https://wuhanpneumonia.ru/)
* [Thewuhanvirus](https://thewuhanvirus.com/)
* [Coronavirus-monitor](https://coronavirus-monitor.ru/)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=flat-square
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[product-screenshot]: images/screenshot.png
[license-url]: license.txt
