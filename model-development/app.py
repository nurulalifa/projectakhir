import streamlit as st
import pandas as pd
import plotly.express as px


# Read in the cereal data
df = pd.read_csv(
        'datasets/gold.csv'
    )
df2 = pd.read_csv('hasilpred.csv')

st.title('Prediksi Harga Emas - Regresi Linier')

x_options =[
    'Open', 'Close'
]

# Allow use to choose
x_axis = st.sidebar.selectbox('PILIH', x_options)

# plot the value
fig = px.line(df,
                x='Date',
                y=x_axis,
                # hover_name='Open',
                title=f'Penjualan Emas - {x_axis}')

fig2= px.line(df2,
                x='Date',
                y=df2.columns,
                # hover_name='Open',
                title=f'Hasil Prediksi')
st.plotly_chart(fig)
st.plotly_chart(fig2)