import streamlit as st
import plotly.express as px
import pandas as pd

# Load the election and GDP data
election_data = px.data.election()
gdp_data = px.data.gapminder()

# Check the columns of both datasets (debugging step)
st.write("Election data columns:", election_data.columns)
st.write("GDP data columns:", gdp_data.columns)

# Check the first few rows of the election data (debugging step)
st.write("Election data sample:", election_data.head())

# Check for the 'year' column or rename if necessary
if 'Year' in election_data.columns:
    election_data.rename(columns={'Year': 'year'}, inplace=True)
elif 'ElectionYear' in election_data.columns:
    election_data.rename(columns={'ElectionYear': 'year'}, inplace=True)

# Verify if 'year' column exists now
st.write("Election data columns after renaming:", election_data.columns)

# Ensure 'year' columns in both datasets are of type int (for merging)
if 'year' in election_data.columns:
    election_data['year'] = election_data['year'].astype(int)
    gdp_data['year'] = gdp_data['year'].astype(int)
else:
    st.write("Error: 'year' column not found in election data!")

# Proceed with the merge if 'year' is present
if 'year' in election_data.columns:
    # Merge the datasets on the 'year' column
    merged_data = pd.merge(election_data, gdp_data, on='year')

    # Display the first few rows of the merged data
    st.write("Merged Data:", merged_data.head())

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
else:
    st.write("The 'year' column is not present in the election data.")
