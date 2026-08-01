# Training Python-Django - 1

Solutions for exercises 00 to 05.

## ex00 - Antigravity
`geohashing.py` computes a geohash from a latitude/longitude pair.
```bash
python3 ex00/geohashing.py 57.64911 10.40744 6
```

## ex01 - Pip
`my_script.sh` installs the `path` library (formerly path.py) from GitHub
into `local_lib`, logs the install, then runs `my_program.py`.
```bash
cd ex01
./my_script.sh
```

## ex02 - Request an API
`request_wikipedia.py` queries the Wikipedia API for a search term and
writes the plain-text article content to `<term>.wiki`.
```bash
cd ex02
pip install -r requirements.txt
python3 request_wikipedia.py "chocolatine"
```

## ex03 - HTML Parser
`roads_to_philosophy.py` follows the "Getting to Philosophy" chain of
first links starting from a given Wikipedia search term.
```bash
cd ex03
pip install -r requirements.txt
python3 roads_to_philosophy.py "42 (number)"
```

## ex04 - Virtualenv
`my_script.sh` creates a `django_venv` virtualenv, installs
`requirement.txt` (django + psycopg2) inside it, and leaves it activated.
```bash
cd ex04
source my_script.sh
```

## ex05 - Hello World
A minimal Django project with an app serving "Hello World!" at
`/helloworld`.
```bash
cd ex05
pip install -r requirements.txt
cd helloworld_project
python3 manage.py migrate
python3 manage.py runserver
```
Visit http://localhost:8000/helloworld
