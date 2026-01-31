import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Dashboard de Salários na Área de Dados",
    page_icon="📊",
    layout="wide"
)

# 1️⃣ Carregar os dados
df = pd.read_csv(
    "https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv"
)

st.title("Dashboard de Salários na Área de Dados")

# 2️⃣ Visualizar os dados
st.subheader("Visualização dos dados")
st.dataframe(df.head())

# 3️⃣ Gráfico: salário médio por cargo (Top 10)

st.subheader("Salário médio por cargo (Top 10)")

salario_por_cargo = (
    df.groupby("job_title", as_index=False)["salary_in_usd"]
    .mean()
    .sort_values(by="salary_in_usd", ascending=False)
    .head(10)
)

fig = px.bar(
    salario_por_cargo,
    x="job_title",
    y="salary_in_usd",
    title="Top 10 cargos com maior salário médio (USD)",
    labels={
        "job_title": "Cargo",
        "salary_in_usd": "Salário médio (USD)"
    }
)

st.plotly_chart(fig, use_container_width=True)

# 3️⃣ Filtro interativo
st.sidebar.header("Filtros")

cargo_selecionado = st.sidebar.selectbox(
    "Selecione o cargo:",
    options=df["job_title"].unique()
)

df_filtrado = df[df["job_title"] == cargo_selecionado]

st.subheader(f"Dados para o cargo: {cargo_selecionado}")
st.dataframe(df_filtrado.head())

st.subheader("Salário por país para o cargo selecionado")

salario_por_pais = (
    df_filtrado.groupby("company_location", as_index=False)["salary_in_usd"]
    .mean()
    .sort_values(by="salary_in_usd", ascending=False)
)

fig = px.bar(
    salario_por_pais,
    x="company_location",
    y="salary_in_usd",
    title=f"Salário médio por país — {cargo_selecionado}",
    labels={
        "company_location": "País",
        "salary_in_usd": "Salário médio (USD)"
    }
)

st.plotly_chart(fig, use_container_width=True)

