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

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

st.title("⭐Towards a Better Spark UI⭐")
st.text("An Interactive Visualization")

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