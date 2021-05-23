## -- UNDER CONSTRUCTION --

# Python Flask Backend Server

This is a Python Flask application backend server the will serve REST API

To run:
```
pip install -r requirements.txt
python run.py
```

For database migration:
```
export FLASK_APP=run.py
flask db init
flask db migrate
flask db upgrade
```

Note:
```
If chosen flask run to run the server, it is adviced to follow the documentation
https://flask.palletsprojects.com/en/1.1.x/cli/
```



## Tech Stack
- Docker
- Ubuntu 20.04 LTS
- MySQL Database Server
- Flask Microframework
