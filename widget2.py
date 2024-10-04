import streamlit as st

# Select /Multiple Select
my_lang=["Python","Julia","Go","Rust"]

choice = st.selectbox("Language",my_lang)
st.write("You selected {}".format(choice))

#multiple Selection
spoken_lang = ("English","French","Spanish","Twi")
my_spoken_lang = st.multiselect("spoken lang",spoken_lang,default="English")



#slider
#Number (Int/Float/Dates)
age = st.slider("Age",1,100)

#Any Datatype
#Select Slider
color= st.select_slider("Choose Color",options=["Yellow","red","blue","Black"],value=("yellow","Red"))