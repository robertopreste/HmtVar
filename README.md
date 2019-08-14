# HmtVar  

[HmtVar](https://www.hmtvar.uniba.it) is a database hosting data about human mitochondrial variants, integrated with their pathogenicity predictions. More details can be found on the official paper, whose DOI is [10.1093/nar/gky1024](https://doi.org/10.1093/nar/gky1024).  

## Installation  

Only the first time the database is set up:  

1. Create a new virtual environment (Python 3): `virtualenv -p python3.6 venv`  
2. Activate the virtual environment: `source venv/bin/activate`  
3. Install all the required packages: `pip install -r requirements.txt`  
3a. Will need to have the `update/data/tables/` folder available, with all the required tables in it.  
4. Export the needed variables: `export FLASK_APP=app:app`  
5. Create the db: `flask create-db`  
6. Update the db: `flask update-db`  
7. Migrate the db: `flask migrate-db`  
8. Update the additional files used by [HmtNote](https://github.com/robertopreste/HmtNote): `flask update-hmtnote`  

Everytime you need to update the database with new data (from the tables in `update/data/tables/`), you need to repeat steps 4, 6, 7, 8 (**not 5!**).  

When finished, deactivate the virtual environment: `deactivate`.  

## Updates  

Details about each update of the public HmtVar instance can be found in the [CHANGELOG](/CHANGELOG.md) file.  
Details about the data updating protocol can be found in the [UPDATE.md](/update/UPDATE.md) file.  
After the updating procedure is complete, please run `flask migrate-db`, then `systemctl restart HmtVar` (with `sudo` if needed).  

## HmtVar instance  

HmtVar is served using [gunicorn](https://gunicorn.org); please ask your system admin for help about this.  

## Citing HmtVar  

HmtVar can be cited as:  

>Preste R, Vitale O, Clima R, Gasparre G, Attimonelli M  
>
>**HmtVar: a new resource for human mitochondrial variations and pathogenicity data.**  
>
>[*Nucleic Acids Res. 2018 Oct 29.*](https://doi.org/10.1093/nar/gky1024)  


