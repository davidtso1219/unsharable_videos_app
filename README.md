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

2) Create a file called `.env`.
```
touch .env
```

3) Open the file, and if you can find it, go to the direcotry and do command+shift+period to see the hidden files.

3) Set the environment by writing this line in `.env`.
```
FLASK_APP=app
```

5) Finally, do the following command to run the app locally!
```
flask run
```