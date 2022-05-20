from turtle import title
from dash import dash, dcc, html
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df1 = pd.read_csv('datasets/data2.csv')
df2 = pd.read_csv('hasilpred.csv')

fig1 = px.line(
 df1, x="Updated_at", y="Sell", title = "Penjualan Emas")

fig = px.line(df2, x="Updated_at", y=df2.columns,
              hover_data={"Updated_at": "|%B %d, %Y"},
              title='Hasil Prediksi')
fig.update_xaxes(
    dtick="M1",
    tickformat="%b\n%Y")
# fig2.show()

app.layout = html.Div([
    dcc.Graph(figure=fig1),
    dcc.Graph(figure = fig)
])

if __name__ == '__main__':
 app.run_server(port = 8080, debug=True)
