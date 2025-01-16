import streamlit as st
import pandas as pd

def main():
    st.title("Streamlit Forms &  Salary Calculator")
    menu=["Home","About"]
    choice=st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        st.subheader("Forms Tutorial")
        #Salary Calculator
        #combine forms +column
        with st.form("Forms Tutorial"):
            col1,col2,col3=st.columns([3,2,1])
            with col1:
                amount=st.number_input("Hourly rate in $")
            with col2:
                hour_per_week = st.number_input("Hours per Week", 1,120)
            with col3:
                st.text("Salary")
                submit_salary=st.form_submit_button(label='Calculate')
        if submit_salary:
         with st.expander("Results"):
            daily = [amount*8]
            weekly=[amount * hour_per_week]
            df=pd.DataFrame({'hourly':amount,'daily':daily,'weekly':weekly})
            st.dataframe(df.T)


        # Method 1 :Context  Manager Approach (with)

        with st.form(key='form1'):
            firstname = st.text_input("Firstname")
            lastname=st.text_input("Lastname")
            dob=st.date_input("Date Of Birth")
            submit_button = st.form_submit_button(label='signup')
        #Result can either form or outside
        if submit_button:
           st.success("Hello {} you  have created an account".format(firstname))
        #method 2
        form2=st.form(key='form2')
        username = form2.text_input("Username")
        jobtype = form2.selectbox("job",["Dev","Data Scientist","doctor"])
        submit_button2 = form2.form_submit_button("Login")

        if submit_button2:
           st.write(username.upper())
    else:
        st.subheader("About")









if __name__=='__main__':
    main()