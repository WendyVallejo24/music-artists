import streamlit as st
import pandas as pd

st.title("Music Artists Popularity")
st.sidebar.image('logo.jpg')
st.sidebar.write('Author: Wendy Belén Vallejo Patraca')

sidebar = st.sidebar
DATA_URL = 'artists.csv'

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data

data_load_state = st.text('Cargando...')
data = load_data(500)
data_load_state.text('Done! (using st.cache)')

st.dataframe(data)

@st.cache
def load_data_byname(name):
    data =pd.read_csv(DATA_URL)
    filtered_data_byname =data[data["artist_mb"].str.contains(name)]
    return filtered_data_byname

name = sidebar.text_input("Nombre del Artista")
btnbuscar = sidebar.button('Buscar Artista')

if(btnbuscar):
    filterbyname = load_data_byname(name)
    count_row = filterbyname.shape[0]
    st.write(f"Total artists: {count_row}")

    st.dataframe(filterbyname)