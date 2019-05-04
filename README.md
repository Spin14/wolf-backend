# wolf backend


## Development

### Setup Poetry

Using [poetry](https://github.com/sdispater/poetry) for project dependency management

```bash
# make sure poetry is installed
$ which poetry
/usr/local/bin/poetry

# how I setup poetry
$ poetry config settings.virtualenvs.create false
$ poetry config settings.virtualenvs.in-project true 

$ poetry config --list                               
settings.virtualenvs.create = false
settings.virtualenvs.in-project = false
settings.virtualenvs.path = "/home/<user>/.cache/pypoetry/virtualenvs"
repositories = {}
```

### Install Dependencies

```bash
# create venv
$ python3.7 -m venv venv
$ source venv/bin/activate

# install project dependencies
$ poetry install
```

### Setup Environment

```bash
# .env for development
$ ln -s .env.dev .env
```

### Lint Checks
```bash
$ flake8 app
```

### Type Checks
```bash
$ mypy app
```

### Run Tests
```bash
$ pytest
============================================================================================ test session starts ============================================================================================
platform linux -- Python 3.7.1, pytest-4.4.1, py-1.8.0, pluggy-0.9.0
rootdir: /home/juan/Projects/WOLF/backend, inifile: setup.cfg
plugins: cov-2.7.1
collected 1 item                                                                                                                                                                                            

tests/test_app.py .                                                                                                                                                                                   [100%]

----------- coverage: platform linux, python 3.7.1-final-0 -----------
Name                Stmts   Miss  Cover
---------------------------------------
app/__init__.py         4      0   100%
app/config.py           3      0   100%
app/endpoints.py        4      0   100%
app/routes.py           4      0   100%
tests/__init__.py       0      0   100%
tests/test_app.py       8      0   100%
---------------------------------------
TOTAL                  23      0   100%

Required test coverage of 100% reached. Total coverage: 100.00%

========================================================================================= 1 passed in 0.12 seconds ==========================================================================================

# for ipdb compatibale test runs
# $ pytest -s

# for detailed coverage report
$ coverage html
$ firefox htmlcov/index.html

```

### Run Server

```bash
# run asgi server with auto load
$ ./dev.sh
```
