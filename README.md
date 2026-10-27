# Portfolio
Portfolio website using Python and Flask.

## Setup

Use Python 3.10 or newer for the pinned dependency versions.

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
flask --app server run
```

For PythonAnywhere, recreate the virtual environment with a supported Python version,
install requirements.txt, point the web app at that environment, and reload the app.
Keep debug mode disabled in production.

## Dependencies and checks

Requirements include only Flask and its pinned runtime dependencies. Removed packages
were not imported by server.py. The removed npm lockfile described a language-server
sample; this site has no npm manifest or Node build step and serves existing CSS and
JavaScript directly.

```sh
python -m unittest discover -s tests -v
python -m pip check
python -m pip install pip-audit==2.10.1
python -m pip_audit -r requirements.txt
```

Contact-form tests write only to a temporary directory. CI runs application and
vulnerability checks on Python 3.10 and 3.14 for pushes and pull requests.
