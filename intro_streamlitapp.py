#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 08:41:01 2021

@author: jblane
"""
#cd /Users/jblane/Desktop/CMUClasses/S21\ -\ Interactive\ Data\ Science/fp--05839-jblane-rlahiri-cvajiac-amichell
# streamlit run intro_streamlitapp.py

import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import altair as alt
from datetime import date

#random orange background color
components.html(
    """
    <body style="background-color:#ffcc00"
    </body>
    """
    )

st.title("⭐Towards a Better Spark UI⭐")
st.text("An Interactive Visualization")

st.markdown("---")
st.markdown("_**Welcome!**_" )
st.markdown(" Stuff...and more stuff.")

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
    
    .overlay {
      position: absolute;
      top: 0;
      bottom: 0;
      left: 0;
      right: 0;
      height: 100%;
      width: 100%;
      opacity: 0;
      transition: .5s ease;
      background-color: #008CBA;
    }
    
    .container:hover .overlay {
      opacity: 1;
    }
    
    .text {
      color: white;
      font-size: 20px;
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
    
    <h2>Fade in Overlay</h2>
    <p>Hover over the image to see the effect.</p>
    
    <div class="container">
      <img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" class="image">
      <div class="overlay">
        <div class="text">Hello World</div>
      </div>
    </div>
    
    </body>
    </html>
    """,
    height=500,
    )


# #colapsible grouping, only shows items one at a time
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

# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# def remote_css(url):
#     st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)    

# def icon(icon_name):
#     st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)

# local_css("style.css")
# remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

# icon("outdoor_grill") #use word list of google icons: https://fonts.google.com/icons
# selected = st.text_input("", "This text input bar goes nowhere right now...")
# button_clicked = st.button("OK")

# #-----------------------------------------_