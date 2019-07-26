# HmtVar  

[HmtVar](https://www.hmtvar.uniba.it) is a database hosting data about human mitochondrial variants, integrated with their pathogenicity predictions. More details can be found on the official paper, whose DOI is [10.1093/nar/gky1024](https://doi.org/10.1093/nar/gky1024).  

## Installation  

1. Create a new virtual environment (Python 3): `virtualenv -p python3.6 venv`  
2. Activate the new virtual environment: `source venv/bin/activate`  
3. Install all the required packages: `pip install -r requirements.txt`  
3a. Will need to have the `update/data/tables/` folder available, with all the required tables in it.  
4. Create the db: `export FLASK_APP=app:app` 
    - `flask create-db`  
5. Update the db: `flask update-db`  
6. Migrate the db: `flask migrate-db`  
7. Update the additional files used by [HmtNote](https://github.com/robertopreste/HmtNote): `flask update-hmtnote`  

## Launch HmtVar instance  

After that, you are ready to launch the HmtVar database using `python run.py`.  

The database will then be available at `127.0.0.1:5000`.  

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


