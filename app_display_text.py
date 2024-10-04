import streamlit as st
import pandas as pd

#display data
df=pd.read_csv("iris.csv")
#  Method 1
#st.dataframe(df,200,100)

#adding A color style from pandas
#st.dataframe(df.style.highlight_max(axis=0))


#method 2 :Static Table
#st.table(df)

#method 3 :Using superfxn st.write
st.write(df.head())

#display json
st.json({'data':'name'})

#Display Code
mycode="""
def sayhello():
print("Hello Streamlit Lovers)
"""


st.code(mycode,language='ruby')