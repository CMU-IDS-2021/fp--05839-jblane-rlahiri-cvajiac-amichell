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
#import awesome_streamlit as ast
#import home
#import interface
#import src.style
st.set_page_config(layout="wide")
#st.set_page_config(layout="wide")
#ast.core.services.other.set_logging_format()

#PAGES = {
#    "Home": home,
#    "Main Interface": interface,
    #"Interface": src.resources,

#}


class home1:
    from datetime import date

#def local_css(file_name):
#    with open(file_name) as f:
#        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

#local_css("style1.css")

    

#logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)


    def write(self):
	    page_bg_img = '''
	    <style>
	    body 	{
    		    color: #fff;
    		    background-color: #4F8BF9;
		    }

	    .stButton>button {
		    color: #4F8BF9;
		    border-radius: 50%;
    		    height: 3em;
    		    width: 3em;
		    }

	    .stTextInput>div>div>input {
   		     color: #4F8BF9;
		    }
	    </style>
	    '''
	    st.markdown(page_bg_img, unsafe_allow_html=True)
	    with open('./style.css') as f:
    	    	st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


	    st.title("⭐A Better Spark Interface⭐")
	    st.markdown("**Why Do We Need a Better Spark UI?**")#
	    st.markdown("---")
	    st.markdown("***First, WHAT IS SPARK?!***" )
	    components.html(
    	    """
    	    <!DOCTYPE html>
    	    <html>
    	    <head>
    	    <meta name="viewport" content="width=device-width, initial-scale=1">
    	    <style>
    	    .container {
     	    position: relative;
      	    width: 30%;
    	    }
    
    	    .image {
      	    display: block;
      	    width: 100%;
      	    height: auto;
    	    }
    	    </style>
    	    </head>
            
    	    <body>

    	    <div class="container">
            <p style="text-align:center">
      	    <img src="https://spark.apache.org/images/spark-logo-trademark.png" alt="Current Spark Results" class="image" >
            </p>
    	    </div>
            <p style="font-size:18px;font-family:verdana">Originated at UC Berkeley in 2009, Apache Spark is a unified analytics 
            engine for big data processing. It includes support for SQL queries, streaming 
            data, machine learning, and graph processing. Spark runs on Hadoop, Apache Mesos, 
            Kubernetes, standalone, or in the cloud. Internet companies such as 
            Netflix, Yahoo, and eBay have deployed Spark at massive scale, collectively 
            processing multiple petabytes of data on clusters of over 8,000 nodes.</p>
    	    
            </body>

    	    </html>
    	    """,
    	    height=300
    	    )

	    st.markdown("---")
	    st.markdown("***How Does it Work?***" )
	    
        # components.html(
    	   #  """
          
    	   #  <!DOCTYPE html>
    	   #  <html>
    	   #  <head>
    	   #  <meta name="viewport" content="width=device-width, initial-scale=1">
    	   #  <style>
    	   #  .container {
     	  #   position: relative;
      	 #    width: 30%;
    	   #  }
    
    	   #  .image {
      	 #    display: block;
      	 #    width: 100%;
      	 #    height: auto;
    	   #  }
    	   #  </style>
    	   #  </head>
    	   #  <body>
    
    	   #  <!--<h2>Current Results View</h2>-->
    	   #  <!--<p>Hover over the image to see the effect.</p>-->

    	   #  <div class="container">
      	 #    <img src="https://spark.apache.org/images/spark-logo-trademark.png" alt="Current Spark Results" class="image" >
    	   #  </div>

    	   #  </body>
    	   #  </html>
    	   #  """,
    	   #  height=200
            
    	   #  )
        
	    st.markdown("""_Magic. Lots of it._""")




	    st.markdown("---")
	    st.markdown("***So What's the Problem?***" )
	    st.markdown("_Here's what Spark results look like now:_" )
	    components.html(
    	    """
    	    <!DOCTYPE html>
    	    <html>
    	    <head>
    	    <meta name="viewport" content="width=device-width, initial-scale=1">
    	    <style>
    	    .container {
      	    position: relative;
      	    width: 50%;
    	    }
    
    	    .image {
      	    display: block;
      	    width: 200%;
      	    height: auto;
    	    }
    
    	    .overlay {
      	    position: absolute;
      	    top: 0;
      	    bottom: 0;
      	    left: 0;
      	    right: 0;
      	    height: 100%;
      	    width: 200%;
      	    opacity: 0;
      	    transition: .5s ease;
      	    background-color: lightblue;
    	    }
    
    	    .container:hover .overlay {
      	    opacity: 1;
    	    }
    
    	    .text {
      	    color: white;
      	    font-size: 30px;
      	    position: absolute;
      	    top: 50%;
      	    left: 50%;
      	    -webkit-transform: translate(-50%, -50%);
      	    -ms-transform: translate(-50%, -50%);
      	    transform: translate(-50%, -50%);
      	    text-align: center;
    	    }
    	    </style>
    	    </head>
    	    <body>
    
    	    <!--<h2>Current Results View</h2>-->
    	    <!--<p>Hover over the image to see the effect.</p>-->
    
    	    <div class="container">
      	    <img src="https://github.com/CMU-IDS-2021/fp--05839-jblane-rlahiri-cvajiac-amichell/blob/main/job_example.png?raw=true" alt="Current Spark Results" class="image" >
      	    <div class="overlay">
            <div class="text">Some useful stuff, but how to make sense of it?!</div>
      	    </div>
    	    </div>
            
            <p style="font-size:18px;font-family:verdana">This UI displays some information, such as the job duration, stages, and a progress bar.
                However, all the information is displayed in tabular format and we don’t see a lot of other useful information,
                such as memory usage or shuffle read/writes. While this information is available, it is not presented with
                effective visual encodings that identify clearly the implication of different characteristics of Spark jobs.
                Furthermore, once the end user has hundreds or thousands of jobs, these tables become impossible to parse.</p>
                
    	    </body>
    	    </html>
    	    """,
    	    height=800
    	    )



class interface:
    
    def write(self):
        with open('./interfacestyle.css') as f:
              st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
		
        source = data.movies.url
	    #st.set_page_config(layout="wide")
        st.title("A Better Spark User Interface")
        st.markdown("""
 	    * Use the menu at left to select data and set plot parameters
 	    * Your plots will appear below
	    """)

        st.sidebar.markdown("## Select Optimization")
	    #set_png_as_page_bg('apache-spark1.jpg')

	    #st.sidebar.markdown('#### Q-tranform plot')
	    #vmax = st.sidebar.slider('Colorbar Max Energy', 10, 500, 25)  # min, max, default
	    #qcenter = st.sidebar.slider('Data', 5, 120, 5)  # min, max, default
	    #qrange = (int(qcenter*0.8), int(qcenter*1.2))
        task = st.selectbox(
        	    "Which problem do you want to Visualize?", ["Word Count","Spark for ML","Apply Optimizations to an Extract, Transform, Load (ETL) job"])
        plot=alt.Chart(source).mark_bar().encode(
    	    alt.X("IMDB_Rating:Q"),
    	    y='count()',
    
	    ).properties(width=400,
    	    height=200)
        data_spill_button=st.sidebar.radio("Show data spill to memory and disk",("Yes","No"))

        suffle_read_button=st.sidebar.radio("Show shuffle read and write quantities",("Yes","No"))
        Dataio_button=st.sidebar.radio("Show data input and output",("Yes","No"))
	    #row2_1, row2_2, row2_3, row2_4 = st.beta_columns((2,1,1,1))
        st.write("** Please select a checkbox to implement one or more optimization**")
        if st.checkbox("Optimization 1"):
    		    #TODO
                st.write("Implement Optimization 1 on Data Set")
    
        if st.checkbox("Optimization 2"):
    		    #TODO
                st.write("Implement Optimization 2 on Data Set")
    
        if st.checkbox("Optimization 3"):
    		    #TODO 
                st.write("Implement Optimization 3 on Data Set")
      
        col1, col2, col3 = st.beta_columns(3)
        if data_spill_button=="Yes":
                col1.header("Data Spill to Memory and Disk")
                col1.write(plot)
    		    #row2_1, row2_2, row2_3 = st.beta_columns((2,1,1))

        if suffle_read_button=="Yes":
                col2.header("Shuffle Read and Write")
                col2.write(plot)
        if Dataio_button=="Yes":
                col3.header("Data input and output")
                col3.write(plot)
        st.write("** Display Data after Optimizations**")
        optimized=st.radio("",("Yes","No"))
        if optimized=="Yes":
                st.write(plot.properties(width=600,height=300))



def main():
    """Main function of the App"""
    st.sidebar.title("Navigation")
    #selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    nav_button=st.sidebar.radio("Go to",("Home","Main Interface"))

    if nav_button=="Home":
        home1().write()
        
    if nav_button=="Main Interface":
        interface().write()
    #interface=st.sidebar.radio()
    #page = PAGES[selection]
    #st.write("hello")
    #with st.spinner(f"Loading {selection} ..."):
    #    ast.shared.components.write_page(page)
    #    #st.write(page)
   
    st.sidebar.title("About")
    st.sidebar.info(
        """
        This app is maintained by\n
        Janice Blane, mailto:jblane@andrew.cmu.edu \n
        Riddhiman Lahiri, (mailto:rlahiri@andrew.cmu.edu) \n
        André Michell, (mailto:amichell@andrew.cmu.edu) \n
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
#    #TODO
#    st.write("Implement Optimization 1 on Data Set")
    
#if st.checkbox("Optimization 2"):
    #TODO
#    st.write("Implement Optimization 2 on Data Set")
    
    
#if st.checkbox("Optimization 3"):
#    #TODO 
#    st.write("Implement Optimization 3 on Data Set")
#col1, col2, col3 = st.beta_columns(3)
#if data_spill_button=="Yes":
#    col1.header("Data Spill to Memory and Disk")
#    col1.write(plot)
#    #row2_1, row2_2, row2_3 = st.beta_columns((2,1,1))

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
