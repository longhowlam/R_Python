########################################################
##
## enkele voorbeelden machine learning in Scikit learn

### huizen data

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
).query('prijs > 50000 & prijs < 2000000')



## packages
from sklearn.model_selection import cross_val_predict
from sklearn import linear_model
import matplotlib.pyplot as plt

## Create a Scikit learn linear model object ########################
lr = linear_model.LinearRegression()

## select features and set target en haal missende waarden weg
feature_cols = ['kamers', 'Oppervlakte']
## haal missende waarden weg
huis3 = huis2.dropna(subset= ['kamers', 'Oppervlakte', 'prijs'])

X = huis3.loc[:, feature_cols]
y = huis3.prijs

## fit model
outlm = lr.fit(X,y)

## bekijk coefficienten
outlm.intercept_
outlm.coef_

# bereken predictions en r kwadraat 
y_pred = outlm.predict(X)

from sklearn.metrics import r2_score
r2_score(y,y_pred)  

# plot predictie tegen voorspelling
plt.scatter(y_pred, y,  color='black')
plt.show()


########### dummy variables
## haal missende waarden weg

huis3 = huis2.dropna(subset= ['kamers', 'Oppervlakte', 'prijs', 'province_code'])
feature_cols = ['kamers', 'Oppervlakte' , 'province_code']
X = huis3.loc[:, feature_cols]
y = huis3.prijs

## maak dummies en laat DR weg
X = pd.get_dummies(X, columns=["province_code"])
X = X.drop('province_code_DR', axis=1)
outlm = lr.fit(X,y)

## bekijk coefficienten
outlm.intercept_
outlm.coef_

# bereken predictions en r kwadraat 
y_pred = outlm.predict(X)
r2_score(y,y_pred)  
