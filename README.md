# Unsharable Videos App

## Final Release
https://david-first-webapp-on-heroku.herokuapp.com/

## Structure
```
unsharable_videos_app/
  app/
    templates/
      index.html
    __init__.py
    routes.py
  run.py
  config.py
```

## Running the application
1) Run setup.sh to set up the virtual environment. Just do the following command:
```
source setup.sh
```

2) Create a file called `.env` to set the environment.
```
FLASK_APP=app
```

3) Install the python-dotenv package to register environment
variables to be automatically imported when running the `flask` command.
```
(venv) $ pip install python-dotenv
```   

4) Finally, do the following command to run the app locally!
```
flask run
```