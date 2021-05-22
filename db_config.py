import os

# Get database credentials from environment variables
# os.getenv(<variable name>, <default value>)
# if <variable name> does not exist, it will use <default value>
# for security purpose, leave the <default value> out
# i.e. os.getenv(<variable name>) which will return None if variable doesnt exist
# for development, it is ok to use os.getenv(<variable name>, <default value>)
# as long as it doesnt get expose to anyone
# Remove any sensitive creds before pushing to public repo

DB_USER = os.getenv("dbuser")
DB_PASS = os.getenv("dbpass")
DB_DB = os.getenv("dbdb")
DB_HOST = os.getenv("dbhost")

# Get string representation of the database uri
DB_URI = 'mysql+pymysql://%s:%s@%s/%s' % (DB_USER, DB_PASS, DB_HOST, DB_DB)

# Pass the uri to sqlaclhemy (ORM - Object Relational Mapping)
SQLALCHEMY_DATABASE_URI = DB_URI

# MySQL settings to supress an error
SQLALCHEMY_TRACK_MODIFICATIONS = True