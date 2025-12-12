# pylint: disable=missing-module-docstring

import io

import duckdb
import pandas as pd
import streamlit as st

# ----- Initialisation bdd ----- #
CSV = """
beverage,price
orange juice,2.5
Expresso,2
Tea,3
"""

CSV2 = """
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3
"""

beverages = pd.read_csv(io.StringIO(CSV))
food_items = pd.read_csv(io.StringIO(CSV2))

ANSWER = """
SELECT * FROM beverages
CROSS JOIN food_items
"""

solution_df = duckdb.sql(ANSWER).df()


def query_handle():
    """
    Check if the SQL query is valid (if invalid return) \n
    Display the result \n
    Check if the result is == to the solution
    """
    if query:  # Check query
        try:
            duckdb.sql(query)
        except (duckdb.ParserException, duckdb.BinderException):
            st.write("Erreur dans la query")
            return
    result = duckdb.sql(query)

    # Display Query
    st.dataframe(result)

    if result:
        result_df = duckdb.sql(query).df()

        n_lines_difference = solution_df.shape[0] - result.shape[0]  # Check lines
        if n_lines_difference != 0:
            st.write(f"{n_lines_difference} lines missing")

        try:  # Check columns
            result_df = result_df[solution_df.columns]
            st.dataframe(
                result_df.compare(solution_df, result_names=("result", "expected"))
            )
        except KeyError:
            st.write("Some columns are missing")


# ----- Mise en page ----- #

# Title
st.write(
    """
# SQL SRS
Spaced Repetition System SQL practice
"""
)

# Select Box
with st.sidebar:
    option = st.selectbox(
        "What would you like to review?",
        ["Joins", "GroupBy", "Windows Functions"],
        placeholder="Select a theme...",
    )
    st.write("You selected:", option)

# SQL_prompt
st.header("enter your code:")
query = st.text_area("votre code SQL ici", key="user_input")
st.write("You entered:", query)


# Handle query (Check query, Display, Compare it to solution)
query_handle()


# Resources Display
tab1, tab2 = st.tabs(["Tables", "Solution"])

with tab1:
    st.write("table: beverages")
    st.dataframe(beverages)
    st.write("table: food_items")
    st.dataframe(food_items)
    st.write("expected:")
    st.dataframe(solution_df)

with tab2:
    st.write(ANSWER)
