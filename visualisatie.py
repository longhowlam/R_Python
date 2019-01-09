###########################################
##
## Some visualisation in Python

### first some data
import pandas as pd
huis = pd.read_csv("huizen.csv")

#### matplotlib
import matplotlib.pyplot as plt

## scatterplot
plt.scatter(huis.Oppervlakte, huis.prijs)
plt.show()

## kleur
huis = huis.query('prijs < 1000000 & kamers < 10 & Oppervlakte < 500')
plt.scatter(huis.Oppervlakte, huis.prijs, c = huis.kamers)
plt.xlabel('Oppervlakte')
plt.ylabel('Prijs')
plt.title('Oppervlakte vs Prijs met aantal kamers')
plt.colorbar()
plt.show()

## histograms
plt.hist(huis.prijs, 20, density=1, facecolor='g', alpha=0.75)
plt.show()

## bar plots
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]
plt.figure(1, figsize=(9, 3))
plt.bar(names, values)
plt.show()


#####################  seaborn #############################

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

################## boxplots
PC = pd.read_csv("postcodes.csv")

## join on postcodes
huis2 = huis.merge(
    PC,
    how = 'left', 
    left_on = 'PC6', 
    right_on = 'Postcode_spatie'
)

sns.set(style="ticks", palette="pastel")

# Draw a nested boxplot to show bills by day and time
sns.boxplot(
    x = "province_code", 
    y = "prijs",
    data = huis2)
sns.despine(offset=10, trim=True)
plt.show()




##################  2d density plots

sns.set(style="dark")
rs = np.random.RandomState(50)

# Set up the matplotlib figure
f, axes = plt.subplots(3, 3, figsize=(9, 9), sharex=True, sharey=True)

# Rotate the starting point around the cubehelix hue circle
for ax, s in zip(axes.flat, np.linspace(0, 3, 10)):
    # Create a cubehelix colormap to use with kdeplot
    cmap = sns.cubehelix_palette(start=s, light=1, as_cmap=True)
    # Generate and plot a random bivariate dataset
    x, y = rs.randn(2, 50)
    sns.kdeplot(x, y, cmap=cmap, shade=True, cut=5, ax=ax)
    ax.set(xlim=(-3, 3), ylim=(-3, 3))

f.tight_layout()
plt.show()
