
# FlaskInfinity

![Python](https://img.shields.io/badge/python-3.8+-blue.svg?style=flat)
![License: MIT](https://img.shields.io/badge/license-MIT-orange.svg?style=flat)
![Flask](https://img.shields.io/badge/Framework-Flask-blue.svg?style=flat)
![Open Source](https://img.shields.io/badge/Open%20Source-Yes-green.svg?style=flat)
![Issues](https://img.shields.io/github/issues/MHumbucker/FlaskInfinity.svg?style=flat)
![Forks](https://img.shields.io/github/forks/MHumbucker/FlaskInfinity.svg?style=flat)
![Stars](https://img.shields.io/github/stars/MHumbucker/FlaskInfinity.svg?style=flat)

## English README

# Flask Infinity - Auto Restart for PythonAnywhere Web Apps

## Description

Flask Infinity is a Flask-based web app that includes an auto-restart feature for PythonAnywhere web apps. The app will automatically restart your web app at scheduled times using the PythonAnywhere API. You can also integrate it into your existing code, so you don’t have to open a million consoles just to get things running.

### Features:
- Automatically restart your web app at specified times of the day.
- Uses PythonAnywhere's API to manage web apps.
- Flask app to serve as a base for web-based applications.

## Requirements
- Flask
- requests
- schedule

To install dependencies, use the following command:

```bash
pip install -r requirements.txt
```

## Configuration

1. Replace `PA_USERNAME` and `PA_API_KEY` with your PythonAnywhere account's username and API key in the script.
2. You can customize the schedule for the auto-restart feature by modifying the `schedule.every().day.at()` function.

## Usage

Run the script and the Flask app will start along with the scheduled restart feature:

```bash
python flask_infinity.py
```

The Flask app will be accessible on `0.0.0.0:8070`.

## Detailed Setup and Configuration Guide for FlaskInfinity

1. Clone the repository or download FlaskInfinity.py separately.

2. Create a web app on PythonAnywhere based on Flask and insert your code into flask_app.py or whatever you named it.

3. Insert FlaskInfinity into your existing code and replace the username and API token, which can be obtained at https://www.pythonanywhere.com/account/#api_token.

4. Optionally, modify/add/remove the schedule for when the script should restart.

5. Run the script, publish the web app (also check if it works by displaying "Hello from flask!") and take its URL address.

6. Go to https://uptimerobot.com/ and sign up, then insert the URL.

7. That's it! Now the app will run 24/7 and will only need to be restarted manually from time to time. Also, don't forget to reactivate the app every 3 months on the PythonAnywhere web app page and on uptime to ensure nothing shuts down.




## Russian README

# Flask Infinity - Автоматический перезапуск веб-приложений на PythonAnywhere

## Описание

Flask Infinity — это веб-приложение на Flask, которое включает функцию автоматического перезапуска веб-приложений на PythonAnywhere. Приложение автоматически перезапустит ваше веб-приложение в запланированные моменты, используя API PythonAnywhere. Так же вы можете вставить его уже в существующий код, чтобы не открывать 100500 консолей.

### Особенности:
- Автоматический перезапуск веб-приложения в заданное время.
- Использует API PythonAnywhere для управления веб-приложениями.
- Flask-приложение, которое служит базой для веб-приложений.

## Требования
- Flask
- requests
- schedule

Чтобы установить зависимости, используйте следующую команду:

```bash
pip install -r requirements.txt
```

## Настройка

1. Замените `PA_USERNAME` и `PA_API_KEY` на ваш логин и API-ключ PythonAnywhere в скрипте.
2. Вы можете настроить расписание для функции автоперезапуска, изменяя функцию `schedule.every().day.at()`.

## Использование

Запустите скрипт, и Flask-приложение начнёт работать вместе с функцией автоперезапуска:

```bash
python flask_infinity.py
```

Flask-приложение будет доступно по адресу `0.0.0.0:8070`.


## Подробная инструкция по установке и настройке FlaskInfinity

1. Скопировать репозиторий или отдельно скачать FlaskInfinity.py.
2. Создать веб-приложение на PythonAnywhere на базе Flask и вставить свой код в flask_app.py или как вы его там назвали.
3. Вставить FlaskInfinity в существующий код и поменять username и api token, который можно взять на https://www.pythonanywhere.com/account/#api_token.
4. По желанию изменить/добавить/убрать время, когда будет перезапускаться скрипт.
5. Запустить скрипт, опубликовать веб-приложение (проверить также работу, там будет "Hello from flask!") и взять его URL адрес.
6. Зайти и зарегистрироваться на https://uptimerobot.com/ и вставить туда URL.
7. Всё, теперь приложение будет работать 24/7, и его лишь изредка нужно будет перезапускать вручную. Также не забывать каждые 3 месяца на странице веб-приложения в PythonAnywhere его подактивировать и на uptime, чтобы ничего не загасло.
