
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris


@st.cache_data
def cargar_datos():
    iris = load_iris(as_frame=True)
    df = iris.frame.copy()
    df["Especie"] = df["target"].map(
        dict(enumerate(iris.target_names))
    )
    return df


def mostrar():
    st.title("Gráfico de dispersión")
    st.caption("Relación entre longitud y anchura de pétalos Iris")

    df = cargar_datos()

    colores = {
        "setosa": "#4285F4",
        "versicolor": "#EA4335",
        "virginica": "#34A853"
    }

    especies = st.multiselect(
        "Selecciona las especies",
        options=list(colores),
        default=list(colores)
    )

    if not especies:
        st.warning("Selecciona al menos una especie.")
        return

    df = df[df["Especie"].isin(especies)]

    tab_st, tab_mpl, tab_sns = st.tabs([
        "Streamlit", "Matplotlib", "Seaborn"
    ])

    with tab_st:
        st.scatter_chart(
            df,
            x="petal length (cm)",
            y="petal width (cm)",
            color="Especie",
            x_label="Longitud del pétalo (cm)",
            y_label="Anchura del pétalo (cm)"
        )

    with tab_mpl:
        fig, ax = plt.subplots(figsize=(10, 5))

        for especie, grupo in df.groupby("Especie"):
            ax.scatter(
                grupo["petal length (cm)"],
                grupo["petal width (cm)"],
                label=especie,
                color=colores[especie],
                alpha=0.7
            )

        ax.set_title("Relación entre longitud y anchura de pétalos")
        ax.set_xlabel("Longitud del pétalo (cm)")
        ax.set_ylabel("Anchura del pétalo (cm)")
        ax.legend(title="Especie")
        ax.grid(alpha=0.3)

        st.pyplot(fig)
        plt.close(fig)

    with tab_sns:
        fig, ax = plt.subplots(figsize=(10, 5))

        sns.scatterplot(
            data=df,
            x="petal length (cm)",
            y="petal width (cm)",
            hue="Especie",
            palette=colores,
            alpha=0.7,
            ax=ax
        )

        ax.set_title("Relación entre longitud y anchura de pétalos")
        ax.set_xlabel("Longitud del pétalo (cm)")
        ax.set_ylabel("Anchura del pétalo (cm)")
        ax.grid(alpha=0.3)

        st.pyplot(fig)
        plt.close(fig)
