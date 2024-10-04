# load EDA pkg
import streamlit as st
import pandas as pd
import numpy as np
# Load Data vis pkg
import plotly.express as px



def main():
    st.title("Plotting In Streamlit with Plotly")
    df=pd.read_csv("prog_languages_data.csv")
    st.dataframe(df)

    fig = px.pie(df,values='Sum',names='lang',title='Pie Chart')
    st.plotly_chart(fig)

    fig2=px.bar(df,x='lang',y='Sum')
    st.plotly_chart(fig2)



if __name__=='__main__':
    main()