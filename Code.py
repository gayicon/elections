import streamlit as st
import plotly.express as px
import pandas as pd

# Load election and GDP data
election_data = px.data.election()
gdp_data = px.data.gapminder()

# Filter GDP data for the United States
us_gdp = gdp_data[gdp_data['country'] == 'United States']

# Merge the data (for demonstration purposes, assume matching by year and state)
merged_data = pd.merge(election_data, us_gdp, left_on='year', right_on='year')

# Create the Plotly figure
fig = px.scatter(merged_data, x="gdpPercap", y="votes", color="party",
                 hover_name="district", title="Election Results vs. GDP per Capita")

# Display the figure in Streamlit
st.title("Election Results vs. GDP per Capita")
st.plotly_chart(fig)
