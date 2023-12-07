
# import the necessary packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
import seaborn as sns

# set mardown name
st.markdown('# Data Analysis Web App Dashboard: Streamlit')

# reading the data
data = pd.read_csv ('Housing.csv')
data.columns = data.columns.str.upper() # convert the columns to uppercase 

# write a text or comment
st.write( '### 1. Overview of the Data ')
# view the data in streamlit
st.dataframe(data, use_container_width=True)

st.write( '### 2. Understanding the Data ')
# creating radio button
selected = st.radio( "**What do you want to know about the data ?**", ["Description", "Data Sample", "Data Head/Tail","Data Shape"])
# creating sidebar and radio simultaneously
# selected = st.sidebar.radio("**What do you want to know about the data ?**", ["Description", "Data Sample", "Data Head/Tail","Data Shape"])
st.write(selected)

if selected == 'Description':
    st.dataframe(data.describe(), use_container_width=True)   # shows the data basic descriptive
elif selected == 'Data Sample':
    st.dataframe(data.sample(10), use_container_width=True)  #  select random row
elif selected == 'Data Head/Tail':
    st.dataframe(data.head(), use_container_width=True)  # shows the head of the data 
else:
    st.write('###### The shape of the data is :',data.shape)  # check the data shape


st.write( '### 3. Data Visualization ')
############# Option-1 : embed and display the html analysis result already done by the auto-eda libraries(pandasprofile, sweet viz) using streamlit Tabs ###############################

# creating tabs 
tab1, tab2 = st.tabs(["PANDASPROFILE ANALYSIS","SWEETVIZ ANALYSIS"])

with tab1:
#load the saved html files of the auto data analyzed files
		analNG = open("analysis_report_profilereport.html", 'r', encoding='utf-8')
		components.html(analNG.read(), height=8000, width=1000, scrolling=False)
with tab2:
		analNG = open("analysis_with_sweetviz.html", 'r', encoding='utf-8')
		components.html(analNG.read(), height=8000, width=1500, scrolling=False)

################################################################################################################################
# make sure to use either option-1 or option-2 not both as the same time

################ Option-2 : make slight manual data visualization and creat streamlit sidebar & mulit select ###############################

# identifiying the numerical and categorical feature 
numerical_features = data.select_dtypes(exclude= 'object').columns 
categorical_features = data.select_dtypes('object').columns 

# creating mutiselect tab in the left sidebar
graph_options = st.sidebar.multiselect( "SELECT GRAPH TYPE:", options=['HISTOGRAM','COUNT-PLOT','BOX-PLOT'], default=['HISTOGRAM','COUNT-PLOT','BOX-PLOT'])

# creating three columns to display on the streamlit web 
col1,col2,col3 = st.columns(3)
# defining columns to disply in the streamlit
col1.write( '##### Histogram Plot ')
col2.write( '##### Box Plot ')
col3.write( '##### Count Plot')

# if histogram selected show the histo graph for reach numerical feature
if  'HISTOGRAM' in graph_options:
    for feature in numerical_features:
        fig1 = plt.figure()
        sns.histplot(data=data, x=feature, color="black") 
        col1.pyplot(fig1)

# # if box plot selected on the multi select, creat box plot for each categorical features
if  'BOX-PLOT' in graph_options:
    for feature in categorical_features:
        fig2 = plt.figure()
        sns.boxplot( x=feature, y='PRICE',data=data, palette="Set1")
        # sns.catplot( data=data,x=feature, y='PRICE', kind="boxen")
        col2.pyplot(fig2)

# if count plot selected on the mulitselect, create count plot for each categorical features
if  'COUNT-PLOT' in graph_options:
    for feature in categorical_features:
        fig3 = plt.figure()
        sns.countplot(x=feature, data=data, palette="Set3")
        col3.pyplot(fig3)
##############################################################################################
