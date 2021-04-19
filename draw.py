import altair as alt
import networkx as nx
import nx_altair as nxa
import os
import pickle as pkl

from pprint import pprint

def count_histogram(url: list, field: str) -> alt.Chart:
    ''' produce histogram displaying counts of a particular field

        :param url: online url or path to data
        :param field: field to count (with type specified) 
        :return altair histogram of counts '''

    field_s = field.split(':')[0] # split type from field name
    bars = alt.Chart(url).mark_bar().encode(
        x=alt.X(field, axis=alt.Axis(labelAngle=-45)),
        y=alt.Y('count({}):Q'.format(field_s), scale=alt.Scale(type='log'), axis=alt.Axis(grid=False))
    ).properties(
        width=600,
        height=300
    )

    text = bars.mark_text(
        align='center',
        baseline='middle',
        dy=-5
    ).encode(
        text='count(Event):Q'
    )

    return (bars+text)


def job_times(url: str) -> alt.Chart:
    ''' produce histogram displaying counts of a particular field

        :param url: online url or path to data
        :return altair chart showing times, split by job id'''
    return alt.Chart(url).transform_calculate(
        time="replace(toString(datum['Submission Time']) + toString(datum['Completion Time']), 'null', '')"
    ).mark_area().encode(
        x=alt.X('time:T'),
        y=alt.Y('count()'),
        row=alt.Row('Job ID:O'),
        tooltip = ['time:T', 'count()']
    ).properties(
        width=600,
        height=30
    ).transform_filter(
        (alt.datum.Event == 'SparkListenerJobStart') | (alt.datum.Event == 'SparkListenerJobEnd')
    ).configure_facet(
        spacing=0
    )


def job_dag(graph: nx.Graph, filename: str) -> alt.Chart:
    ''' draw task graph in altair

        :param graph: task graph
        :return altair chart of task graph'''

    pkl_filename = 'data/{}-pos.pkl'.format(filename)
    if os.path.exists(pkl_filename):
        with open(pkl_filename, 'rb') as f:
            pos = pkl.load(f)
    else:
        pos = nx.drawing.nx_pydot.graphviz_layout(graph, prog='dot')
        with open(pkl_filename, 'wb') as f:
            pkl.dump(pos, f)
    flipped_pos = {node: (-y,x) for (node, (x,y)) in pos.items()}

    return nxa.draw_networkx(
        graph,
        pos=flipped_pos,
    ).properties(
        width=800,
        height=300
    )