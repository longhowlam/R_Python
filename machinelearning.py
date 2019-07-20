########################################################
##
## enkele voorbeelden machine learning in Scikit learn

### huizen data

import pandas as pd
import numpy as np

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

## Python is wat 'kaal' in de output, plak zelf de namen er bij
cdf = pd.DataFrame(outlm.coef_, X.columns, columns=['Coefficients'])
print(cdf)

# bereken predictions en r kwadraat 
y_pred = outlm.predict(X)
r2_score(y,y_pred)  

## wat zou er gebeuren als je DR niet zou weglaten
huis3 = huis2.dropna(subset= ['kamers', 'Oppervlakte', 'prijs', 'province_code'])
feature_cols = ['kamers', 'Oppervlakte' , 'province_code']
X = huis3.loc[:, feature_cols]
y = huis3.prijs

## maak dummies en fit
X = pd.get_dummies(X, columns=["province_code"])
outlm = lr.fit(X,y)

cdf = pd.DataFrame(outlm.coef_, X.columns, columns=['Coefficients'])
print(cdf)

#### som van de eerste 11 prov parameters is de negatieve 12e parameter
np.sum(outlm.coef_[2:13])
outlm.coef_[13]
## het blijkt dat we de zogenaamde sum contrast in R hebben.



##################################################################################
##
## classification model

import pandas as pd

## import titanic data set
titanic = pd.read_csv("titanic.csv")
titanic.shape

# define decision tree object from scikit learn
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier(
    random_state = 1337,
    criterion = 'gini',
    splitter = 'best',
    max_depth = 5,
    min_samples_leaf = 10
)

# Features for which we drop rows with missing values"
drop_rows_when_missing = ['Age', 'Pclass']
for feature in drop_rows_when_missing:
    titanic = titanic[titanic[feature].notnull()]

titanic.shape

# dummie encoding # Only keep the top 100 values
LIMIT_DUMMIES = 100
from collections import defaultdict, Counter

categorical_to_dummy_encode = ['Pclass', 'Sex']

def select_dummy_values(train, features):
    dummy_values = {}
    for feature in categorical_to_dummy_encode:
        values = [
            value
            for (value, _) in Counter(train[feature]).most_common(LIMIT_DUMMIES)
        ]
        dummy_values[feature] = values
    return dummy_values

DUMMY_VALUES = select_dummy_values(titanic, categorical_to_dummy_encode)

def dummy_encode_dataframe(df):
    for (feature, dummy_values) in DUMMY_VALUES.items():
        for dummy_value in dummy_values:
            dummy_name = u'%s_value_%s' % (feature, dummy_value)
            df[dummy_name] = (df[feature] == dummy_value).astype(float)
        del df[feature]

dummy_encode_dataframe(titanic)

# show the created dummy columns
titanic[['Pclass_value_1', 'Pclass_value_2', 'Pclass_value_3', 'Sex_value_male', 'Sex_value_female']]

# set X and Y, the input features and the target
X = titanic.iloc[:,[3,10,11,12,13,14]] 
Y = titanic['Survived']

# train the decison tree
clf.fit(X, Y)

# plot the tree
import graphviz 
dot_data = tree.export_graphviz(clf, out_file=None) 
graph = graphviz.Source(dot_data) 
graph.render("titanic") 

dot_data = tree.export_graphviz(
    clf, out_file=None, 
    feature_names = list(X),  
    class_names = ['Y','N'],  
    filled=True, rounded=True,  
    special_characters=True
)  
graph = graphviz.Source(dot_data)  
graph.render("titanic") 

#### area under curve metric
# comparison of predicted scores and the true label
pred_scores = clf.predict_proba(X)

# The magic happens in the scikit-plot package.....
import matplotlib.pyplot as plt
import scikitplot as skplt
skplt.metrics.plot_roc(titanic.Survived, pred_scores)
plt.show()
