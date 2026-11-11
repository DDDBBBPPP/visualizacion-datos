
from pathlib import Path

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


@st.cache_data
def cargar_datos():
    ruta = Path(__file__).resolve().parent.parent / "datos" / "1921.CSV"
    df = pd.read_csv(ruta)
    df["date"] = pd.to_datetime(df["date"])
    return df


def mostrar():
    st.title("Gráfico de líneas")
    st.caption("Temperaturas máximas diarias durante enero de 1921")

    df = cargar_datos()
    df = df[df["date"].dt.month == 1].copy()

    estaciones = sorted(df["station_name"].dropna().unique())

    seleccion = st.multiselect(
        "Selecciona las estaciones meteorológicas",
        options=estaciones,
        default=estaciones[:3]
    )

    if not seleccion:
        st.warning("Selecciona al menos una estación.")
        return

    df = df[df["station_name"].isin(seleccion)].copy()
    df = df.dropna(subset=["temperature_max[C]"])
    df = df.sort_values("date")

    if df.empty:
        st.warning("No hay temperaturas disponibles para esta selección.")
        return

    tab_st, tab_mpl, tab_sns = st.tabs([
        "Streamlit", "Matplotlib", "Seaborn"
    ])

    with tab_st:
        tabla = df.pivot_table(
            index="date",
            columns="station_name",
            values="temperature_max[C]",
            aggfunc="mean"
        )
        st.line_chart(
            tabla,
            x_label="Fecha",
            y_label="Temperatura máxima (°C)"
        )

    with tab_mpl:
        fig, ax = plt.subplots(figsize=(11, 5))

        for estacion, grupo in df.groupby("station_name"):
            ax.plot(
                grupo["date"],
                grupo["temperature_max[C]"],
                marker="o",
                markersize=3,
                label=estacion
            )

        ax.set_title("Temperaturas máximas — Enero de 1921")
        ax.set_xlabel("Fecha")
        ax.set_ylabel("Temperatura máxima (°C)")
        ax.legend(title="Estación")
        ax.grid(alpha=0.3)
        fig.autofmt_xdate()
        fig.tight_layout()

        st.pyplot(fig)
        plt.close(fig)

    with tab_sns:
        fig, ax = plt.subplots(figsize=(11, 5))

        sns.lineplot(
            data=df,
            x="date",
            y="temperature_max[C]",
            hue="station_name",
            ax=ax
        )

        ax.set_title("Temperaturas máximas — Enero de 1921")
        ax.set_xlabel("Fecha")
        ax.set_ylabel("Temperatura máxima (°C)")
        ax.grid(alpha=0.3)
        fig.autofmt_xdate()
        fig.tight_layout()

        st.pyplot(fig)
        plt.close(fig)
