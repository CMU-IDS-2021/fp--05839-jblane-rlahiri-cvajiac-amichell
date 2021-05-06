import pandas as pd
import networkx as nx
import os
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
    """ read JSON data from jobs -- each line is valid JSON object
        :param task: The task the user has selected to explore optimizations for
        :param filename: path to job data
        :return string path for cleansed data"""
    base = 'https://raw.githubusercontent.com/CMU-IDS-2021/fp--05839-jblane-rlahiri-cvajiac-amichell/' \
           'main/data/{}-sanitized.json'
    return base.format(filename)


def json_to_nx(filename: str) -> nx.Graph:
    """ turn JSON DAG data into a networkx graph

        :param filename: path to graph data
        :return networkx Graph object """
    return nx.balanced_tree(2, 3)


def extract_filename(filename: str) -> str:
    """ remove path & extension from filename

        :param filename: path to file
        :return filename w/o path and extension """
    return os.path.splitext(os.path.basename(filename))[0]


def get_filename(job: str, is_one: bool, is_two: bool, is_three: bool) -> str:
    """ get filename of source code based on filename and checked optimizations

        :param job:			name of job (Word Count or ETL)
        :param is_one:		true if optimization 1 selected
        :param is_two:		true if optimization 2 selected
        :param is_three:	true if optimization 3 selected
        :return location of source code """
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


def get_runtime(file_name: str) -> int:
    """
    gets the overall runtime of a provided application using the provided data

    :param file_name: the location of the data to load
    :return: an integer indicating the total runtime in seconds
    """
    url = f"data/{file_name}-sanitized.json"

    data = pd.read_json(url)

    start_time = data[data["Event"] == "SparkListenerApplicationStart"]["Timestamp"].values[0]
    end_time = data[data["Event"] == "SparkListenerApplicationEnd"]["Timestamp"].values[0]
    elapsed_time = end_time - start_time
    return int(elapsed_time.item()/10**9)
