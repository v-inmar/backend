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
https://flask.palletsprojects.com/en/2.0.x/cli/
```



## Tech Stack
- Docker
- Ubuntu 20.04 LTS
- MySQL Database Server
- Flask Microframework


## May 24 2021
## Version 1.0.0

Does not have authentication. Should only be run locally

Client Requirements
```
Accept Header - application/json
```

API Routes
```
1. Create new Note
POST
http://localhost:5000/notes

2. Get Note by pid
GET
http://localhost:5000/notes/<string:pid>

3. Get all Notes
GET
http://localhost:5000/notes

4. Update a Note by pid
PUT
http://localhost:5000/notes/<string:pid>

5. Delete Note by pid
DELETE
http://localhost:5000/notes/<string:pid>
```