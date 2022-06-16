from cgitb import text
import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image



# Read in the cereal data
df = pd.read_csv(
        'datasets/gold.csv'
    )
df2 = pd.read_csv('hasilpred.csv')

st.title('Prediksi Harga Emas - Regresi Linier')


image = Image.open('emas.jpg')
st.image(image)


# st.text('Memprediksi harga hingga bulan Februari')
x_options =[
    'Open', 'Close'
]

# Allow use to choose
st.sidebar.title("SELAMAT DATANG")
st.sidebar.subheader("Pilihan Data")
x_axis = st.sidebar.selectbox('',x_options)
# st.sidebar.subheader("")
# st.sidebar.subheader("")
# st.sidebar.subheader("")
# st.sidebar.subheader("")
# st.sidebar.subheader("")
# st.sidebar.subheader("")
# st.sidebar.subheader("")

st.sidebar.subheader("About Us")
st.sidebar.info(
    """
    KELAS DEVALOPA 
    
    Anggota :
    - Meriati Gabriella Pane
    - Nur Faizi
    - Mychael Yahya Gultom 
    - Nurul Alifa Putri Muslim
    - Markus Logan Jaya Manurung
    """
    )

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

st.markdown(
    """
    Emas adalah adalah logam mulia bersifat lunak dan memiliki instrumen investasi yang populer dan terpercaya. 
    Pergerakan investasi emas cenderung lebih stabil dan nilainya meningkat. 
    Emas salah satu jenis komoditi yang saat ini banyak diminati oleh investor karena dinilai menguntungkan. 
    Pergerakan investasi emas cenderung lebih stabil dan nilainya meningkat. 
    Berbeda dengan investasi kurs mata uang, investasi emas merupakan investasi jangka panjang. 
    """
)

st.plotly_chart(fig)
st.subheader('Hasil Prediksi')
st.markdown(
    """
    Prediksi ini dilakukan dengan menggunakan model regresi linier.
    Regresi linier adalah salah satu dari jenis analisis peramalan atau prediksi yang sering digunakan pada data berskala kuantitatif (interval atau rasio).
    Dilakukannya prediksi ini untuk mengetahui ramalan atau prediksi harga emas.
    Prediksi dilakukan hingga bulan februari.
    """
)
st.plotly_chart(fig2)

