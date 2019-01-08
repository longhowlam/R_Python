################################################
##
## basic data prep with pandas

import pandas as pd

## import data sets
huis = pd.read_csv("huizen.csv")
PC = pd.read_csv("postcodes.csv")

## join on postcodes
huis2 = huis.merge(
    PC,
    how = 'left', 
    left_on = 'PC6', 
    right_on = 'Postcode_spatie'
)

## gemiddelde prijs per provincie
Prov = huis2.\
    groupby('province_code')['prijs'].\
    agg(['min', 'max', 'mean', 'median']).\
    sort_values(['mean'])

Prov

## filter data
huis2.query(
 'province_code == "ZE" & \
 prijs > 75000'
)