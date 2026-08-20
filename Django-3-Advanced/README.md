# Training Python-Django 3 Advanced — Hellenica

A simple Django project that combines the 7 exercises from the **Training Python-Django 3 Advanced** subject.

Hellenica is a small publishing website about Ancient Greece. Users can register, publish articles, save favourites, switch between English and French, and use the Django admin.

## Features

* User registration and login
* Create and view articles
* Personal publications
* Favourite articles
* Bootstrap styling
* English / French translations
* Django generic class-based views
* Custom template filters
* Fixtures with sample data
* Automated tests

## Project Structure

```text
ex/
├── manage.py
├── requirements.txt
├── hellenica/
│   ├── settings.py
│   └── urls.py
├── articles/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── tests.py
│   ├── admin.py
│   ├── context_processors.py
│   ├── templatetags/
│   └── fixtures/
├── templates/
│   ├── base.html
│   ├── articles/
│   └── registration/
└── locale/
    └── fr/
```

## Requirements

* Python 3.10+
* pip
* gettext (only needed when editing translations)

## Installation

```bash
cd ex

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python3 manage.py migrate
python3 manage.py loaddata articles/fixtures/users.json articles/fixtures/articles.json

python3 manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

Admin:

```text
http://127.0.0.1:8000/admin/
```

To create an admin user:

```bash
python3 manage.py createsuperuser
```

## Sample Accounts

All sample users use:

```text
Password: hellenica123
```

| Username  | Description                   |
| --------- | ----------------------------- |
| homer     | Has sample favourite articles |
| sappho    | Sample user                   |
| herodotus | Sample user                   |

## Exercises

### Exercise 00 — Models and Generic Views

* Created `Article` model
* Created `UserFavouriteArticle` model
* Article list page
* Login page
* Sample fixtures

### Exercise 01 — Articles and Favourites

* Article details
* User publications
* Favourite articles
* Logout
* Login protection

### Exercise 02 — CreateView

* User registration
* Publish articles
* Add articles to favourites
* Automatic article author assignment

### Exercise 03 — Template Tags

* Global navigation menu
* Login form in the menu
* Custom `short_synopsis` filter
* Custom `days_since` filter
* Newest articles first

### Exercise 04 — Bootstrap

* Bootstrap navbar
* Styled forms
* Styled tables
* Responsive layout

### Exercise 05 — Internationalization

* English and French
* Language switcher
* `/en/` and `/fr/` URLs
* Django translation files

### Exercise 06 — Testing

The project contains tests for:

* Authentication
* Access control
* Registration
* Publishing articles
* Favourite articles
* Duplicate favourites

Run the tests:

```bash
python3 manage.py test articles
```

## Quick Test

After starting the server:

1. Open `/`
2. Login with `homer`
3. Open **Publications**
4. Create an article
5. Open an article and add it to favourites
6. Open **Favourites**
7. Switch between English and French
8. Logout
9. Run the tests

## Useful Django Commands

```bash
# Start server
python3 manage.py runserver

# Create migrations
python3 manage.py makemigrations

# Apply migrations
python3 manage.py migrate

# Run tests
python3 manage.py test

# Create admin user
python3 manage.py createsuperuser

# Load sample data
python3 manage.py loaddata articles/fixtures/users.json articles/fixtures/articles.json
```

## Resources

* [Django Documentation](https://docs.djangoproject.com/)
* [Django Generic Views](https://docs.djangoproject.com/en/5.2/topics/class-based-views/)
* [Django Models](https://docs.djangoproject.com/en/5.2/topics/db/models/)
* [Django Forms](https://docs.djangoproject.com/en/5.2/topics/forms/)
* [Django Authentication](https://docs.djangoproject.com/en/5.2/topics/auth/)
* [Django Testing](https://docs.djangoproject.com/en/5.2/topics/testing/)
* [Django Internationalization](https://docs.djangoproject.com/en/5.2/topics/i18n/)
* [django-bootstrap5](https://django-bootstrap5.readthedocs.io/)
* [Bootstrap](https://getbootstrap.com/)

## Troubleshooting

**Django is not installed**

```bash
pip install -r requirements.txt
```

**Database tables are missing**

```bash
python3 manage.py migrate
```

**No articles appear**

```bash
python3 manage.py loaddata articles/fixtures/users.json articles/fixtures/articles.json
```

**French translation does not work**

Make sure the compiled translation file exists:

```text
locale/fr/LC_MESSAGES/django.mo
```

If you changed translations:

```bash
python3 manage.py makemessages -l fr
python3 manage.py compilemessages
```

## Tech Stack

* Python
* Django 5.2
* SQLite
* django-bootstrap5
* HTML / CSS
* Django Templates
* Django Test Framework
* gettext
