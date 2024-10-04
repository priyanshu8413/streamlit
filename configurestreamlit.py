import streamlit as st
from PIL import Image
img=Image.open("—Pngtree—creative company_1420804.png")
#must be the first activity of streamlit
#method 2:Dictionary
PAGE_CONFIG={"page_title":"Priyanshu","page_icon":":smiley","layout":"centered"}
st.set_page_config(**PAGE_CONFIG)
#st.set_page_config(page_title='hello',
                  # page_icon=img,layout='wide',initial_sidebar_state='auto')



def main():
    st.title("Hello streamlit Lovers ❤️")
    st.sidebar.success("Menu")



if __name__ == '__main__':
    main()


