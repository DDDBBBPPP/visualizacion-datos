
import streamlit as st

from graficos import (
    barras,
    lineas,
    histograma,
    dispersion,
    burbujas
)

st.set_page_config(
    page_title="Visualización de datos",
    page_icon="📊",
    layout="wide"
)

# Menú de navegación
with st.sidebar:
    st.title("📊 Visualización de datos")
    st.caption("Matplotlib · Seaborn · Streamlit")

    grafico = st.radio(
        "Selecciona un gráfico",
        [
            "Barras agrupadas",
            "Líneas",
            "Histograma",
            "Dispersión",
            "Burbujas"
        ]
    )

    st.divider()
    st.caption("Práctica de visualización de datos")

# Cada módulo gestiona su propio contenido y pestañas
if grafico == "Barras agrupadas":
    barras.mostrar()

elif grafico == "Líneas":
    lineas.mostrar()

elif grafico == "Histograma":
    histograma.mostrar()

elif grafico == "Dispersión":
    dispersion.mostrar()

elif grafico == "Burbujas":
    burbujas.mostrar()
