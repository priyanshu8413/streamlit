import streamlit as st

#Working Media Files(Videos/images/audio)
from PIL import Image
img = Image.open("image_01.jpg")
st.image(img,use_column_width=True)


# From URL
st.image("https://images.pexels.com/photos/1580271/pexels-photo-1580271.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1","rb")


# Dispay video
video_file = open("secret_of_success.mp4","rb").read()
st.video(video_file,start_time=3)

#Display Audio /Working with Audio

audio_file=open("song.mp3","rb")
st.audio(audio_file.read())
