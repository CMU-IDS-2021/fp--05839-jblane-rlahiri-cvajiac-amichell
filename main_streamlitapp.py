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
import nx_altair
import draw, utils
#import awesome_streamlit as ast
#import home
#import interface
#import src.style
st.set_page_config(layout="wide")
#st.set_page_config(layout="wide")
#ast.core.services.other.set_logging_format()

#PAGES = {
#	"Home": home,
#	"Main Interface": interface,
	#"Interface": src.resources,

#}


class home1:
    from datetime import date

#def local_css(file_name):
#	with open(file_name) as f:
#		st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

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


        st.title("⭐A Better Spark User Interface⭐")
        st.markdown("---")
        st.markdown("***First, WHAT IS APACHE SPARK?!***" )
        components.html(
			"""
			<!DOCTYPE html>
			<html>
			<head>
			<meta name="viewport" content="width=device-width, initial-scale=1">
			<style>
			.container {
	 		position: center;
	  		width: 30%;
			}
	
			.image {
	  		display: block;
			}
			</style>
			</head>
			
			<body>

			<div class="container">

	  		<img src="https://spark.apache.org/images/spark-logo-trademark.png" alt="Current Spark Results" class="image" >

			</div>
			<p style="font-size:18px;font-family:verdana">Originated at UC Berkeley in 2009, Apache Spark is a unified analytics 
			engine for big data processing. It includes support for SQL queries, streaming 
			data, machine learning, and graph processing. Spark runs on Hadoop, Apache Mesos, 
			Kubernetes, standalone, or in the cloud. Internet companies such as 
			Netflix, Yahoo, and eBay have deployed Spark at massive scale, collectively 
			processing multiple petabytes of data on clusters of over 8,000 nodes.</p>
			
			<div class="container">

	  		<img src="https://github.com/CMU-IDS-2021/fp--05839-jblane-rlahiri-cvajiac-amichell/blob/main/sparkCircle.png?raw=true" alt="Current Spark Results" class="image" height = 300>

			</div>
			
			</body>

			</html>
			""",
			height=700
			)
		
        st.markdown("---")
        st.markdown("***How Does it Work?***" )

		
        st.markdown("""Spark is capable of running different types of jobs. In this interface, we focus specifically on three specific types:""")
        
        components.html(
            """
            <!-- Slideshow container -->
            <html>
            <style>
            /*----------------------Carousel styles-----------------------*/
            * {
              box-sizing: border-box;
            }
            
            /* Position the image container (needed to position the left and right arrows) */
            .container {
              position: relative;
            }
            
            /* Hide the images by default */
            .mySlides {
              display: none;
            }
            
            /* Add a pointer when hovering over the thumbnail images */
            .cursor {
              cursor: pointer;
            }
            
            /* Next & previous buttons */
            .prev,
            .next {
              cursor: pointer;
              position: absolute;
              top: 40%;
              width: auto;
              padding: 16px;
              margin-top: -50px;
              color: white;
              font-weight: bold;
              font-size: 20px;
              border-radius: 0 3px 3px 0;
              user-select: none;
              -webkit-user-select: none;
            }
            
            /* Position the "next button" to the right */
            .next {
              right: 0;
              border-radius: 3px 0 0 3px;
            }
            
            /* On hover, add a black background color with a little bit see-through */
            .prev:hover,
            .next:hover {
              background-color: rgba(0, 0, 0, 0.8);
            }
            
            /* Number text (1/3 etc) */
            .numbertext {
              color: #f2f2f2;
              font-size: 12px;
              padding: 8px 12px;
              position: absolute;
              top: 0;
            }
            
            /* Container for image text */
            .caption-container {
              text-align: center;
              background-color: #222;
              padding: 2px 16px;
              color: white;
            }
            
            .row:after {
              content: "";
              display: table;
              clear: both;
            }
            
            /* Six columns side by side */
            .column {
              float: left;
              width: 16.66%;
            }
            
            /* Add a transparency effect for thumnbail images */
            .demo {
              opacity: 0.6;
            }
            
            .active,
            .demo:hover {
              opacity: 1;
            }
            </style>
            <script>
            var slideIndex = 1;
            showSlides(slideIndex);

            // Next/previous controls
            function plusSlides(n) {
              showSlides(slideIndex += n);
            }
            
            // Thumbnail image controls
            function currentSlide(n) {
              showSlides(slideIndex = n);
            }
            
            function showSlides(n) {
              var i;
              var slides = document.getElementsByClassName("mySlides");
              var dots = document.getElementsByClassName("dot");
              if (n > slides.length) {slideIndex = 1}
              if (n < 1) {slideIndex = slides.length}
              for (i = 0; i < slides.length; i++) {
                  slides[i].style.display = "none";
              }
              for (i = 0; i < dots.length; i++) {
                  dots[i].className = dots[i].className.replace(" active", "");
              }
              slides[slideIndex-1].style.display = "block";
              dots[slideIndex-1].className += " active";
            }
            </script>
            
            <div class="slideshow-container">
            
              <!-- Full-width images with number and caption text -->
              <div class="mySlides fade">
                <div class="numbertext">1 / 3</div>
                <img src="https://github.com/CMU-IDS-2021/fp--05839-jblane-rlahiri-cvajiac-amichell/blob/main/intro001.png?raw=true" style="width:100%">
                <div class="text">Caption Text</div>
              </div>
            
              <div class="mySlides fade">
                <div class="numbertext">2 / 3</div>
                <img src="https://github.com/CMU-IDS-2021/fp--05839-jblane-rlahiri-cvajiac-amichell/blob/main/intro002.png?raw=true" style="width:100%">
                <div class="text">Caption Two</div>
              </div>
            
              <div class="mySlides fade">
                <div class="numbertext">3 / 3</div>
                <img src="https://github.com/CMU-IDS-2021/fp--05839-jblane-rlahiri-cvajiac-amichell/blob/main/intro003.png?raw=true" style="width:100%">
                <div class="text">Caption Three</div>
              </div>
            
              <!-- Next and previous buttons -->
              <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
              <a class="next" onclick="plusSlides(1)">&#10095;</a>
            </div>
            <br>
            
            <!-- The dots/circles -->
            <div style="text-align:center">
              <span class="dot" onclick="currentSlide(1)"></span>
              <span class="dot" onclick="currentSlide(2)"></span>
              <span class="dot" onclick="currentSlide(3)"></span>
            </div>
            </html>
            """,
            height=800
            )
        
        st.markdown("""*Note: For simplicity, this interface will be performed using a premade static dataset of Spark job data.""" )
				


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
		filename = 'data/spark_ml_job.json'
		filename_strip = utils.extract_filename(filename)
		url = utils.prep_data(filename)
		dag = utils.json_to_nx('')

		#st.set_page_config(layout="wide")
		st.title("⭐A Better Spark User Interface⭐")
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
			alt.X("IMDB_Rating:Q", title='Time'),
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
	  
		st.header('Task Overview: What does the job look like?')
		col1, _, col2, _, col3, _ = st.beta_columns([1, 0.1, 1, 0.1, 1, 0.1])
		with col1:
			st.write('Task Graph: what are the job dependencies?')
			st.altair_chart(draw.job_dag(dag, filename_strip), use_container_width=True)

		with col2:
			st.write('Breakdown of events: What is Spark doing?')
			st.altair_chart(draw.count_histogram(url, 'Event:N'), use_container_width=True)

		with col3:
			st.write('How long does each job take?')
			st.altair_chart(draw.job_duration(url), use_container_width=True)
		


		col1, _, col2, _, col3 = st.beta_columns([1, 0.1, 1, 0.1, 1])
		if data_spill_button=="Yes":
			col1.header("Data Spill to Memory and Disk")
			col1.altair_chart(draw.data_spill(url), use_container_width=True)

		if suffle_read_button=="Yes":
			col2.header("Shuffle Read and Write")
			col2.altair_chart(draw.shuffle_read_write(url), use_container_width=True)
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
	#	ast.shared.components.write_page(page)
	#	#st.write(page)
	
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
#	with open(file_name) as f:
#		st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

#local_css("style.css")

#st.title("⭐Towards a Better Spark UI⭐")
#st.text("An Interactive Visualization")





#components.html(
#	"""
#	<!DOCTYPE html>
#	<html>
#	<head>
#	<meta name="viewport" content="width=device-width, initial-scale=1">
#	<style>
#	.container {
#	  position: relative;
#	  width: 50%;
#	}
	
#	.image {
#	  display: block;
#	  width: 100%;
#	  height: auto;
#	}
#	</style>
#	</head>
#	<body>
	
#	<!--<h2>Current Results View</h2>-->
#	<!--<p>Hover over the image to see the effect.</p>-->
	
#	<div class="container">
#	  <img src="https://spark.apache.org/images/spark-logo-trademark.png" alt="Current Spark Results" class="image" >
#	</div>
	
#	</body>
#	</html>
#	""",
#	height=100
#	)

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
#	with open(bin_file, 'rb') as f:
#		data = f.read()
#	return base64.b64encode(data).decode()
#def set_png_as_page_bg(png_file):
#	bin_str = get_base64_of_bin_file(png_file)
#	page_bg_img = '''
#	<style>
#	body {
#	background-image: url("data:image/jpg;base64,%s");
#	background-size: cover;
#	opacity: 1;
#	}
#	</style>
#	''' % bin_str
	
#	st.markdown(page_bg_img, unsafe_allow_html=True)
#	return
#set_png_as_page_bg('apache-spark1.jpg')
#task = st.selectbox(
#		"Which problem do you want to Visualize?", ["Word Count","Spark for ML","Apply Optimizations to an Extract, Transform, Load (ETL) job"])
#plot=alt.Chart(source).mark_bar().encode(
#	alt.X("IMDB_Rating:Q"),
#	y='count()',
	
#).properties(width=400,
#	height=200)
#data_spill_button=st.sidebar.radio("Show data spill to memory and disk",("Yes","No"))

#suffle_read_button=st.sidebar.radio("Show shuffle read and write quantities",("Yes","No"))

#Dataio_button=st.sidebar.radio("Show data input and output",("Yes","No"))

#if st.checkbox("Optimization 1"):
#	#TODO
#	st.write("Implement Optimization 1 on Data Set")
	
#if st.checkbox("Optimization 2"):
	#TODO
#	st.write("Implement Optimization 2 on Data Set")
	
	
#if st.checkbox("Optimization 3"):
#	#TODO 
#	st.write("Implement Optimization 3 on Data Set")
#col1, col2, col3 = st.beta_columns(3)
#if data_spill_button=="Yes":
#	col1.header("Data Spill to Memory and Disk")
#	col1.write(plot)
#	#row2_1, row2_2, row2_3 = st.beta_columns((2,1,1))

#if suffle_read_button=="Yes":
#	col2.header("Shuffle Read and Write")
#	col2.write(plot)
#if Dataio_button=="Yes":
#	col3.header("Data input and output")
#	col3.write(plot)
#st.write("** Display Data after Optimizations**")
#optimized=st.radio("",("Yes","No"))
#if optimized=="Yes":
#	st.write(plot.properties(width=600,height=300))
