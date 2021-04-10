#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 10:30:52 2021

@author: jblane
"""

import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import altair as alt
from datetime import date
import collections
import base64
from vega_datasets import data
import awesome_streamlit as ast
#import home
#import interface
#import src.style
#st.set_page_config(layout="wide")
#st.set_page_config(layout="wide")
#ast.core.services.other.set_logging_format()

#PAGES = {
#    "Home": home,
#    "Main Interface": interface,
    #"Interface": src.resources,

#}
def main():
    """Main function of the App"""
    st.sidebar.title("Navigation")
    #selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    #page = PAGES[selection]
    
    #with st.spinner(f"Loading {selection} ..."):
    #    ast.shared.components.write_page(page)
    
   
    st.sidebar.title("About")
    st.sidebar.info(
        """
        This app is maintained by  Janice Blane, mailto:jblane@andrew.cmu.edu
        Riddhiman Lahiri, (mailto:rlahiri@andrew.cmu.edu)
        André Michell, (mailto:amichell@andrew.cmu.edu)
        Catalina Vajiac, (mailto:cvajiac@andrew.cmu.edu)
        """
    )


if __name__ == "__main__":
    main()









#source = data.movies.url
#st.set_page_config(layout="wide")
#def local_css(file_name):
#    with open(file_name) as f:
#        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

#local_css("style.css")

#st.title("⭐Towards a Better Spark UI⭐")
#st.text("An Interactive Visualization")
#page_bg_img = '''
#<style>
#body {
#background-image: url("https://spark.apache.org/images/spark-logo-back.png");
#background-size: cover;
#}
#</style>
#'''

#st.markdown(page_bg_img, unsafe_allow_html=True)




#components.html(
#    """
#    <!DOCTYPE html>
#    <html>
#    <head>
#    <meta name="viewport" content="width=device-width, initial-scale=1">
#    <style>
#    .container {
#      position: relative;
#      width: 50%;
#    }
    
#    .image {
#      display: block;
#      width: 100%;
#      height: auto;
#    }
#    </style>
#    </head>
#    <body>
    
#    <!--<h2>Current Results View</h2>-->
#    <!--<p>Hover over the image to see the effect.</p>-->
    
#    <div class="container">
#      <img src="https://spark.apache.org/images/spark-logo-trademark.png" alt="Current Spark Results" class="image" >
#    </div>
    
#    </body>
#    </html>
#    """,
#    height=100
#    )

#st.set_page_config(layout="wide")



#st.markdown("""
# * Use the menu at left to select data and set plot parameters
# * Your plots will appear below
#""")


#st.sidebar.markdown("## Select Optimization")
#set_png_as_page_bg('apache-spark1.jpg')

#st.sidebar.markdown('#### Q-tranform plot')
#vmax = st.sidebar.slider('Colorbar Max Energy', 10, 500, 25)  # min, max, default
#qcenter = st.sidebar.slider('Data', 5, 120, 5)  # min, max, default
#qrange = (int(qcenter*0.8), int(qcenter*1.2))


#@st.cache(allow_output_mutation=True)
#def get_base64_of_bin_file(bin_file):
#    with open(bin_file, 'rb') as f:
#        data = f.read()
#    return base64.b64encode(data).decode()
#def set_png_as_page_bg(png_file):
#    bin_str = get_base64_of_bin_file(png_file)
#    page_bg_img = '''
#    <style>
#    body {
#    background-image: url("data:image/jpg;base64,%s");
#    background-size: cover;
#    opacity: 1;
#    }
#    </style>
#    ''' % bin_str
    
#    st.markdown(page_bg_img, unsafe_allow_html=True)
#    return
#set_png_as_page_bg('apache-spark1.jpg')
#task = st.selectbox(
#        "Which problem do you want to Visualize?", ["Word Count","Spark for ML","Apply Optimizations to an Extract, Transform, Load (ETL) job"])
#plot=alt.Chart(source).mark_bar().encode(
#    alt.X("IMDB_Rating:Q"),
#    y='count()',
    
#).properties(width=400,
#    height=200)
#data_spill_button=st.sidebar.radio("Show data spill to memory and disk",("Yes","No"))

#suffle_read_button=st.sidebar.radio("Show shuffle read and write quantities",("Yes","No"))

#Dataio_button=st.sidebar.radio("Show data input and output",("Yes","No"))

#if st.checkbox("Optimization 1"):
    #TODO
#    st.write("Implement Optimization 1 on Data Set")
    
#if st.checkbox("Optimization 2"):
    #TODO
#    st.write("Implement Optimization 2 on Data Set")
    
    
#if st.checkbox("Optimization 3"):
    #TODO 
#    st.write("Implement Optimization 3 on Data Set")
#col1, col2, col3 = st.beta_columns(3)
#if data_spill_button=="Yes":
#    col1.header("Data Spill to Memory and Disk")
#    col1.write(plot)
    #row2_1, row2_2, row2_3 = st.beta_columns((2,1,1))

#if suffle_read_button=="Yes":
#    col2.header("Shuffle Read and Write")
#    col2.write(plot)
#if Dataio_button=="Yes":
#    col3.header("Data input and output")
#    col3.write(plot)
#st.write("** Display Data after Optimizations**")
#optimized=st.radio("",("Yes","No"))
#if optimized=="Yes":
#    st.write(plot.properties(width=600,height=300))
