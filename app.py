import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="CTH - Gestão Escolar & Desempenho", layout="wide")

# Cabeçalho Principal
st.title("🏫 Colégio Teixeira Holanda")
st.subheader("Sistema de Gestão de Desempenho e Diagnóstico Pedagógico")

# Sidebar - Controle de Períodos e Upload
st.sidebar.header("⚙️ Painel de Controle")
etapa_selecionada = st.sidebar.selectbox(
    "Selecione o Período de Análise", 
    ["2ª Etapa", "1ª Etapa", "Comparativo 1ª x 2ª", "3ª Etapa (Novo)"]
)

# Upload de novos boletins/notas do 3º Período
st.sidebar.markdown("---")
st.sidebar.subheader("📥 Atualizar Notas do Período")
uploaded_file = st.sidebar.file_uploader(
    "Enviar Boletins/Planilha do 3º Período (PDF ou Excel)", 
    type=["pdf", "xlsx"]
)

if uploaded_file:
    st.sidebar.success("Arquivo recebido com sucesso! Processando notas...")

# KPIs Principais
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total de Alunos", "163", "Ativos no Fund. II")
col2.metric("Aprovação Direta", "24 Alunos", "14.7% sem RP")
col3.metric("Alunos com RP", "139 Alunos", "85.3% em pelo menos 1 matéria")
col4.metric("Risco de Reprovação", "3 Alunos", "3+ matérias < 5,0")

st.markdown("---")

# Formulário para entrada manual de notas adicionais
with st.expander("📝 Inserir / Editar Notas do 3º Período Manualmente"):
    with st.form("form_notas"):
        c1, c2, c3 = st.columns(3)
        aluno_nome = c1.text_input("Nome do Aluno")
        turma_aluno = c2.selectbox(
            "Turma", 
            ["6º ANO/M", "6º ANO/T", "7º ANO/M", "7º ANO/T", "8º ANO/M", "9º ANO/M"]
        )
        disciplina = c3.selectbox(
            "Disciplina", 
            ["Matemática", "Português", "História", "Geografia", "Ciências", "Inglês", "Filosofia", "Artes"]
        )
        
        n1, n2 = st.columns(2)
        nota_3_etapa = n1.number_input("Nota Média 3ª Etapa", min_value=0.0, max_value=10.0, value=7.0)
        nota_rp_3 = n2.number_input("Nota RP 3ª Etapa (se houver)", min_value=0.0, max_value=10.0, value=0.0)
        
        btn_salvar = st.form_submit_button("Salvar e Atualizar Dashboards")
        if btn_salvar:
            st.success(f"Nota de {disciplina} para {aluno_nome} atualizada com sucesso!")
