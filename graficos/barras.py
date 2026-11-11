
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def mostrar():
    st.title("Barras agrupadas")
    st.caption("Ventas simuladas de videojuegos por género y plataforma")

    df = pd.DataFrame({
        "Genero": ["Acción", "Aventura", "RPG", "Deportes", "Estrategia"],
        "PC": [42, 35, 58, 18, 46],
        "PlayStation": [75, 62, 55, 68, 20],
        "Xbox": [60, 45, 38, 52, 15]
    })

    tab_st, tab_mpl, tab_sns = st.tabs([
        "Streamlit", "Matplotlib", "Seaborn"
    ])

    # Gráfico nativo de Streamlit
    with tab_st:
        st.bar_chart(
            df.set_index("Genero"),
            color=["#4285F4", "#EA4335", "#34A853"],
            stack=False,
            x_label="Género",
            y_label="Ventas (millones de unidades)"
        )

    # Gráfico con Matplotlib
    with tab_mpl:
        x = np.arange(len(df))
        ancho = 0.25

        fig, ax = plt.subplots(figsize=(10, 5))

        ax.bar(x - ancho, df["PC"], ancho,
               label="PC", color="#4285F4")
        ax.bar(x, df["PlayStation"], ancho,
               label="PlayStation", color="#EA4335")
        ax.bar(x + ancho, df["Xbox"], ancho,
               label="Xbox", color="#34A853")

        ax.set_title("Ventas de videojuegos por género y plataforma")
        ax.set_xlabel("Género")
        ax.set_ylabel("Ventas (millones de unidades)")
        ax.set_xticks(x)
        ax.set_xticklabels(df["Genero"])
        ax.set_ylim(0, 90)
        ax.legend(title="Plataforma")
        ax.grid(axis="y", alpha=0.3)
        ax.set_axisbelow(True)

        st.pyplot(fig)
        plt.close(fig)

    # Gráfico con Seaborn
    with tab_sns:
        df_largo = df.melt(
            id_vars="Genero",
            var_name="Plataforma",
            value_name="Ventas"
        )

        fig, ax = plt.subplots(figsize=(10, 5))

        sns.barplot(
            data=df_largo,
            x="Genero",
            y="Ventas",
            hue="Plataforma",
            palette=["#4285F4", "#EA4335", "#34A853"],
            ax=ax
        )

        ax.set_title("Ventas de videojuegos por género y plataforma")
        ax.set_xlabel("Género")
        ax.set_ylabel("Ventas (millones de unidades)")
        ax.set_ylim(0, 90)
        ax.legend(title="Plataforma")
        ax.grid(axis="y", alpha=0.3)
        ax.set_axisbelow(True)

        st.pyplot(fig)
        plt.close(fig)
