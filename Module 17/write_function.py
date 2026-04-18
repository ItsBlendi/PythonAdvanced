import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'Name': ["Alice", "Bob", "Charlie"],
    'Age':[24,27,22],
    'City':["Podujev","Prishtin","Drenas"]
})

st.write(df)