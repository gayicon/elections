import streamlit as st
import plotly.express as px
import pandas as pd

# Load the election and GDP data
election_data = px.data.election()
gdp_data = px.data.gapminder()

# Check the columns of both datasets (debugging step)
st.write("Election data columns:", election_data.columns)
st.write("GDP data columns:", gdp_data.columns)

# Rename columns to ensure consistency in 'year'
election_data.rename(columns={'Year': 'year'}, inplace=True)  # Rename 'Year' to 'year' in election data
gdp_data.rename(columns={'year': 'year'}, inplace=True)  # Ensure both datasets have a 'year' column

# Ensure that the 'year' columns in both datasets are of type int (for merging)
election_data['year'] = election_data['year'].astype(int)
gdp_data['year'] = gdp_data['year'].astype(int)

# Merge the datasets on the 'year' column (this assumes matching years between the two datasets)
merged_data = pd.merge(election_data, gdp_data, on='year')

# Display the first few rows of the merged data (debugging step)
st.write(merged_data.head())

# Create a scatter plot comparing GDP per capita and votes for each party
fig = px.scatter(
    merged_data,
    x="gdpPercap",  # GDP per capita
    y="votes",  # Votes for the candidate
    color="party",  # Color by party
    hover_name="district",  # Show district name on hover
    title="Election Results vs. GDP per Capita",
    labels={"gdpPercap": "GDP per Capita", "votes": "Votes for Party"}
)

# Display the Plotly figure in Streamlit
st.title("Election Results vs. GDP per Capita")
st.plotly_chart(fig)

# Optional: Show the raw merged data (in case you want to inspect it)
st.write("Merged Data", merged_data)
