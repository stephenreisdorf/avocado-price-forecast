import streamlit as st
from plotly import graph_objects as go

from scripts.prepare import extract_and_transform

df = extract_and_transform()

st.title("Data Exploration")

st.header("Average Price Trend")
region_sel = st.selectbox("Region", options=df["region"].unique())
type_sel = st.selectbox("Type", options=df["type"].unique())

avg_price_trend_df = df[ 
    (df["region"] == region_sel)
    & (df["type"] == type_sel)
]
fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=avg_price_trend_df.index
        , y=avg_price_trend_df["AveragePrice"]
        , mode="markers"
    )
)

st.plotly_chart(fig)

st.header("Conventional Avocodo Prices By Region")

conventional_df = df[ df["type"] == "conventional" ]
fig = go.Figure()
for region in conventional_df["region"].unique():
    fig.add_trace(
        go.Box(
            x=conventional_df[ conventional_df["region"] == region ]["AveragePrice"]
            , name=region
        )
    )
st.plotly_chart(fig)

st.header("Organic Avocodo Prices By Region")

organic_df = df[ df["type"] == "organic" ]
fig = go.Figure()
for region in organic_df["region"].unique():
    fig.add_trace(
        go.Box(
            x=organic_df[ organic_df["region"] == region ]["AveragePrice"]
            , name=region
        )
    )
st.plotly_chart(fig)

st.header("Dataframe View")
st.dataframe(df)
