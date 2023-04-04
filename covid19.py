import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import random
from PIL import Image
logo = Image.open('logo.png')
#pip install pandas numpy matplotlib seaborn streamlit
#to run streamlit :   streamlit run netflix.py 
st.set_page_config(page_title="COVID-19  EDA", page_icon=":bar_chart:", layout="wide")
st.image(logo)
# Define the list of names
names = ["21A21A6145-P.Sushmitha Devi", "21A21A6127-K.Bharathi ", "21A21A6142-P.Madhu Sai","21A21A6148-P.Shiva Mukesh","21A21A6144-P.Sneha Anitha","21A21A6136-M.L.S.Tejas","22A25A6102(L2)-D.R.Vara Prasad"]
st.title("Exploratory Data Analysis on COVID-19 Data Set")
# Add the names to the sidebar
st.sidebar.title("Project Team Members:")

for name in names:
    st.sidebar.write(name)
st.sidebar.title("Under The Guidance of :")
st.sidebar.write("Dr.Bomma.Ramakrishna")
# File upload
uploaded_file = st.file_uploader("Choose a COVID-19 Dataset csv")
if uploaded_file is not None:
    data=pd.read_csv(uploaded_file)
    st.dataframe(data)

    st.title("COVID-19 Data Analysis")

    # Checkboxes for questions
    q1 = st.sidebar.checkbox("Q1: Show the number of Confirmed, Deaths, and Recovered cases in each Region")
    q2 = st.sidebar.checkbox("Q2: Remove all the records where Confirmed Cases is Less Than 10")
    q3 = st.sidebar.checkbox("Q3: In which Region, maximum number of Confirmed cases were recorded?")
    q4 = st.sidebar.checkbox("Q4: In which Region, minimum number of Deaths cases were recorded?")
    q5 = st.sidebar.checkbox("Q5: How many Confirmed, Deaths & Recovered cases were reported from India till 29 April 2020?")
    q6a = st.sidebar.checkbox("Q6-A: Sort the entire data wrt No. of Confirmed cases in ascending order")
    q6b = st.sidebar.checkbox("Q6-B: Sort the entire data wrt No. of Recovered cases in descending order")

    # Question 1
    if q1:
        st.subheader("Q1: Show the number of Confirmed, Deaths, and Recovered cases in each Region")
        st.write(data.groupby('Region')['Confirmed', 'Deaths', 'Recovered'].sum())

    # Question 2
    if q2:
        st.subheader("Q2: Remove all the records where Confirmed Cases is Less Than 10")
        data = data[~(data.Confirmed < 10)]
        st.write(data)

    # Question 3
    if q3:
        st.subheader("Q3: In which Region, maximum number of Confirmed cases were recorded?")
        st.write(data.groupby('Region')['Confirmed'].sum().sort_values(ascending=False).head(1))

    # Question 4
    if q4:
        st.subheader("Q4: In which Region, minimum number of Deaths cases were recorded?")
        st.write(data.groupby('Region')['Deaths'].sum().sort_values().head(1))

    # Question 5
    if q5:
        st.subheader("Q5: How many Confirmed, Deaths & Recovered cases were reported from India till 29 April 2020?")
        india_data = data[data['Region'] == 'India']
        st.write("Confirmed cases:", india_data['Confirmed'].sum())
        st.write("Deaths:", india_data['Deaths'].sum())
        st.write("Recovered:", india_data['Recovered'].sum())

    # Question 6-A
    if q6a:
        st.subheader("Q6-A: Sort the entire data wrt No. of Confirmed cases in ascending order")
        st.write(data.sort_values(by=['Confirmed'], ascending=True))

    # Question 6-B
    if q6b:
        st.subheader("Q6-B: Sort the entire data wrt No. of Recovered cases in descending order")
        st.write(data.sort_values(by=['Recovered'], ascending=False))
