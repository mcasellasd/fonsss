import streamlit as st
import pandas as pd

# Dades inicials del dashboard
data = {
    "Fons d'Inversió": [
        "AB - American Growth Portfolio A EUR Acc",
        "BGF World Healthscience Fund A2 EUR",
        "Capital Group New Perspective Fund (LUX) B EUR",
    ],
    "ISIN": [
        "LU0232524495",
        "LU0171307068",
        "LU1295551144",
    ],
    "Objectiu Principal": [
        "Revalorització del capital a llarg termini invertint en grans companyies nord-americanes.",
        "Invertir en empreses del sector salut a nivell global.",
        "Identificar empreses multinacionals que es beneficien de canvis en el comerç global.",
    ],
    "Distribució Geogràfica": [
        "Principalment EUA",
        "EUA (76.86%), Europa (17.44%)",
        "Global",
    ],
    "Distribució Sectorial": [
        "Tecnologia (33.85%), Consum Cíclic (16.94%), Serveis Comunicació (15.54%)",
        "Salut (100%)",
        "Tecnologia (20.9%), Salut (14.7%), Consum Durador (14.0%)",
    ],
}

# Convertim les dades a DataFrame
df = pd.DataFrame(data)

# Crear el Dashboard
st.title("Dashboard dels Fons d'Inversió")
st.write("Comparativa detallada dels fons seleccionats amb els seus objectius i distribucions.")

# Mostra la taula completa
st.subheader("Taula Resum")
st.dataframe(df)