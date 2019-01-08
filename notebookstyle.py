#%% [markdown]

## Inleiding 

# Sinds de november release van VSC is het mogelijk om interactieve python code
# te runnen in notebook styl. Markdown cellen en code cellen kunnen aangemaakt
# worden met #%% [markdown] en #%%


#%%
# gewone python code
import pandas as pd

huis = pd.read_csv("huizen.csv")
PC = pd.read_csv("postcodes.csv")

## join on postcodes
huis2 = huis.merge(
    PC,
    how = 'left', 
    left_on = 'PC6', 
    right_on = 'Postcode_spatie'
)
Prov = huis2.\
    groupby('province_code')['prijs'].\
    agg(['min', 'max', 'mean', 'median']).\
    sort_values(['mean'])

Prov

#%% [markdown]

# Ook plaatjes kunnen worden gemaakt

#%% [markdown]
# 3D wiskundig plaatje

#%%
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

#%%
# simpel barchart

#%%
data = [go.Bar(
            x = Prov.index,
            y = Prov['median']
    )]

py.iplot(data, filename='basic-bar')