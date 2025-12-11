import streamlit as st
import pandas as pd
import duckdb

st.write("""
# SQL SRS
Spaced Repetition System SQL practice
""")

option = st.selectbox(
    "What would you like to review?",
    ["Joins", "GroupBy", "Windows Functions"],
    placeholder="Select a theme..."
)

st.write("You selected:", option)

data = {"a": [1,2,3], "b": [4,5,6], "c": [7,8,9]}
df = pd.DataFrame(data)



st.header("SQL TRAINING")
query = st.text_area("Faire une query interogeant la table 'df'")

st.write(f"Vous avez rentré la query suivante {query}")

st.dataframe(duckdb.sql(query))
