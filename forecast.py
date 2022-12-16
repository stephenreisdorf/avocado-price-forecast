# %%
import pandas as pd
import numpy as np
from plotly import graph_objects as go
import random

from prophet import Prophet

# %%
avocado_df = pd.read_csv("data/avocado.csv")
avocado_df

# %%
avocado_df.info()

# %%
avocado_df.set_index("Date", inplace=True)
avocado_df.sort_index(inplace=True)
avocado_df.drop('Unnamed: 0', axis="columns", inplace=True)
avocado_df

# %%
fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=avocado_df.index
        , y=avocado_df["AveragePrice"]
    )
)
fig

# %%
fig = go.Figure()
fig.add_trace(
    go.Violin(
        x=avocado_df["AveragePrice"]
    )
)
fig

# %%
counts = avocado_df.groupby("region").count()
fig = go.Figure()
fig.add_trace(
    go.Bar(
        x=counts.index
        , y=counts["AveragePrice"]
    )
)

# %%
counts = avocado_df.groupby("year").count()
fig = go.Figure()
fig.add_trace(
    go.Bar(
        x=counts.index
        , y=counts["AveragePrice"]
    )
)

# %%
conventional_df = avocado_df[ avocado_df["type"] == "conventional" ]
fig = go.Figure()
for region in conventional_df["region"].unique():
    fig.add_trace(
        go.Box(
            x=conventional_df[ conventional_df["region"] == region ]["AveragePrice"]
            , name=region
        )
    )
fig

# %%
conventional_df = avocado_df[ avocado_df["type"] == "organic" ]
fig = go.Figure()
for region in conventional_df["region"].unique():
    fig.add_trace(
        go.Box(
            x=conventional_df[ conventional_df["region"] == region ]["AveragePrice"]
            , name=region
        )
    )
fig

# %%
avocado_prophet_df = avocado_df.reset_index()[["Date", "AveragePrice"]]
avocado_prophet_df.columns = ["ds", "y"]
avocado_prophet_df

# %%
model = Prophet()
model.fit(avocado_prophet_df)
future = model.make_future_dataframe(periods=365)
future

# %%
forecast = model.predict(future)
forecast

# %%
model.plot(forecast)

# %%
model.plot_components(forecast)

# %%
from prophet.plot import plot_plotly, plot_components_plotly

plot_plotly(model, forecast)

# %%
plot_components_plotly(model, forecast)

# %%
