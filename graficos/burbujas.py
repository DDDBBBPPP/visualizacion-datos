
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


@st.cache_data
def cargar_datos():
    df = sns.load_dataset("mpg")

    return df.dropna(
        subset=["horsepower", "mpg", "weight", "origin"]
    )


def mostrar():
    st.title("Gráfico de burbujas")
    st.caption("Potencia, eficiencia y peso de los automóviles")

    df = cargar_datos()

    colores = {
        "usa": "#4285F4",
        "europe": "#EA4335",
        "japan": "#34A853"
    }

    origenes = st.multiselect(
        "Selecciona los orígenes",
        options=list(colores),
        default=list(colores)
    )

    if not origenes:
        st.warning("Selecciona al menos un origen.")
        return

    df = df[df["origin"].isin(origenes)].copy()

    tab_st, tab_mpl, tab_sns = st.tabs([
        "Streamlit", "Matplotlib", "Seaborn"
    ])

    with tab_st:
        st.scatter_chart(
            df,
            x="horsepower",
            y="mpg",
            color="origin",
            size="weight",
            x_label="Potencia (HP)",
            y_label="Eficiencia (MPG)"
        )

    with tab_mpl:
        tam_min, tam_max = 30, 350

        # Escala de tamaño fija para todo el dataset
        datos_completos = cargar_datos()
        peso_min = datos_completos["weight"].min()
        peso_max = datos_completos["weight"].max()

        tamanos = tam_min + (
            (df["weight"] - peso_min) /
            (peso_max - peso_min)
        ) * (tam_max - tam_min)

        fig, ax = plt.subplots(figsize=(10, 6))

        for origen, grupo in df.groupby("origin"):
            ax.scatter(
                grupo["horsepower"],
                grupo["mpg"],
                s=tamanos.loc[grupo.index],
                color=colores[origen],
                alpha=0.5,
                edgecolors="white",
                label=origen
            )

        ax.set_title("Potencia, eficiencia y peso")
        ax.set_xlabel("Potencia (HP)")
        ax.set_ylabel("Eficiencia (MPG)")
        ax.legend(title="Origen")
        ax.grid(alpha=0.3)

        st.pyplot(fig)
        plt.close(fig)

    with tab_sns:
        fig, ax = plt.subplots(figsize=(10, 6))

        sns.scatterplot(
            data=df,
            x="horsepower",
            y="mpg",
            hue="origin",
            size="weight",
            sizes=(30, 350),
            size_norm=(
                cargar_datos()["weight"].min(),
                cargar_datos()["weight"].max()
            ),
            palette=colores,
            alpha=0.5,
            edgecolor="white",
            ax=ax
        )

        ax.set_title("Potencia, eficiencia y peso")
        ax.set_xlabel("Potencia (HP)")
        ax.set_ylabel("Eficiencia (MPG)")
        ax.grid(alpha=0.3)
        ax.legend(bbox_to_anchor=(1.02, 1), loc="upper left")
        fig.tight_layout()

        st.pyplot(fig)
        plt.close(fig)
