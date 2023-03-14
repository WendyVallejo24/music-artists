import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Music Artists Popularity")
st.sidebar.image('logo.jpg')
st.sidebar.write('Author: Wendy Belén Vallejo Patraca')
st.sidebar.write('S20006733')

sidebar = st.sidebar
DATA_URL = 'artists.csv'

#cache
@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data

data_load_state = st.text('Cargando...')
data = load_data(500)
data_load_state.text('Done! (using st.cache)')

st.dataframe(data)

# --------------- buscar artista ----------------
@st.cache
def load_data_byname(name):
    data =pd.read_csv(DATA_URL)
    filtered_data_byname =data[data["artist_mb"].str.contains(name, case=False)]
    return filtered_data_byname

name = sidebar.text_input("Nombre del Artista")
btnbuscar = sidebar.button('Buscar Artista')

if(btnbuscar):
    filterbyname = load_data_byname(name)
    count_row = filterbyname.shape[0]
    st.write(f"Total artists: {count_row}")

    st.dataframe(filterbyname)

# --------------- select -----------------
@st.cache
def load_data_byartist(artist):
    data =pd.read_csv(DATA_URL)
    filtered_data_byartist = data[data['artist_mb'] == artist]

    return filtered_data_byartist

selected_artist =sidebar.selectbox('Seleccionar Artista ', data['artist_mb'].unique())
btnartist = sidebar.button('Seleccionar')

if(btnartist):
    filterbyartist =load_data_byartist(selected_artist)
    count_row = filterbyartist.shape[0]
    st.write(f"Total items: {count_row}")

    st.dataframe(filterbyartist)

# ------------ multiselect --------------------
country_mb = st.sidebar.multiselect("Selecciona Nacionalidades",
                                options=data['country_mb'].unique())

df_selection=data.query("country_mb == @country_mb")
st.write("Nacionalidad seleccionada",df_selection)

# ------------ histograma -------------
st.subheader('Histograma')
data = data['country_mb']
fig_country = px.bar(data,
                     x = data,
                     y = data.index,
                     orientation = 'v',
                     title = 'Cantidad por paises',
                     labels=dict(x="Country", index = 'Cantidad'),
                     color_discrete_sequence=['#7ECBB4'],
                     template = 'plotly_white')
st.plotly_chart(fig_country)

# -------------- grafica de barras -----------------
st.subheader('Gráfica de barras')
data = load_data(500)
artist=data['artist_mb']
listeners=data['listeners_lastfm']
fig_barra=px.bar(data,
                x=artist,
                y=listeners,
                title="Número de oyentes que tiene el artista",
                labels=dict(artist_mb="Artists", listeners_lastfm='Listeners'),
                color_discrete_sequence=["#7ECBB4"],
                template="plotly_white")
st.plotly_chart(fig_barra)

# --------- grafica scatter -----------
st.subheader('Gráfica Scatter')
country=data['country_mb']
artist=data['artist_mb']
listeners=data['listeners_lastfm']
fig_age=px.scatter(data,
                   x=country,
                   y=listeners,
                   color=artist,
                   title="¿De qué país es el artistas y qué tan escuchado es?",
                   labels=dict(country_mb="Country", artist_mb="Artist", listeners_lastfm="Listeners"),
                   template="plotly_white")
st.plotly_chart(fig_age)