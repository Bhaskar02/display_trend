import streamlit as st
from streamlit.elements.image import image_to_url, MAXIMUM_CONTENT_WIDTH
from PIL import Image
import webbrowser
import click
import streamlit.components.v1 as components

option = st.selectbox('Select the year',('2010', '2011', '2012','2013','2014','2015','2016','2017','2018'))
col1, col2 = st.columns(2)
img = 'https://raw.githubusercontent.com/Bhaskar02/display_trend/main/images/'+option+'.png'
img1 = 'https://raw.githubusercontent.com/Bhaskar02/display_trend/main/lineplot/'+option+'.png'
#st.image(img, caption='corelation '+option,width=400,use_column_width=400)
col1.image(img, caption='corelation '+option, width=400,use_column_width=480)
#st.image(img1, caption='line'+option,width=400,use_column_width=400)
col2.image(img1, caption='line  '+option, width=400,use_column_width=480)


url = 'https://share.streamlit.io/bhaskar02/display_trend/main/app2.py'

link = '[Home](https://sites.google.com/view/iitkgpicps/home?authuser=2)'
st.markdown(link, unsafe_allow_html=True)
    
