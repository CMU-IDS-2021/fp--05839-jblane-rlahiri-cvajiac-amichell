"""
Carnegie Mellon University - Interactive Data Science 05-839 Final Project

home.py defines the homepage for our StreamLit application
"""
import streamlit as st
import streamlit.components.v1 as components


def write():
    page_bg_img = '''<style>
                    body {
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

    st.title("⭐Why Do We Need a Better Spark UI?⭐")
    st.markdown("---")
    st.markdown("_**First, WHAT IS SPARK?!**_")
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
    st.markdown("_**So What's the Problem?**_")
    st.markdown("_Here's what Spark results look like now:_")
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


if __name__ == "__main__":
    write()
