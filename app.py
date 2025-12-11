import streamlit as st
import pandas as pd
import duckdb
import io

# ----- Initialisation bdd ----- #
csv = '''
beverage,price
orange juice,2.5
Expresso,2
Tea,3
'''

csv2 = '''
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3
'''

beverages = pd.read_csv(io.StringIO(csv))
food_items = pd.read_csv(io.StringIO(csv2))

answer = '''
SELECT * FROM beverages
CROSS JOIN food_items
'''

solution = duckdb.sql(answer)

# ----- Mise en page ----- #

# Title
st.write("""
# SQL SRS
Spaced Repetition System SQL practice
""")

# Select Box
with st.sidebar:
    option = st.selectbox(
        "What would you like to review?",
        ["Joins", "GroupBy", "Windows Functions"],
        placeholder="Select a theme..."
    )
    st.write("You selected:", option)

# SQL_prompt
st.header("enter your code:")
query = st.text_area("votre code SQL ici", key="user_input")
st.write("You entered:", query)

# Result Display
st.dataframe(duckdb.sql(query))

# Resources Display
tab1, tab2 = st.tabs(["Tables", "Solution"])

with tab1:
    st.write("table: beverages")
    st.dataframe(beverages)
    st.write("table: food_items")
    st.dataframe(food_items)
    st.write("expected:")
    st.dataframe(solution)

with tab2:
    st.write(answer)
