import streamlit as st
from streamlit.elements.image import image_to_url, MAXIMUM_CONTENT_WIDTH
from PIL import Image

option = st.selectbox('Select the year',('2010', '2011', '2012','2013','2014','2015','2016'))

img = 'https://raw.githubusercontent.com/Bhaskar02/dengueapp/main/data/images/2010.PNG'
st.image(img, caption='corelation '+option,width=500,use_column_width=500)
