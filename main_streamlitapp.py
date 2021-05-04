#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr	8 10:30:52 2021

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
from PIL import Image
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
				
				#st.markdown("***First, WHAT IS APACHE SPARK?!***" )
				my_expander1 = st.beta_expander("1) WHAT IS APACHE SPARK?!")
				
				with my_expander1:
						sparkLogo = Image.open('./spark-logo-trademark.png')
						st.image(sparkLogo)
		
		
						st.markdown("""<p class="listFont"> Originated at UC Berkeley in 2009, Apache Spark is a unified analytics 
					engine for big data processing. It includes support for SQL queries, streaming 
					data, machine learning, and graph processing. Spark runs on Hadoop, Apache Mesos, 
					Kubernetes, standalone, or in the cloud. Internet companies such as 
					Netflix, Yahoo, and eBay have deployed Spark at massive scale, collectively 
					processing multiple petabytes of data on clusters of over 8,000 nodes.</p>""", unsafe_allow_html=True)
						
						

				#st.markdown("***HOW DOES IT WORK?***" )
				my_expander2 = st.beta_expander("2) HOW DOES IT WORK?")
				
				with my_expander2:
		
						st.markdown("""<p class="listFont"> Spark is capable of running different types of jobs. In this interface, we focus on three specific types (click side arrows):</p>
								""", unsafe_allow_html=True)

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
						
						
						<div class="slideshow-container">
						
							<!-- Full-width images with number and caption text -->
							<div class="mySlides fade">
								<div class="numbertext">1 / 3</div>
								<img src="https://github.com/CMU-IDS-2021/fp--05839-jblane-rlahiri-cvajiac-amichell/blob/main/intro001.png?raw=true" style="width:100%">
								<!--<div class="text">Caption Text</div>-->
							</div>
						
							<div class="mySlides fade">
								<div class="numbertext">2 / 3</div>
								<img src="https://github.com/CMU-IDS-2021/fp--05839-jblane-rlahiri-cvajiac-amichell/blob/main/intro002.png?raw=true" style="width:100%">
								<!--<div class="text">Caption Two</div>-->
							</div>
						
							<div class="mySlides fade">
								<div class="numbertext">3 / 3</div>
								<img src="https://github.com/CMU-IDS-2021/fp--05839-jblane-rlahiri-cvajiac-amichell/blob/main/intro003.png?raw=true" style="width:100%">
								<!--<div class="text">Caption Three</div>-->
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
						<div>
						<p style="font-size:18px;font-family:verdana">
						*Note: For simplicity, this interface will be performed using preselected optimization strategies for each Spark job.
						</p>
						</div>
						</html>
						
						
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
						
								""",
								height=800,scrolling=True
								)
		


				#st.markdown("---")
				#st.markdown("***SO, WHAT'S THE PROBLEM?***" )
				my_expander3 = st.beta_expander("3) SO, WHAT'S THE PROBLEM?")
				
				with my_expander3:
						st.markdown("""<p class="listFont"> Here's what Spark results look like now:</p>
												""", unsafe_allow_html=True)
						components.html("""
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
						
						.listFont{
						font-size: 18px !important;
						font-family: "verdana" !important;
						}
						
			</style>
			</head>
			<body>
	
			<!--<h2>Current Results View</h2>-->
			<!--<p>Hover over the image to see the effect.</p>-->
	
			<div class="container">
				<img src="https://github.com/CMU-IDS-2021/fp--05839-jblane-rlahiri-cvajiac-amichell/blob/main/job_example.png?raw=true" alt="Current Spark Results" class="image">
				<div class="overlay">
			<div class="text">Some useful stuff, but how to make sense of it?!</div>
				</div>
			</div>
			
			<p style="font-size:18px;font-family:verdana">
						Pros: </br> </p>
								<ul class="listFont">
								<li>Some useful information: job duration, stages, progress bar, etc.</li>
								</ul>
								</br> </br>
			
						<p style="font-size:18px;font-family:verdana">
						Cons:</br>
						</p>
								<ul class="listFont">
								<li>which machines running which jobs?</li>
								<li>where is the data being transferred?</li>
								<li>where are the bottlenecks?</li>
								<li>time spent executing, shuffling, reading/writing data?</li>
								<li>tabular format: difficult to <i>visualize</i> useful information
								</ul>
		
				
			</body>
			</html>
			""",
					height=800,
								scrolling=True)
						
				st.markdown("Click on the Main Interface on the Navigation bar (to the left) to see how we created more useful visualizations." )




class interface:
	
	def write(self):
		with open('./interfacestyle.css') as f:
				st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
		

		st.title("⭐A Better Spark User Interface⭐")
		st.markdown("""
 		* Use the menu at left to select data and set plot parameters
 		* Your plots will appear below
		""")

		st.sidebar.markdown("## Select Plots to Show")

		task = st.selectbox(
				"Which problem do you want to Visualize?", ["Word Count","Extract, Transform, Load (ETL)"])

		data_spill_button=st.sidebar.radio("Show data spill to memory and disk",("Yes","No"), 1)

		suffle_read_button=st.sidebar.radio("Show shuffle read and write quantities",("Yes","No"))
		#Dataio_button=st.sidebar.radio("Show data input and output",("Yes","No"))
		#row2_1, row2_2, row2_3, row2_4 = st.beta_columns((2,1,1,1))
		st.write("** Please select a checkbox to implement one or more optimization**")
		opt_text = utils.WC_OPTS if task == 'Word Count' else utils.ETL_OPTS
		is_opt_one =	st.checkbox(opt_text[0])
		is_opt_two =	st.checkbox(opt_text[1])
		is_opt_three =	st.checkbox(opt_text[2])
	
		filename = utils.get_filename(task, is_opt_one, is_opt_two, is_opt_three)
		filename_strip = utils.extract_filename(filename)
		url = utils.prep_data('data/{}.json'.format(filename), task)

		with st.beta_expander('Click Here to Display the Code!!!'):
			with open('spark/{}.py'.format(filename), 'r') as f:
				code = ''.join(line for line in f)
			st.code(code)
		
		st.header('Task Overview: What does the job look like?')
		col1, _, col2, _, col3, _ = st.beta_columns([1, 0.1, 1, 0.1, 1, 0.1])

		with col1:
			st.write('Breakdown of events: What is Spark doing?')
			st.altair_chart(draw.count_histogram(url, 'Event:N'), use_container_width=True)

		with col2:
			st.write('Breakdown of events: What is Spark doing over time?')
			st.altair_chart(draw.strip_chart(url, 'Event:N'), use_container_width=True)

		with col3:
			st.write('How long does each job take?')
			st.altair_chart(draw.job_duration(url), use_container_width=True)
		


		charts = []
		if data_spill_button=="Yes":
			st.header("Data Spill to Memory and Disk")
			st.altair_chart(draw.data_spill(url), use_container_width=True)
			#charts.append(draw.data_spill(url))

		if suffle_read_button=="Yes":
			st.header("Shuffle Read and Write")
			st.altair_chart(draw.shuffle_read_write(url), use_container_width=True)


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
#		position: relative;
#		width: 50%;
#	}
	
#	.image {
#		display: block;
#		width: 100%;
#		height: auto;
#	}
#	</style>
#	</head>
#	<body>
	
#	<!--<h2>Current Results View</h2>-->
#	<!--<p>Hover over the image to see the effect.</p>-->
	
#	<div class="container">
#		<img src="https://spark.apache.org/images/spark-logo-trademark.png" alt="Current Spark Results" class="image" >
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
#vmax = st.sidebar.slider('Colorbar Max Energy', 10, 500, 25)	# min, max, default
#qcenter = st.sidebar.slider('Data', 5, 120, 5)	# min, max, default
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
