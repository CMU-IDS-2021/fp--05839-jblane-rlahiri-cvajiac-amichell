#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 08:41:01 2021

@author: jblane
"""
#cd /Users/jblane/Desktop/CMUClasses/S21\ -\ Interactive\ Data\ Science/fp--05839-jblane-rlahiri-cvajiac-amichell
# streamlit run intro_streamlitapp.py
# streamlit run main_streamlitapp.py

import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import altair as alt
from datetime import date

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")


st.title("⭐Why Do We Need a Better Spark UI?⭐")
st.text("An Interactive Visualization")
st.markdown("---")
st.markdown("_**First, WHAT IS SPARK?!**_" )
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
      width: 100%;
      height: auto;
    }
    </style>
    </head>
    <body>
    
    <!--<h2>Current Results View</h2>-->
    <!--<p>Hover over the image to see the effect.</p>-->
    
    <div class="container">
      <img src="https://spark.apache.org/images/spark-logo-trademark.png" alt="Current Spark Results" class="image" >
    </div>
    
    </body>
    </html>
    """,
    height=200
    )
st.markdown("""Originated at UC Berkeley in 2009, Apache Spark is a unified analytics 
            engine for big data processing. It includes support for SQL queries, streaming 
            data, machine learning, and graph processing. Spark runs on Hadoop, Apache Mesos, 
            Kubernetes, standalone, or in the cloud. Internet companies such as 
            Netflix, Yahoo, and eBay have deployed Spark at massive scale, collectively 
            processing multiple petabytes of data on clusters of over 8,000 nodes.""")


st.markdown("---")
st.markdown("_**So What's the Problem?**_" )
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
      background-color: #C88F0A;
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
    
    </body>
    </html>
    """,
    height=300
    )
st.markdown("""This UI displays some information, such as the job duration, stages, and a progress bar.
            However, all the information is displayed in tabular format and we don’t see a lot of other useful information,
            such as memory usage or shuffle read/writes. While this information is available, it is not presented with
            effective visual encodings that identify clearly the implication of different characteristics of Spark jobs.
            Furthermore, once the end user has hundreds or thousands of jobs, these tables become impossible to parse.""")

#random orange background color
# components.html(
#     """
#     <body style="background-color:#ffcc00"
#     </body>
#     """
#     )


# #collapsible grouping, only shows items one at a time
# components.html(
#     """
#     <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
#     <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
#     <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
#     <div id="accordion">
#       <div class="card">
#         <div class="card-header" id="headingOne">
#           <h5 class="mb-0">
#             <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
#             Team Members
#             </button>
#           </h5>
#         </div>
#         <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
#           <div class="card-body">
#             Andre
#           </div>
#           <div class="card-body">
#             Catalina
#           </div>
#           <div class="card-body">
#             Janice
#           </div>
#           <div class="card-body">
#             Riddhiman
#           </div>
#         </div>
#       </div>
#       <div class="card">
#         <div class="card-header" id="headingTwo">
#           <h5 class="mb-0">
#             <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
#             Random List of Stuff
#             </button>
#           </h5>
#         </div>
#         <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
#           <div class="card-body">
#             First thing
#           </div>
#         </div>
#       </div>
#     </div>
#     """,
#     height=500,
# )

# #---A search field to nowhere example -css makes the blue background---#



# def remote_css(url):
#     st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)    

# def icon(icon_name):
#     st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)

# local_css("https://github.com/CMU-IDS-2021/fp--05839-jblane-rlahiri-cvajiac-amichell/blob/main/style.css")
#local_css("style.css")

# remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

# icon("outdoor_grill") #use word list of google icons: https://fonts.google.com/icons
# selected = st.text_input("", "This text input bar goes nowhere right now...")
# button_clicked = st.button("OK")

# #-----------------------------------------_