from turtle import title
from unittest import result
from dash import dash, dcc, html
import plotly.graph_objects as go
import streamlit as st
import pandas as pd
import plotly.express as px
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

data = pd.read_csv('datasets/gold.csv')
df=(data['Date'] > '2020-01-01') & (data['Date'] <= '2022-05-20')
df1=(data.loc[df])
df2 = pd.read_csv('hasilpred.csv')

fig1 = px.line(
 df1, x="Date", y="Open", title = "Penjualan Emas")

fig = px.line(df2, y=df2.columns, x='Date',
              hover_data={"Date": "|%B %d, %Y"},
              title='Hasil Prediksi')
fig.update_xaxes(
    dtick="M1",
    tickformat="%b\n%Y")

px.title('PREDIKSI EMAS DENGAN METODE REGRESI LINIER')
# st.sidebar('Which value do you want to explore?')

app.layout = html.Div([
    dcc.Graph(figure=fig1),
    dcc.Graph(figure = fig)
])



if __name__ == '__main__':
 app.run_server(port = 8050, debug=True)
