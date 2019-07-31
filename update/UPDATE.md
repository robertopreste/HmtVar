# HmtVar update  

After updating HmtDB (and having generated the related **complete** datasets), you will need the results of allele frequencies and ntvar calculations. Place them into `basic/freqs/` and `basic/sitevars/`, respectively; you should have a similar structure:  

```
- update/
    - basic/ 
        - freqs/ 
            sitevar_AF_H_compl.csv
            sitevar_AF_P_compl.csv
            ...
            sitevar_tot_H_compl.csv
            sitevar_tot_P.compl.csv
        - sitevars/ 
            ntvar_healthy_complete.csv
            ntvar_patient_complete.csv
        update_frequency.py
        update_pathogenicity.py
        update_variability.py
    - data/ 
        - tables/ 
            Annot.csv
            CrossRef.csv
            ...
            Scores.csv
            Variab.csv
```

**Please rename the allele frequency files as `var_af_h.csv` and so on.**  

## Allele frequency  

Change directory to `basic/` and use the `update_frequency.py` script to update allele frequencies, as follows:  

```shell script
python update_frequency.py -m ../data/tables/Main.csv -v ../data/tables/Variab.csv
```

The resulting file will be saved as `Variab_new_freqs.csv`; rename it as `Variab.csv` and move it to `data/tables/`.  

## Variability  

From `basic/`, use the `update_variability.py` script:  

```shell script
python update_variability.py -m ../data/tables/Main.csv -v ../data/tables/Variab.csv
```

The resulting file will be saved as `Variab_new_vars.csv`; rename it as `Variab.csv` and move it to `data/tables/`.  

## Update pathogenicity  

From `basic/`, use the `update_pathogenicity.py` script:  

```shell script
python update_pathogenicity.py -m ../data/tables/Main.csv -v ../data/tables/Variab.csv
```

The resulting file will be saved as `Main_new_patho.csv`; rename it as `Main.csv` and move it to `data/tables/`.  

___  

You are now ready to update the database as described in the [README](../README.md).  

