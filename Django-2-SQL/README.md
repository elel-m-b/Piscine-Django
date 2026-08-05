# Django_2_SQL: Django & PostgreSQL: Raw SQL vs ORM

## What I learned today

Today I learned two different ways to interact with a PostgreSQL database in Django.
The first approach was using **raw SQL** with the `psycopg2` library. In this case, I had to write every SQL query myself, manage the database connection, execute the queries, and handle possible errors.
The second approach was using **Django ORM (Object-Relational Mapping)**. Instead of writing SQL manually, I worked with Python classes and methods, and Django generated the SQL queries automatically.
Learning both approaches helped me understand what the ORM is actually doing behind the scenes.

---

# Key Concepts

## SQL vs ORM

### Raw SQL

Raw SQL means writing SQL commands directly.

Example:

```sql
SELECT * FROM movies;
```

With this approach, I have complete control over every query. However, I also have more responsibility because I must:

- Write valid SQL syntax.
- Open and close database connections.
- Handle errors.
- Prevent SQL injection.
- Keep the code organized.

Raw SQL is powerful, but it can become difficult to maintain as a project grows.

---

### Django ORM

ORM stands for **Object-Relational Mapping**.

Instead of writing SQL queries, I work with Python objects.

Example:

```python
Movies.objects.all()
```

Django automatically converts this into the appropriate SQL query.

The ORM makes development faster, cleaner, and easier to maintain. Even though I don't write SQL directly, SQL is still executed behind the scenes.

Understanding SQL first makes it much easier to understand how the ORM works.

---

## Django Project vs App

A **project** is the entire Django application.

It contains:

- Project settings
- Main URLs
- Configuration
- Database settings

An **app** is a small part of the project that focuses on one feature.

For these exercises, each exercise is organized inside its own app. This keeps the project modular and easier to manage.

---

## Views

A **view** is a Python function (or class) that receives a request from the user and returns a response.

The view is where most of the application's logic lives.

For example, a view can:

- Read data from the database.
- Insert new records.
- Update existing data.
- Delete records.
- Display an HTML page.

The browser communicates with the view, and the view communicates with the database.

---

## Models

A **model** is a Python class that represents a database table.

Each class attribute becomes a column inside the database.

Example:

```python
class Movies(models.Model):
    title = models.CharField(max_length=64)
```

Instead of manually creating tables with SQL, I simply describe the table using Python, and Django creates it for me.

Models also make the code easier to read because they represent real objects instead of SQL tables.

---

## Migrations

A migration is a file that records changes made to the models.

Whenever I modify a model, Django can generate a migration that updates the database schema.

Typical workflow:

```bash
python manage.py makemigrations
python manage.py migrate
```

I think of migrations as version control for the database.

Instead of manually editing tables, Django keeps track of every change.

---

## Database Constraints

Constraints are rules that protect the database from invalid data.

### NOT NULL

The field cannot be empty.

### UNIQUE

Two rows cannot contain the same value.

### PRIMARY KEY

Uniquely identifies every row in a table.

Usually this is the `id` field.

### FOREIGN KEY

Creates a relationship between two tables.

For example, a character can belong to one planet.

Constraints help maintain data integrity regardless of whether I use SQL or the ORM.

---

## CRUD Operations

Almost every database application performs four basic operations.

### Create

Insert new data into the database.

Example:

- Create a table.
- Add a movie.

---

### Read

Retrieve data from the database.

Example:

- Display every movie.

---

### Update

Modify existing data.

Example:

- Change a movie title.

---

### Delete

Remove data from the database.

Example:

- Delete a movie.

The exercises followed this exact order, making it easy to understand how databases work.

---

## Triggers

A trigger is a function that PostgreSQL executes automatically when a specific event happens.

For example, before updating a row, a trigger can automatically update the `updated` timestamp while keeping the `created` timestamp unchanged.

This is useful because the rule is enforced directly by the database, regardless of which application modifies the data.

---

## Relationships Between Tables

### One-to-Many (Foreign Key)

One record can be related to many other records.

Example:

- One planet can be the homeworld of many characters.

This relationship is created using a **ForeignKey**.

---

### Many-to-Many

Many records from one table can be connected to many records from another table.

Example:

- One movie has many characters.
- One character appears in many movies.

Django automatically creates an intermediate table (called a join table) to manage this relationship.

---

# What I understood today

The most important thing I learned is that **the Django ORM does not replace SQL**.

It simply writes SQL for me.

When I call:

```python
Movies.objects.create(...)
```

Django generates an SQL `INSERT` query.

When I call:

```python
Movies.objects.filter(...)
```

Django generates an SQL `SELECT` query.

Knowing SQL helps me understand what Django is doing internally and makes debugging much easier.

---

# Resources

## Django Documentation

- https://docs.djangoproject.com/en/stable/topics/db/models/
- https://docs.djangoproject.com/en/stable/topics/migrations/
- https://docs.djangoproject.com/en/stable/ref/models/querysets/

## PostgreSQL Documentation

- https://www.postgresql.org/docs/

## psycopg2 Documentation

- https://www.psycopg.org/docs/

## SQL Learning

- https://www.w3schools.com/sql/
- https://sqlbolt.com/
- https://www.postgresqltutorial.com/
