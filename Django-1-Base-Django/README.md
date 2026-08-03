# Django-1-Base-Django

This repository contains my solutions for the **Base Django** exercises (`ex00` to `ex03`).

## Project structure

```text
Django-1-Base-Django/
├── manage.py
├── requirements.txt
├── d05/
├── ex00/
├── ex01/
├── ex02/
└── ex03/
```

## Requirements

* Python 3.10+
* pip

## Installation

Create a virtual environment and install the dependencies:

```bash
python3 -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate

pip install -r requirements.txt
```

## Run the project

Start the development server:

```bash
python manage.py runserver
```

Open your browser and visit:

| Exercise | URL                               |
| -------- | --------------------------------- |
| ex00     | http://127.0.0.1:8000/ex00        |
| ex01     | http://127.0.0.1:8000/ex01/django |
| ex02     | http://127.0.0.1:8000/ex02        |
| ex03     | http://127.0.0.1:8000/ex03        |

## Exercises

### ex00

A static HTML page rendered with Django templates.

### ex01

Three pages using template inheritance, shared navigation, and CSS.

### ex02

A simple form built with Django Forms. Submitted messages are stored in a log file and displayed on the page.

### ex03

A table showing 50 shades of four colors generated dynamically by the view.

## Notes

* Every exercise is part of the same Django project (`d05`).
* Static files are located in `ex01/static/`.
* Templates are stored inside each application's `templates/` directory.
* The project follows the requirements of the subject while keeping the code organized.

## Tests

Each exercise includes unit tests.

Run all tests with:

```bash
python manage.py test
```
