# imports
import h2o
h2o.init()
from h2o.estimators.glm import H2OGeneralizedLinearEstimator
from h2o.estimators.gbm import H2OGradientBoostingEstimator

# import data
huis = h2o.import_file("huizen.csv")
huis.types

huis['VON'] = huis['VON'].asfactor()
predictors = ["kamers", "Oppervlakte", "VON"]
response_col = "prijs"

### fit linear regression model
glm_model = H2OGeneralizedLinearEstimator(family = "gaussian",  lambda_ = 0, compute_p_values = True)
glm_model.train(predictors, response_col, training_frame= huis)

# Coefficients that can be applied to the non-standardized data.
print(glm_model.coef())

# Coefficients fitted on the standardized data (requires standardize = True, which is on by default)
print(glm_model.coef_norm())

# Print the Coefficients table
glm_model._model_json['output']['coefficients_table']

glm_model

### fit gradient boosting
gbm = H2OGradientBoostingEstimator()
gbm.train(predictors, response_col, training_frame= huis)
gbm


### train automl
from h2o.automl import H2OAutoML

aml = H2OAutoML(max_runtime_secs=120)
aml.train(predictors, response_col, training_frame= huis)

lb = aml.leaderboard
lb.head(rows=lb.nrows)  # Print all rows instead of default (10 rows)


