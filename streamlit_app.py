import pandas as pd
import streamlit as st
#add a title to the web app
st.title("Automobile Data Dashboard")
#data overview
df= pd.read_csv("Automobile_data.csv")
st.write("Here is the dataset:")
df
