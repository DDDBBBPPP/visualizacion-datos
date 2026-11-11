
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def mostrar():
    st.title("Histograma")
    st.caption("Distribución de 200 calificaciones simuladas")

    rng = np.random.default_rng(42)
    notas = rng.normal(loc=6, scale=1.8, size=200)
    notas = np.clip(notas, 0, 10)

    df = pd.DataFrame({"Nota": notas.round(2)})

    intervalos = st.slider(
        "Número de intervalos",
        min_value=5,
        max_value=20,
        value=10
    )

    bordes = np.linspace(0, 10, intervalos + 1)

    tab_mpl, tab_sns = st.tabs([
        "Matplotlib", "Seaborn"
    ])

    with tab_mpl:
        fig, ax = plt.subplots(figsize=(10, 5))

        ax.hist(
            df["Nota"],
            bins=bordes,
            color="#4285F4",
            edgecolor="white"
        )

        ax.set_title("Distribución de calificaciones")
        ax.set_xlabel("Calificación")
        ax.set_ylabel("Número de estudiantes")
        ax.set_xlim(0, 10)
        ax.grid(axis="y", alpha=0.3)

        st.pyplot(fig)
        plt.close(fig)

    with tab_sns:
        fig, ax = plt.subplots(figsize=(10, 5))

        sns.histplot(
            data=df,
            x="Nota",
            bins=bordes,
            kde=True,
            color="#4285F4",
            edgecolor="white",
            ax=ax
        )

        ax.set_title("Distribución de calificaciones")
        ax.set_xlabel("Calificación")
        ax.set_ylabel("Número de estudiantes")
        ax.set_xlim(0, 10)
        ax.grid(axis="y", alpha=0.3)

        st.pyplot(fig)
        plt.close(fig)
