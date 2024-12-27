import streamlit as st
import pandas as pd
import plotly.express as px

# Dades dels fons (amb la columna Gestora)
data = {
    "ISIN": [
        "LU0034353002", "LU0113257694", "LU0599946893",
        "LU0218171717", "IE00B4468526", "LU1769942233", "LU0203975437",
        "LU0171307068", "LU0232524495", "LU1295551144",
        "ES0174013021", "IE00B3K83P04", "IE00B03HCZ61",
        "IE0031786142", "LU0072462426", "LU0599946893"
    ],
    "Nom del Fons": [
        "DWS FLOAT RATE NOTES",
        "SISF EUR CORPORATE BOND",
        "DWS CONCEPT KALDEMORGEN",
        "JPM US SELECT EQ A EUR",
        "POLAR CAPITAL GLOBAL TECHNOLOGY R EUR",
        "DWS INVEST CROCI JAPAN",
        "ROBECO GLOBAL PREMIUM",
        "BGF WORLD HEALTHSCIENCE FUND A2 EUR",
        "AB - AMERICAN GROWTH PORTFOLIO A EUR ACC",
        "CAPITAL GROUP NEW PERSPECTIVE FUND (LUX) B EUR",
        "CREAND RTA. FIXA MIXTA",
        "POLAR CAP-HEALTH",
        "VANG, GLOB, STK",
        "VANG-EMRG IND",
        "BLACKROCK GLOBAL FUND",
        "DWS CONCEPT KALDEMORGEN"
    ],
    "Gestora": [
        "Deutsche Bank", "Deutsche Bank", "Deutsche Bank",
        "Deutsche Bank", "Crèdit Andorrà", "Deutsche Bank", "Crèdit Andorrà",
        "Crèdit Andorrà", "CaixaBank", "CaixaBank",
        "CaixaBank", "Crèdit Andorrà", "Crèdit Andorrà",
        "Crèdit Andorrà", "Deutsche Bank", "Deutsche Bank"
    ],
    "Empreses Principals": [
        "DWS ESG Money Market, Swedbank AB, BNP Paribas Cardif",
        "Germany Federal Bonds, JPMorgan, MSD Netherlands",
        "Flexible Allocation (sense posicions fixes)",
        "Apple, Microsoft, Amazon",
        "Apple, NVIDIA, Samsung",
        "Toyota, Sony, Nintendo",
        "Alphabet, Roche, Microsoft",
        "UnitedHealth, Eli Lilly, AbbVie",
        "Apple, Microsoft, Amazon",
        "Tesla, Alphabet, Roche",
        "No disponible",
        "UnitedHealth, Johnson & Johnson, Pfizer",
        "Apple, Microsoft, Alphabet",
        "Tencent, Samsung, Alibaba",
        "Amazon, Tesla, Roche",
        "Flexible Allocation (sense posicions fixes)"
    ],
    "Distribució Geogràfica": [
        "Eurozona: 81.31%, Efectiu: 17.01%",
        "Eurozona: 87.83%, Efectiu: 9.85%",
        "Global (flexible)",
        "Estats Units (alta concentració)",
        "Global (tecnologia)",
        "Japó 100%",
        "Global (diversificada)",
        "Estats Units: 76.86%, Europa: 17.44%",
        "Estats Units 100%",
        "Global (tecnologia, salut, consum)",
        "Zona Euro",
        "Estats Units",
        "Global",
        "Mercats Emergents",
        "Global",
        "Global (flexible)"
    ],
    "Distribució Actius": [
        "Renda Fixa: 70%, Efectiu: 30%",
        "Renda Fixa: 87.83%, Efectiu: 9.85%",
        "Multiactiu (Flexible)",
        "Renda Variable: 100%",
        "Tecnologia: 60%, Comunicacions: 30%",
        "Renda Variable (Japó): 100%",
        "Tecnologia: 40%, Salut: 35%, Energia: 25%",
        "Salut: 100%",
        "Renda Variable: 100%",
        "Tecnologia: 50%, Salut: 30%, Consum: 20%",
        "Renda Fixa: 70%, Altres: 30%",
        "Salut: 100%",
        "Renda Variable Global",
        "Mercats Emergents",
        "Multiactiu (Flexible)",
        "Renda Variable Global"
    ],
    "Comissions (%)": [
        0.75, 0.85, 1.5, 1.0, 1.2, 0.9, 1.1, 1.4, 1.0, 1.3, 0.7, 1.5, 0.9, 1.2, 0.95, 1.0
    ],
    "Benchmark": [
        "Euribor + Spread", "Euribor + Spread", "MSCI World",
        "S&P 500", "MSCI Tech Index", "Nikkei 225", "MSCI ACWI",
        "MSCI Health Index", "S&P 500", "MSCI ACWI",
        "MSCI Europe", "MSCI Health Index", "MSCI ACWI",
        "MSCI Emerging Markets", "MSCI ACWI", "MSCI World"
    ],
    "Pes Relatiu (%)": [
        10, 8, 12, 15, 5, 10, 6, 8, 9, 7, 4, 6, 5, 8, 8, 10
    ],
    "Nivell de Risc": [3, 3, 5, 6, 6, 6, 5, 6, 5, 4, 3, 6, 6, 6, 5, 5]
}

df = pd.DataFrame(data)

# Títol del Dashboard
st.title("Dashboard dels Fons d'Inversió")

# Filtre per Gestora
st.sidebar.subheader("Filtra per Gestora")
selected_gestores = st.sidebar.multiselect(
    "Selecciona una o més gestores:",
    options=df["Gestora"].unique(),
    default=df["Gestora"].unique()
)

# Aplicar el filtre
filtered_df = df[df["Gestora"].isin(selected_gestores)]

# Mostrar taula filtrada
st.subheader("Fons filtrats per Gestora")
st.dataframe(filtered_df)

# Gràfic Comparatiu: Nivell de Risc per Gestora
st.subheader("Comparativa de Nivell de Risc per Gestora")
fig = px.bar(
    filtered_df,
    x="Nom del Fons",
    y="Nivell de Risc",
    color="Gestora",
    title="Nivell de Risc dels Fons per Gestora",
    labels={"Nivell de Risc": "Risc (1-7)", "Nom del Fons": "Fons"},
    width=1000,
    height=600
)
st.plotly_chart(fig)