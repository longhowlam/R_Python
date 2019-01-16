###########################################
##
## Some visualisation in Python

### first import some data
import pandas as pd
huis = pd.read_csv("huizen.csv")

##################### matplotlib ###########################################
import matplotlib.pyplot as plt

## scatterplot
plt.scatter(huis.Oppervlakte, huis.prijs)
plt.show()

## kleur, filter wat outliers weg die de plot anders kapot maken
huis = huis.query('prijs < 1000000 & kamers < 10 & Oppervlakte < 500')
plt.scatter( huis.Oppervlakte, huis.prijs, c = huis.kamers )
plt.xlabel('Oppervlakte')
plt.ylabel('Prijs')
plt.title('Oppervlakte vs Prijs met aantal kamers')
plt.colorbar()
plt.show()

## histograms
plt.hist(
    huis.prijs, 
    20, 
    facecolor = 'g',
    alpha = 0.75,
    histtype='bar', ec='black'
)
plt.show()

## bar plots
typecount = huis["Type"].value_counts()
typecount = typecount[typecount > 1000]
plt.bar(typecount.index, typecount.values)
plt.xticks(rotation=45)
plt.show()


#####################  seaborn ###############################################
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

########## boxplots
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

#############  2d density plots

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

###### plotly plot #################################################################################

#%% werkt niet direct in VSC, alleen met inerteractive notebook viewer

# daarvoor is het wel nodig om data opnieuw in te lezen
import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
import numpy as np

# ruim 100K punten, interactive plot kan net wat traag zijn
# je kan altijd sample trekken
huis = pd.read_csv("huizen.csv")
huis = huis.query('prijs < 1000000 & kamers < 10 & Oppervlakte < 500')
huis = huis.sample(n=10000)

trace = go.Scatter(
    x = huis.Oppervlakte,
    y = huis.prijs,
    mode = 'markers'
)

data = [trace]
py.iplot(data, filename='basic-scatter')


#%% Nog een mooie wiskundige plot --------------------------------------------------------------------------

import plotly.offline as py
import plotly.graph_objs as go
import numpy as np

s = np.linspace(0, 2 * np.pi, 240)
t = np.linspace(0, np.pi, 240)
tGrid, sGrid = np.meshgrid(s, t)

r = 2 + np.sin(7 * sGrid + 5 * tGrid)  # r = 2 + sin(7s+5t)
x = r * np.cos(sGrid) * np.sin(tGrid)  # x = r*cos(s)*sin(t)
y = r * np.sin(sGrid) * np.sin(tGrid)  # y = r*sin(s)*sin(t)
z = r * np.cos(tGrid)                  # z = r*cos(t)

surface = go.Surface(x=x, y=y, z=z)
data = [surface]

layout = go.Layout(
    title='Parametric Plot',
    scene=dict(
        xaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        yaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        zaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        )
    )
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='jupyter-parametric_plot')
