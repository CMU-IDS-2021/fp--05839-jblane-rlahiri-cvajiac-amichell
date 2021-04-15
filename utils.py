import json
import networkx as nx
import os, sys
import streamlit as st

@st.cache(show_spinner=False)
def prep_data(filename: str) -> str:
	''' read JSON data from jobs -- each line is valid JSON object
    
        :param filename: path to job data
        :return string path for cleansed data'''
	with open(filename) as f:
		data = [json.loads(line) for line in f]
		data_json = json.dumps(data)

	url = '{}-sanitized.json'.format(os.path.splitext(filename)[0])
	with open(url, 'w') as f:
		json.dump(data_json, f)

	return url


def json_to_nx(filename: str) -> nx.Graph:
    ''' turn JSON DAG data into a networkx graph

        :param filename: path to graph data
        :return networkx Graph object '''

    return nx.balanced_tree(2, 3)