# enkele voorbeelden machine learning

from sklearn import datasets
from sklearn.model_selection import cross_val_predict
from sklearn import linear_model
import matplotlib.pyplot as plt
import umap


########## SK LEARN TEST ########################################################
lr = linear_model.LinearRegression()
boston = datasets.load_boston()

#info on data https://scikit-learn.org/stable/datasets/index.html#boston-dataset

type(boston.data)
boston.data

y = boston.target

predicted = cross_val_predict(lr, boston.data, y, cv=10)

fig, ax = plt.subplots()
ax.scatter(y, predicted, edgecolors=(0, 0, 0))
ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()

########## UMAP TEST ############################################################

digits = datasets.load_digits()

embedding = umap.UMAP().fit_transform(digits.data)
exit()
