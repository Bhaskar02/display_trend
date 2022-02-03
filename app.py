import streamlit as st
from streamlit.elements.image import image_to_url, MAXIMUM_CONTENT_WIDTH
from PIL import Image

option = st.selectbox('Select the year',('2010', '2011', '2012','2013','2014','2015','2016'))

img = 'https://raw.githubusercontent.com/Bhaskar02/display_trend/main/images/'+option+'.png'
img1 = 'https://raw.githubusercontent.com/Bhaskar02/display_trend/main/lineplot/'+option+'.png'
st.image(img, caption='corelation '+option,width=400,use_column_width=400)
st.image(img1, caption='line'+option,width=400,use_column_width=400)
