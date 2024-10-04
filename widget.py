import streamlit as st
# Working with Widgets
#Buttons /Radio/Checkbox/Select/
# Working with Buttons
name="Priyanshu Raj"
if st.button("Submit"):
    st.write("Name: {}".format(name.upper()))


if st.button("Submit",key='new02'):
  st.write("First Name: {}".format(name.lower()))

  #Working with Radio Button
status=st.radio("What is Your status",("Active","Inactive"))
if status == 'Active':
 st.success("You are active")
elif status == "Inactive" :
 st.warning("Inactive")



 #Working with Checkbox
if st.checkbox("Show/Hide"):
    st.text("Showing something")



#Working with Beta Expander
if  st.expander("Python"):
    st.success("Hello Python")




