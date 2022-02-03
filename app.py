import streamlit as st
from streamlit.elements.image import image_to_url, MAXIMUM_CONTENT_WIDTH
from PIL import Image
import webbrowser
option = st.selectbox('Select the year',('2010', '2011', '2012','2013','2014','2015','2016','2017','2018'))
col1, col2 = st.columns(2)
img = 'https://raw.githubusercontent.com/Bhaskar02/display_trend/main/images/'+option+'.png'
img1 = 'https://raw.githubusercontent.com/Bhaskar02/display_trend/main/lineplot/'+option+'.png'
#st.image(img, caption='corelation '+option,width=400,use_column_width=400)
col1.image(img, caption='corelation '+option, width=450,use_column_width=450)
#st.image(img1, caption='line'+option,width=400,use_column_width=400)
col2.image(img1, caption='line  '+option, width=450,use_column_width=450)


url = 'https://share.streamlit.io/bhaskar02/display_trend/main/app2.py'

if st.button('home'):
    webbrowser.open_new(url)
