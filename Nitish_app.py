import streamlit as st 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objs as go
import time
import plotly.express as px


st.set_page_config(page_title="Nitish (922)",page_icon=":bar_chart:", layout="centered")


st.title("Customer Data Analysis")

df= pd.read_excel("Customers.xlsx")

categorical = df.dtypes[df.dtypes == "object"]
categorical = df.dtypes[df.dtypes == "object"].index
df[categorical].describe() # categorical variables
df['Profession'].isnull().sum()
df[df['Profession'].isnull()]


tab1, tab2, tab3 = st.tabs(["Bar graph", "Box plot","Heatmap"])

with tab1:
    
    z=plt.figure(figsize=(10,6))
    ax=df["Gender"].value_counts().plot(kind="bar", color=["tab:blue", "tab:orange"])
    plt.xticks(rotation=0, fontsize=12)
    plt.yticks(fontsize=12)
    ax.bar_label(ax.containers[0], label_type='edge') 
    st.pyplot(z)
 
    w=plt.figure(figsize=(22,6))
    ax=df["Profession"].value_counts().plot(kind="bar")
    plt.xticks(rotation=0, fontsize=12)
    plt.yticks(fontsize=12)
    ax.bar_label(ax.containers[0], label_type='edge')
    st.pyplot(w)



with tab2:
    # plot 1
    st.write("Box Plot Of Age,Annual Income & Spending Score")
    fig, (ax1,ax2,ax3) = plt.subplots(1,3,figsize=(22, 6))
    sns.boxplot(x=df['Age'], ax=ax1)
    sns.boxplot(x=df['Annual Income ($)'], ax=ax2)
    sns.boxplot(x=df['Spending Score (1-100)'], ax=ax3)
    st.pyplot(fig)

  
with tab3:
    plt.figure(figsize=(6,5))
    x=sns.heatmap(df.corr())
    st.pyplot(x.figure)
 
