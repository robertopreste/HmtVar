# HmtVar  

## Installation  

1. Create a new virtual environment (Python 3): `virtualenv -p python3 venv`  
2. Activate the new virtual environment: `source venv/bin/activate`  
3. Install all the required packages: `pip install -r requirements.txt`  

If you want to create a brand-new database:  
1. Create the empty database: `python db_create.py`  
2. Migrate the database: `python db_migrate.py`  
3. Populate the database with the `sqlite3` command, then migrate the database again: `python db_migrate.py`  


