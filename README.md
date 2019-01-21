# HmtVar  

[HmtVar](https://www.hmtvar.uniba.it) is a database hosting data about human mitochondrial variants, integrated with their pathogenicity predictions. More details can be found on the official paper, whose DOI is [10.1093/nar/gky1024](https://doi.org/10.1093/nar/gky1024).  

## Installation  

1. Create a new virtual environment (Python 3): `virtualenv -p python3 venv`  
2. Activate the new virtual environment: `source venv/bin/activate`  
3. Install all the required packages: `pip install -r requirements.txt`  

## Launch HmtVar instance  

After that, you are ready to launch the HmtVar database using `python run.py`.  

Data offered here are only 5% of those available on the real [HmtVar](https://www.hmtvar.uniba.it), but nonetheless the system is fully functional.  
The database can be launched with `python run.py`, and will then be available at `127.0.0.1:5000`.  


