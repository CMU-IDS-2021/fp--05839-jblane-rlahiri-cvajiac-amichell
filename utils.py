import json
import networkx as nx
import os, sys
import pandas as pd
import streamlit as st

WC_OPTS = [
	'Reduce the size of each record in the RDD by pre-reducing RDDs',
	'Increase the Default Parallelism',
	'Adjust processing logic to avoid expensive regex operations'
]

ETL_OPTS = [
	'Reduce filter steps down to only one filter',
	'Adjust memory available to use ~70% of available memory on executors',
	'Change data structure to avoid join and reduce expensive operations'
]


@st.cache(show_spinner=False)
def prep_data(filename: str, task: str) -> str:
	''' read JSON data from jobs -- each line is valid JSON object
    
        :param filename: path to job data
        :return string path for cleansed data'''

	task_s = 'wordcount' if task == 'Word Count' else 'etl'
	with open(filename.replace('-', '_')) as f:
		data = [json.loads(line) for line in f]

	url = '{}-sanitized.json'.format(os.path.splitext(filename)[0])
	with open(url, 'w') as f:
		json.dump(data, f)

	base = 'https://raw.githubusercontent.com/CMU-IDS-2021/fp--05839-jblane-rlahiri-cvajiac-amichell/main/data/{}/{}-sanitized.json'
	return base.format(task_s, extract_filename(filename))


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


def get_filename(job: str, is_one: bool, is_two: bool, is_three: bool) -> str:
	''' get filename of source code based on filename and checked optimizations

		:param job:			name of job (Word Count or ETL)
		:param is_one:		true if optimization 1 selected
		:param is_two:		true if optimization 2 selected
		:param is_three:	true if optimization 3 selected
		:return location of source code '''

	task_s = 'wordcount' if job == 'Word Count' else 'etl'

	suffix = [task_s]

	if not any([is_one, is_two, is_three]):
		suffix.append('base')

	if is_one:
		suffix.append('one')
	if is_two:
		suffix.append('two')
	if is_three:
		suffix.append('three')

	return '{}/{}'.format(task_s, '-'.join(suffix))