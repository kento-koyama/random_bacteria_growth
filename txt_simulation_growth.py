import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import base64

st.title('Monte Carlo simulation for bacterial growth')
st.write("## Simulation")

E_N0 = st.number_input('N0',value=10, min_value=1, max_value=10**3)
N_stop = st.number_input('N_stop',value=10**3, min_value=1, max_value=10**3)
rep = st.number_input('Repetition',value=100, min_value=1, max_value=100)
Lag = st.number_input('Lag time',value=1.45)
mu = st.number_input('µmax',value=0.86)
st.write('N0 is', E_N0,'Lag time is ', Lag,'µmax is', mu)

box = []

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
    box.append(division_time)
ax.set_ylabel("Cell counts [$\log_{10}$CFU]", fontsize = 16)
ax.set_xlabel('Time [h]', fontsize=16, color='k')
ax.tick_params(labelsize=16, direction='out')
st.pyplot(fig)

df = pd.DataFrame(box)
event_str = np.array(range(0, df.shape[1], 1))
event_str = [str(n) for n in event_str]
event_str = ['event'+s for s in event_str]
rep_name = np.array(range(1, rep+1, 1))
rep_name = [str(n) for n in rep_name]
rep_name = ['rep'+s for s in rep_name]
df["rep"] = rep_name
df.set_index("rep",inplace=True)
df.columns = event_str
st.subheader('Table: The simulation result')
st.dataframe(df)

csv = df.to_csv(index=True)  
b64 = base64.b64encode(csv.encode()).decode()
href = f'<a href="data:application/octet-stream;base64,{b64}" download="result.csv">download</a>'
st.markdown(f"Download the result as a csv file {href}", unsafe_allow_html=True)

st.write('## Reference')
st.write('Koyama, K., Hiura, S., Abe, H., Koseki, S. Application of growth rate from kinetic model to calculate stochastic growth of a bacteria population at low contamination level, 2021, Journal of Theoretical Biology, 525, 21, 110758. [doi.org/10.1016/j.jtbi.2021.110758](https://doi.org/10.1016/j.jtbi.2021.110758)')
