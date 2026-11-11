
import streamlit as st
from graficos import barras

# Configuración general
st.set_page_config(
    page_title="Visualización de datos",
    page_icon="📊",
    layout="wide"
)

# Menú lateral
with st.sidebar:
    st.title("📊 Visualización de datos")
    st.caption("Matplotlib · Seaborn · Streamlit")

    grafico = st.radio(
        "Selecciona un gráfico",
        [
            "1. Barras agrupadas",
            "2. Líneas",
            "3. Histograma",
            "4. Dispersión",
            "5. Burbujas"
        ]
    )

    st.divider()
    st.caption("Práctica de visualización de datos")

# Contenido principal
if grafico == "1. Barras agrupadas":
    barras.mostrar()

else:
    st.info("Este gráfico se añadirá próximamente.")
