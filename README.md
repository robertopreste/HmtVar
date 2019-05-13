# HmtVar  

[HmtVar](https://www.hmtvar.uniba.it) is a database hosting data about human mitochondrial variants, integrated with their pathogenicity predictions. More details can be found on the official paper, whose DOI is [10.1093/nar/gky1024](https://doi.org/10.1093/nar/gky1024).  

## Installation  

1. Create a new virtual environment (Python 3): `virtualenv -p python3 venv`  
2. Activate the new virtual environment: `source venv/bin/activate`  
3. Install all the required packages: `pip install -r requirements.txt`  
4. Login as root into MySQL: `mysql -u root -p`  
5. Create a new user for HmtVar:  
```mysql
USE mysql;
CREATE USER 'hmtvar_admin'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'hmtvar_admin'@'localhost';
FLUSH PRIVILEGES;
```
6. Exit MySQL (using `\q`) and enter back using the new user: `mysql -u username -p`  
7. Create the database: `CREATE DATABASE HmtVar;`  
8. Instantiate and populate the db:  
```python
from app import db
db.drop_all()
db.create_all()
```
9. Upload the tables to the database: 
```bash
export FLASK_APP=app:app
flask update-db
```  
10. Migrate the db (actually saves data needed to populate HTML menus): `flask migrate-db`  


## Launch HmtVar instance  

After that, you are ready to launch the HmtVar database using `python run.py`.  

Data offered here are only 5% of those available on the real [HmtVar](https://www.hmtvar.uniba.it), but nonetheless the system is fully functional.  
The database can be launched with `python run.py`, and will then be available at `127.0.0.1:5000`.  

## Updates  

Details about each update of the public HmtVar instance can be found in the [CHANGELOG](/CHANGELOG.md) file.  
Statistics shown in this file are referred to the public database, not the subset of data available in this repository, which is always restricted to the 5% of the total data.  

## Citing HmtVar  

HmtVar can be cited as:  

>Preste R, Vitale O, Clima R, Gasparre G, Attimonelli M  
>
>**HmtVar: a new resource for human mitochondrial variations and pathogenicity data.**  
>
>[*Nucleic Acids Res. 2018 Oct 29.*](https://doi.org/10.1093/nar/gky1024)  


