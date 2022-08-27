from numpy.core.records import array
import streamlit as st
from joblib import load
import numpy as np
import sys


def app():

    # Load Saved Results Data
    model = load(filename='models/satisfaction_model.joblib')

    st.title("Satisfaction Model")

    st.header("To calculate a user's satisfaction score, enter values below.")

    session_count = st.number_input('Enter The Sessions', key='a')
    total_time = st.number_input('Enter The Total Time', key='b')
    total_data = st.number_input('Enter Total Data', key='c')
    total_retransmission = st.number_input('Enter Tcp Retransmission', key='d')
    average_delay = st.number_input('Enter Average Delay', key='e')
    total_throughput = st.number_input('Enter Average Ahroughput', key='f')

    if st.button('Satisfaction prediction'):
        array = [session_count, total_time, total_data,
                 total_retransmission, average_delay, total_throughput]
        val = model.predict([array])
        satisfaction = [i[0] for i in val][0]
        st.write(
            "The Telcommunication user's estimated satisfaction score is: {:.3f}".format(satisfaction))
