import os
DATABASE_URI = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser=os.getenv('DBUSER'),
    dbpass=os.getenv('DBPASS'),
    dbhost=os.getenv('DBHOST'),
    dbname=os.getenv('DBNAME')
)
