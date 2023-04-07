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
    
    # Question 1
    
    if st.checkbox("Q1: Show the number of Confirmed, Deaths, and Recovered cases in each Region"):
           st.write(data.groupby('Region')[['Confirmed', 'Deaths', 'Recovered']].sum())
    # Question 2
    
    if st.checkbox("Q2: Remove all the records where Confirmed Cases is Less Than 10"):
          data = data[~(data.Confirmed < 10)]
          st.write(data)
            
    # Question 3
    
    if st.checkbox("Q3: In which Region, maximum number of Deaths cases were recorded?"):
           st.write(data.groupby('Region')['Confirmed'].sum().sort_values(ascending=False).head(1))
        
    # Question 4
    
    if st.checkbox("Q4: In which Region, minimum number of Deaths cases were recorded?"):
           st.write(data.groupby('Region')['Deaths'].sum().sort_values().head(1))
        
    # Question 5
    
    if st.checkbox("Q5: How many Confirmed, Deaths & Recovered cases were reported from India till 29 April 2020?"):
           india_data = data[data['Region'] == 'India']
           st.write("Confirmed cases:", india_data['Confirmed'].sum())
           st.write("Deaths:", india_data['Deaths'].sum())
           st.write("Recovered:", india_data['Recovered'].sum())
            
    # Question 6-A
    
    if st.checkbox("Q6-A: Sort the entire data wrt No. of Confirmed cases in ascending order"):
           st.write(data.sort_values(by=['Confirmed'], ascending=True))
        
     # Question 6-B  
    
    if st.checkbox("Q6-B: Sort the entire data wrt No. of Recovered cases in descending order"):
           st.write(data.sort_values(by=['Recovered'], ascending=False))


    # Question 7

    if st.checkbox("Q7: Check if the patient is likely to have COVID-19 based on symptoms"):
          # Create checkboxes for symptoms
          fever = st.checkbox("Fever")
          cough = st.checkbox("Dry Cough")
          tiredness = st.checkbox("Tiredness")
          breathing_difficulty = st.checkbox("Difficulty in Breathing")
          sore_throat = st.checkbox("Sore Throat")
          body_aches = st.checkbox("Body Aches")
          loss_of_smell_or_taste = st.checkbox("Loss of Smell or Taste")

    # Check if any of the symptoms are present
          if fever or cough or tiredness or breathing_difficulty or sore_throat or body_aches or loss_of_smell_or_taste:
                st.write("Based on the symptoms, the patient may have COVID-19.")
          else:
                st.write("Based on the symptoms, the patient is unlikely to have COVID-19.")

    # Question 8
    if st.checkbox("Q8: Which Region has the highest number of Confirmed cases?"):
           st.write(data.groupby('Region')['Confirmed'].sum().sort_values(ascending=False).head(1).index[0])

    
        
    # Question 9  
    
    if st.checkbox("Q9: Which region have a death rate of over 10%?"):
           data['Death Rate'] = (data['Deaths'] / data['Confirmed']) * 100
           high_death_rate = data[data['Death Rate'] > 10]['Region']
           st.write(high_death_rate.unique()) 
           
    # Question 10  
           
    if st.checkbox("Q10: Which region have the highest mortality rates (number of deaths / number of confirmed cases)?"):
           #Calculate mortality rate
           data['Mortality_Rate'] = data['Deaths'] / data['Confirmed']
           #Group data by country and sort by mortality rate
           mortality_by_Region = data.groupby('Region')['Mortality_Rate'].max().sort_values(ascending=False)
           st.write(mortality_by_Region)
    
    # Question 11
    if st.checkbox("Q11: Show a bar chart showing the total confirmed cases for each region"):
          region_confirmed = data.groupby("Region")["Confirmed"].sum().reset_index()
          fig, ax = plt.subplots()
          sns.barplot(x="Region", y="Confirmed", data=region_confirmed, ax=ax)
          ax.set_title("Total Confirmed Cases by Region")
          #ax.set_xlabel("Region")
          ax.set_ylabel("Confirmed Cases")
          st.pyplot(fig) 
    
    # Question 12
    if st.checkbox("Q12: Create a line chart showing the trend of Confirmed, Deaths, and Recovered cases over time."):
          data_by_date = data.groupby(['Date'])[['Confirmed', 'Deaths', 'Recovered']].sum()
          st.line_chart(data_by_date)

    
    
    
    
    
    # Question 13

    if st.checkbox("Q13: Show a bar chart of the top 10 Regoins with the highest number of confirmed cases."):
           top10 = data.groupby('Region')['Confirmed'].sum().sort_values(ascending=False).head(10)
           plt.figure(figsize=(12,6))
           plt.title("Top 10 Regions with Highest Number of Confirmed Cases", fontsize=18)
           plt.xlabel("Region", fontsize=14)
           plt.ylabel("Number of Confirmed Cases", fontsize=14)
           sns.barplot(x=top10.index, y=top10.values)
           st.pyplot()
        
    # Question 14

    if st.checkbox("Q14: Show the trend of Confirmed, Deaths, and Recovered cases over time for a selected region"):
           # Create a dropdown menu for region selection
           regions = data['Region'].unique()
           selected_region = st.selectbox("Select a region", regions)
    
           # Filter data for the selected region
           region_data = data[data['Region'] == selected_region]
    
           # Line chart showing the trend of Confirmed, Deaths, and Recovered cases over time
           fig, ax = plt.subplots(figsize=(12, 8))
           ax.plot(region_data['Date'], region_data['Confirmed'], label='Confirmed')
           ax.plot(region_data['Date'], region_data['Deaths'], label='Deaths')
           ax.plot(region_data['Date'], region_data['Recovered'], label='Recovered')
           ax.set_xlabel('Date')
           ax.set_ylabel('Number of Cases')
           ax.set_title(f"{selected_region} COVID-19 Cases")
           ax.legend()
           st.pyplot(fig)
    # Question 15
    if st.checkbox("Q15: How has the distribution of COVID-19 cases changed over time in different regions? Can you show this on a heatmap?"):   
 

           # Pivot the data to get the number of confirmed cases by region and date
           pivot_data = data.pivot('region', 'date', 'confirmed')

           # Create the heatmap
           sns.heatmap(pivot_data, cmap='YlOrRd')

           # Set the plot title and axis labels
           plt.title('Number of Confirmed Cases by Region and Date')
           plt.xlabel('Date')
           plt.ylabel('Region')

           # Show the plot
           plt.show()



