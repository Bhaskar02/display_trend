import datetime
from glob import glob
import numpy as np
import folium
from folium import plugins
from folium.plugins import HeatMap
import pandas as pd
import streamlit as st
import leafmap.foliumap as leafmap
from PIL import Image

option = st.selectbox('Select the year',('2010', '2011', '2012','2013','2014','2015','2016'))
#a = Image.open('https://github.com/Bhaskar02/dengueapp/blob/main/data/images/2011.png')

st.image('https://github.com/Bhaskar02/dengueapp/blob/main/data/images/2011.png', caption='corelation '+option,width=500,use_column_width=500)
#images = ['output/2010.png', 'output/2011.png', 'output/2012.png']
#st.image(images, use_column_width=True, caption=["some generic text"] * len(images))
