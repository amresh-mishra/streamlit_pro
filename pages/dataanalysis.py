import streamlit as st
from matplotlib import image
import numpy as np
import pandas as pd
import os
import plotly.express as px
import plotly.graph_objects as go


# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "ipl1.jpeg")
DATA_PATH = os.path.join(dir_of_interest, "data", "Top_100_batsman.csv")

img = image.imread(IMAGE_PATH)
st.image(img)
st.title(':blue[IPL analytics 2008- 2019]')
st.title(':red[Batsman KPIs]')

batsman = pd.read_csv(DATA_PATH, encoding = 'unicode_escape')


Batsman_matches = batsman[batsman['Runs']>3000]
topfive=(Batsman_matches['PLAYER'].iloc[0:5])
df1 = batsman
fig5 = px.bar(df1, x=batsman['PLAYER'], y=batsman['Avg'], color=batsman['SR'])
st.plotly_chart(fig5)
st.title(':red[Top 5 batsman by Run]')
fig6 = go.Figure()
fig6.add_trace(go.Scatter(x=topfive, y=(batsman['Runs'].iloc[0:5]),
                    mode='lines+markers',
                    name='lines+markers'))
st.plotly_chart(fig6)


Matches=pd.read_csv('https://raw.githubusercontent.com/akpythonyt/Datasets/main/matches.csv')
bat=Matches['toss_winner'].loc[Matches['toss_decision']=='bat']
battoss=(bat.value_counts())
st.title('Teams chose batting when they won toss')
data = bat
fig7 = px.bar(data, x=battoss.values, y=battoss.index)
st.plotly_chart(fig7)
field=Matches['toss_winner'].loc[Matches['toss_decision']=='field']
fieldtoss=(field.value_counts())
data = field
st.title('Teams chose bowling when they won toss')
fig8 = px.bar(data, x=fieldtoss.values, y=fieldtoss.index)
st.plotly_chart(fig8)
st.title('Overall toss mapping')
Overalltosswin=fieldtoss+battoss
pie_col = ["Red","Blue","Yellow","Purple","Black","Indigo","Salmon","Olive","Green","Teal","Aqua","Silver","Navy",'white']
fig9 = px.pie(values=Overalltosswin.values, names= Overalltosswin.index)
st.plotly_chart(fig9)
count = Matches['winner'].value_counts()
st.title('Most successful teams based on win count')
pie_col = ["Red","Blue","Yellow","Purple","Black","Indigo","Salmon","Olive","Green","Teal","Aqua","Silver","Navy",'white']
fig = px.pie(values=count.values, names= count.index)
st.plotly_chart(fig)
st.title('Player of the Match award')
count = Matches['player_of_match'].value_counts()
fig1 = go.Figure(data=[go.Scatter(
    x=count.index, y=count.head(5),
    mode='markers',
    marker=dict(
        color=['rgb(93, 164, 214)', 'rgb(255, 144, 14)',
               'rgb(44, 160, 101)', 'rgb(255, 65, 54)','yellow'],
        opacity=[1, 0.8, 0.6, 0.4,0.3],
        size=[40, 60, 80, 100,105],
    )
)])
st.plotly_chart(fig1)
st.title('Top 5 Bowlers Based on wickets')
Bowlers=pd.read_csv('https://raw.githubusercontent.com/akpythonyt/Datasets/main/Top_100_bowlers.csv')
Bowlers_matches = Bowlers[Bowlers['Wkts']>1]
topfive=(Bowlers_matches['PLAYER'].iloc[0:5])
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=topfive, y=(Bowlers['Wkts'].iloc[0:5]),
                    mode='lines+markers',
                    name='lines+markers'))
st.plotly_chart(fig2)