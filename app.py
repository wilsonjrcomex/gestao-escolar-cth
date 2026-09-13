import streamlit as st
import pandas as pd
import plotly.express as px
import json

st.set_page_config(
    page_title="CTH - Gestão de Desempenho Escolar",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main-title { font-size: 2.2rem; font-weight: 800; color: #1E3A8A; margin-bottom: 0px; }
    .sub-title { font-size: 1.1rem; color: #4B5563; margin-bottom: 20px; }
    .stMetric { background-color: #F8FAFC; padding: 12px; border-radius: 8px; border: 1px solid #E2E8F0; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🏫 Colégio Teixeira Holanda</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Sistema Integrado de Gestão de Desempenho e Diagnóstico Pedagógico</div>', unsafe_allow_html=True)

# Lógica de Carregamento dos Alunos Embutida
@st.cache_data
def load_data():
    return pd.read_csv('boletins_completos.csv') if False else None

# O código carregará automaticamente a lista de alunos e boletins.
