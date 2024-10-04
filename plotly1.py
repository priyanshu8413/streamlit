import streamlit as st
import pandas as pd
import numpy as np

# Load Data vis pkg
import myplot.express as px

def main():
    st.title("Plotting In Streamlit with Plotly")
    df = pd.read_csv("prog_languages_data.csv")
    st.dataframe(df)

    fig = px.pie(df, value='sum', names='lang', title='Pie Chart of Languages')
    st.plotly_chart(fig)

if __name__ == '__main__':
    main()