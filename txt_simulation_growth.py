import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title('Monte Carlo simulation for bacterial growth')
st.write("Simulation")

E_N0 = st.number_input('N0',value=10)
N_stop = st.number_input('N_stop',value=10**3)
rep = st.number_input('Repetition',value=100)
Lag = st.number_input('Lag time',value=1.45)
mu = st.number_input('µmax',value=0.86)
st.write('N0 is', E_N0,'Lag time is ', Lag,'µmax is', mu)


fig, ax = plt.subplots()
for z in range(rep):
    N0 = np.random.poisson(E_N0)
    Growth_Number = N_stop-N0
    Number_of_cell = np.arange(N0, N_stop + 1)
    interval_of_time_to_division = -np.log(np.random.rand(Growth_Number))/(mu*np.arange(N0,N_stop))
    division_time = np.zeros(len(interval_of_time_to_division) + 1)
    for i in range(len(interval_of_time_to_division)):
        division_time[i + 1] = sum(interval_of_time_to_division[:i]) + Lag
    ax.plot(division_time, np.log10(Number_of_cell), drawstyle = 'steps-post')
ax.set_ylabel("Cell counts [$\log_{10}$CFU]", fontsize = 16)
ax.set_xlabel('Time [h]', fontsize=16, color='k')
ax.tick_params(labelsize=16, direction='out')
st.pyplot(fig)

st.write('Reference')
st.write('Application of growth rate from kinetic model to calculate stochastic growth of a bacteria population at low contamination level')
