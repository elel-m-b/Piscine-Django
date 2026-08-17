# Django—3-Sessions

A Django project combining the exercises from the training sessions into one application.

## Learning Concepts

### Session 1

* Django project and app structure
* URL routing and views
* Templates
* Django forms
* User registration and authentication
* Sessions

### Session 2

* Django models and relationships
* Creating and displaying data
* Many-to-many relationships
* Voting logic
* Built-in permissions
* Custom permissions

### Session 3

* Custom user models
* Django signals
* Automatic reputation updates
* Permission management based on reputation
* Connecting multiple Django features into one application

## Project Structure

```text
ex/
├── manage.py
├── requirements.txt
├── lpt_site/
├── accounts/
├── tips/
└── templates/
```

## How to Run

```bash
cd ex

python3 -m venv venv
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create the database:

```bash
python3 manage.py migrate
```

Create an admin user:

```bash
python3 manage.py createsuperuser
```

Run the server:

```bash
python3 manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

Admin panel:

```text
http://127.0.0.1:8000/admin/
```

If you modify the models, run:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```
