"""
Carnegie Mellon University - Interactive Data Science 05-839 Final Project

draw.py contains useful utilities that help separate plot drawing functionality into other files.
"""

import altair as alt
import networkx as nx
import os
import pickle as pkl


def count_histogram(url: str, field: str) -> alt.Chart:
    """ produce histogram displaying counts of a particular field

        :param url: online url or path to data
        :param field: field to count (with type specified)
        :return altair histogram of counts """

    field_s = field.split(':')[0]  # split type from field name
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

    return bars + text


def strip_chart(url: str, field: str) -> alt.Chart:
    """ produce strip chart displaying counts of a particular field

        :param url: online url or path to data
        :param field: field to count (with ty over timepe specified)
        :return altair strip chart of counts """

    field_s = field.split(':')[0] # split type from field name

    specs = [
        ('SparkListenerStageSubmitted', "datum['Stage Info']['Submission Time']"),
        ('SparkListenerStageCompleted', "datum['Stage Info']['Completion Time']"),
        ('SparkListenerTaskStart', "datum['Task Info']['Launch Time']"),
        ('SparkListenerTaskEnd', "datum['Task Info']['Finish Time']"),
        ('SparkListenerApplicationStart', "datum['Timestamp']"),
        ('SparkListenerApplicationEnd', "datum['Timestamp']"),
        ('SparkListenerJobStart', "datum['Submission Time']"),
        ('SparkListenerJobEnd', "datum['Completion Time']"),
    ]

    return alt.layer(*[alt.Chart(url).transform_filter(
        alt.datum.Event == event
        ).transform_calculate(
            time=time_s
        ).mark_tick(
            binSpacing=0,
        ).encode(
            x=alt.X('time:T', axis=alt.Axis(labelAngle=-45, grid=False)),
            y=alt.Y(field, scale=alt.Scale(type='log'), axis=alt.Axis(grid=False)),
            color=alt.Color('count({}):Q'.format(field_s), scale=alt.Scale(scheme='goldred', type='sqrt')),
            tooltip=['time:T', 'count()']
        ).properties(
            height=300,
            width=600
        )
        for event, time_s in specs])


def job_times(url: str) -> alt.Chart:
    """ produce histogram displaying counts of a particular field

        :param url: online url or path to data
        :return altair chart showing times, split by job id"""
    return alt.Chart(url).transform_calculate(
        time="replace(toString(datum['Submission Time']) + toString(datum['Completion Time']), 'null', '')"
    ).mark_area().encode(
        x=alt.X('time:T', axis=alt.Axis(grid=False)),
        y=alt.Y('count()', axis=alt.Axis(grid=False)),
        row=alt.Row('Job ID:O'),
    ).properties(
        width=600,
        height=30
    ).transform_filter(
        (alt.datum.Event == 'SparkListenerJobStart') | (alt.datum.Event == 'SparkListenerJobEnd')
    )


def data_spill(url: str) -> alt.Chart:
    """ draw data spill chart in altair

        :param url: link to data
        :return altair chart of data spill"""
    return alt.Chart(url).mark_area().transform_filter(
        (alt.datum.Event == 'SparkListenerTaskEnd')
    ).transform_calculate(
        bytes="datum['Task Metrics']['Disk Bytes Spilled'] / 1000000"
    ).encode(
        x=alt.X('Task Info.Finish Time:T', axis=alt.Axis(title='Time', grid=False)),
        y=alt.Y('bytes:Q', stack='center', axis=alt.Axis(title='MB spilled to mem & disk', grid=False)),
        color=alt.Color('Stage ID:N', scale=alt.Scale(scheme='category20b'), legend=None),
        tooltip=['Task Info.Finish Time:T', 'bytes:Q']
    )


def shuffle_read_write(url: str) -> alt.Chart:
    """ draw shuffle read/write chart in altair

        :param url: link to data
        :return altair chart of shuffle reads/writes """
    # makes transform_calc string nicer
    datum_s = lambda s1, s2: "datum['Task Metrics']['Shuffle {} Metrics']['{}']".format(s1, s2)
    return alt.Chart(url).mark_area().transform_filter(
        alt.datum.Event == 'SparkListenerTaskEnd'
    ).transform_calculate(
        bytes="({}+{}) / 1000000".format(datum_s('Read', 'Local Bytes Read'), datum_s('Write', 'Shuffle Bytes Written'))
    ).encode(
        x=alt.X('Task Info.Finish Time:T', axis=alt.Axis(title='Time', grid=False)),
        y=alt.Y('bytes:Q', stack='center', title='MB shuffled', axis=alt.Axis(grid=False)),
        color=alt.Color('Stage ID:N', scale=alt.Scale(scheme='category20b'), legend=None),
        tooltip=['Task Info.Finish Time:T', 'bytes:Q', 'Stage ID:N']
    )


def job_duration(url: str) -> alt.Chart:
    """ draw job duration faceted chart in altair

        :param url: link to data
        :return altair chart showing duration of each job """
    return alt.Chart(url).transform_calculate(
        time="replace(toString(datum['Submission Time']) + toString(datum['Completion Time']), 'null', '')"
    ).mark_area().encode(
        x=alt.X('time:T', axis=alt.Axis(grid=False)),
        y=alt.Y('count()', axis=alt.Axis(grid=False, tickCount=0), title=None),
        row=alt.Row('Job ID:O'),
        tooltip=['time:T', 'count()']
    ).properties(
        width=600,
        height=25
    ).transform_filter(
        (alt.datum.Event == 'SparkListenerJobStart') | (alt.datum.Event == 'SparkListenerJobEnd')
    ).configure_facet(
        spacing=1
    )
