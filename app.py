import pandas as pd
import plotly.express as px
import streamlit as st
     
car_data = pd.read_csv('datasets/vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
disp_button = st.button('Construir un gráfica de dispersión') # crear un botón
     
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma')
         
    fig = px.histogram(car_data, x="odometer")
     
         # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
if disp_button:
    st.write('Creacion de un diagrama de dispersion')

    #Creación de gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
    fig.show()