######### imports needed ##########

import mleap.sklearn.pipeline
import mleap.sklearn.feature_union
import mleap.sklearn.base
import mleap.sklearn.logistic
import mleap.sklearn.preprocessing.data

## packages
from sklearn.model_selection import cross_val_predict
from sklearn import linear_model
import matplotlib.pyplot as plt

from mleap.sklearn.ensemble import forest
from mleap.sklearn.preprocessing.data import FeatureExtractor, LabelEncoder, ReshapeArrayToN1

from sklearn.linear_model import LinearRegression
from sklearn.ensemble.forest import RandomForestRegressor
from sklearn.pipeline import Pipeline, FeatureUnion

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Imputer
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import OneHotEncoder

import numpy as np
import pandas as pd




############ import huizen data sets #################################

huis = pd.read_csv("huizen.csv")
PC = pd.read_csv("postcodes.csv")

## join on postcodes
huis2 = huis.merge(
    PC,
    how = 'left', 
    left_on = 'PC6', 
    right_on = 'Postcode_spatie'
).query('prijs > 50000 & prijs < 2000000')


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
outlm
## bekijk coefficienten
outlm.intercept_
outlm.coef_

############  model pipeline #################

# Define our linear regression
feature_extractor_tf = FeatureExtractor(
    input_scalars = feature_cols, 
    output_vector = 'unscaled_cont_features'
)

# Vector Assembler, for serialization purposes only
feature_extractor_lr_model_tf = FeatureExtractor(
    input_vectors = [feature_extractor_tf], 
    output_vector = 'input_features'
)

feature_extractor_lr_model_tf.skip_fit_transform = True

# Define our linear regression
lr_model = LinearRegression()
lr_model.mlinit(
    input_features = 'input_features',
    prediction_column = 'prijs'
)

lr_model_pipeline = Pipeline([
    (feature_extractor_lr_model_tf.name, feature_extractor_lr_model_tf),
    (lr_model.name, lr_model)
])
lr_model_pipeline.mlinit()
model_pipeline = Pipeline([
    (feature_union.name, feature_union),
    (lr_model_pipeline.name, lr_model_pipeline)
])

model_pipeline.mlinit()
### train the pipeline
lr_model_pipeline.fit(X,y)

lr_model_pipeline.steps[1][1].coef_
lr_model_pipeline.steps[1][1].intercept_

lr_model_pipeline.
lr_model_pipeline.serialize_to_bundle('tmp', 'huisprijs.lr', init=True)


model_pipeline.steps


