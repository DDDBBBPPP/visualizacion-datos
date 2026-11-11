
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Visualización de datos",
    page_icon="📊",
    layout="wide"
)

st.title("Visualización de datos")
st.write("Comparación de gráficos con Matplotlib y Seaborn")

st.header("1. Ventas de videojuegos por plataforma")

df = pd.DataFrame({
    "Genero": ["Acción", "Aventura", "RPG", "Deportes", "Estrategia"],
    "PC": [42, 35, 58, 18, 46],
    "PlayStation": [75, 62, 55, 68, 20],
    "Xbox": [60, 45, 38, 52, 15]
})

st.subheader("Datos utilizados")
st.dataframe(df, hide_index=True)

biblioteca = st.radio(
    "Selecciona la biblioteca:",
    ["Matplotlib", "Seaborn"],
    horizontal=True
)

fig, ax = plt.subplots(figsize=(10, 5))

if biblioteca == "Matplotlib":
    import numpy as np

    x = np.arange(len(df))
    ancho = 0.25

    ax.bar(x - ancho, df["PC"], ancho, label="PC")
    ax.bar(x, df["PlayStation"], ancho, label="PlayStation")
    ax.bar(x + ancho, df["Xbox"], ancho, label="Xbox")

    ax.set_xticks(x)
    ax.set_xticklabels(df["Genero"])

else:
    df_largo = df.melt(
        id_vars="Genero",
        var_name="Plataforma",
        value_name="Ventas"
    )

    sns.barplot(
        data=df_largo,
        x="Genero",
        y="Ventas",
        hue="Plataforma",
        ax=ax
    )

ax.set_title("Ventas por género y plataforma")
ax.set_xlabel("Género")
ax.set_ylabel("Ventas (millones de unidades)")
ax.legend(title="Plataforma")
ax.grid(axis="y", alpha=0.3)
ax.set_axisbelow(True)

st.pyplot(fig)
plt.close(fig)
