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

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Russian README

# Flask Infinity - Автоматический перезапуск веб-приложений на PythonAnywhere

## Описание

Flask Infinity — это веб-приложение на Flask, которое включает функцию автоматического перезапуска веб-приложений на PythonAnywhere. Приложение автоматически перезапустит ваше веб-приложение в запланированные моменты, используя API PythonAnywhere. Так же мы можете вставить его уже в существующий код, чтобы не открывать 100500 консолей.

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

## Лицензия

Этот проект лицензируется на условиях MIT License — подробности см. в файле [LICENSE](LICENSE).
