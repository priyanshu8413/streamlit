import streamlit as st

#Text Input
fname = st.text_input("Enter First name",max_chars=10)
#Text input Hide Password
password =st.text_input("Enter Password",type='password')
st.title(fname)


#Text Area
message = st.text_area("Enter Message",height=100)
st.write(message)


#numbers
number = st.number_input("Enter Number",1.0,25.0)

#date Input

myappointment = st.date_input("Appointment")

#time input
mytime= st.time_input("My Time")


#color picker
color=st.color_picker("Select Color")