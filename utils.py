import json
import networkx as nx
import os, sys
import pandas as pd
import streamlit as st

@st.cache(show_spinner=False)
def prep_data(filename: str) -> str:
	''' read JSON data from jobs -- each line is valid JSON object
    
        :param filename: path to job data
        :return string path for cleansed data'''
	with open(filename) as f:
		data = [json.loads(line) for line in f]

	url = '{}-sanitized.json'.format(os.path.splitext(filename)[0])
	with open(url, 'w') as f:
		json.dump(data, f)

	base = 'https://raw.githubusercontent.com/CMU-IDS-2021/fp--05839-jblane-rlahiri-cvajiac-amichell/main/data/{}-sanitized.json'
	return base.format(extract_filename(filename))


def json_to_nx(filename: str) -> nx.Graph:
    ''' turn JSON DAG data into a networkx graph

        :param filename: path to graph data
        :return networkx Graph object '''

    return nx.balanced_tree(2, 3)


def extract_filename(filename: str) -> str:
	''' remove path & extension from filename
	
		:param filename: path to file
		:return filename w/o path and extension '''

	return os.path.splitext(os.path.basename(filename))[0]