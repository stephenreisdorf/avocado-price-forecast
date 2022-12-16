import streamlit as st
from plotly import graph_objects as go

from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly

from scripts.prepare import extract_and_transform

df = extract_and_transform()

st.title("Forecast")
region_sel = st.selectbox("Region", options=df["region"].unique())
type_sel = st.selectbox("Type", options=df["type"].unique())

model_df = df[ 
    (df["region"] == region_sel)
    & (df["type"] == type_sel)
]
model_df = model_df.reset_index()[["Date", "AveragePrice"]]
model_df.columns = [ "ds", "y" ]
model = Prophet()
model.fit(model_df)

future = model.make_future_dataframe(periods=365)
forecast = model.predict(future)

st.header("Model Plot")
st.plotly_chart(plot_plotly(model, forecast))

st.header("Components Plot")
st.plotly_chart(plot_components_plotly(model, forecast))
