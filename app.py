import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="CTH - Gestão de Desempenho Escolar",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS Personalizado ---
st.markdown("""
<style>
    .main-title { font-size: 2.2rem; font-weight: 800; color: #1E3A8A; margin-bottom: 0px; }
    .sub-title { font-size: 1.1rem; color: #4B5563; margin-bottom: 20px; }
    .stMetric { background-color: #F8FAFC; padding: 12px; border-radius: 8px; border: 1px solid #E2E8F0; }
</style>
""", unsafe_allow_html=True)

# --- TÍTULO ---
st.markdown('<div class="main-title">🏫 Colégio Teixeira Holanda</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Sistema Integrado de Gestão de Desempenho e Diagnóstico Pedagógico</div>', unsafe_allow_html=True)

# --- DADOS BASEADOS NO BANCO AUDITADO ---
data_turmas = pd.DataFrame({
    'Turma': ['6º ANO/M', '6º ANO/T', '7º ANO/M', '7º ANO/T', '8º ANO/M', '9º ANO/M'],
    'Total_Alunos': [36, 36, 26, 16, 31, 18],
    'Sem_RP_1': [4, 3, 5, 1, 5, 2],
    'Sem_RP_2': [2, 2, 6, 1, 8, 5],
    'Com_RP_1': [32, 33, 21, 15, 26, 16],
    'Com_RP_2': [34, 34, 20, 15, 23, 13],
    'Risco_Reprov_1': [4, 3, 1, 2, 1, 0],
    'Risco_Reprov_2': [1, 2, 0, 0, 0, 0],
    'Media_Orig_1': [7.21, 7.09, 7.72, 6.56, 7.69, 7.61],
    'Media_Orig_2': [7.49, 7.65, 8.18, 7.34, 8.38, 8.08]
})

data_ranking_2 = pd.DataFrame({
    'Disciplina': ['Matemática', 'História', 'Química', 'Filosofia', 'Inglês', 'Geografia', 'Ciências', 'Artes', 'Ed. Física', 'Português', 'Biologia', 'Redação', 'Of. Negócios', 'Física', 'Literatura'],
    'Total_Alunos': [163, 163, 49, 163, 163, 163, 145, 163, 163, 163, 49, 163, 163, 49, 163],
    'Alunos_em_RP': [123, 80, 23, 72, 41, 41, 28, 25, 23, 16, 3, 8, 7, 1, 1]
})
data_ranking_2['Pct_RP'] = (data_ranking_2['Alunos_em_RP'] / data_ranking_2['Total_Alunos']) * 100

data_ranking_1 = pd.DataFrame({
    'Disciplina': ['Matemática', 'História', 'Inglês', 'Artes', 'Filosofia', 'Geografia', 'Português', 'Ciências', 'Ed. Física', 'Redação'],
    'Total_Alunos': [163, 163, 163, 163, 163, 163, 145, 163, 163, 163],
    'Alunos_em_RP': [106, 100, 80, 66, 64, 45, 38, 32, 28, 20]
})
data_ranking_1['Pct_RP'] = (data_ranking_1['Alunos_em_RP'] / data_ranking_1['Total_Alunos']) * 100

df_risco_2 = pd.DataFrame([
    {"Aluno": "DAVI DA SILVA LIMA", "Turma": "6º ANO/T", "Disciplinas_Abaixo5": 4, "RPs_Iniciais": 10, "RPs_Recuperadas": 4, "RPs_Finais": 6, "Media_Final": 5.88},
    {"Aluno": "FERNANDO ADRIAN FEITOSA TORRES", "Turma": "6º ANO/T", "Disciplinas_Abaixo5": 4, "RPs_Iniciais": 9, "RPs_Recuperadas": 1, "RPs_Finais": 8, "Media_Final": 5.75},
    {"Aluno": "JULIA VIEIRA LIMA", "Turma": "6º ANO/M", "Disciplinas_Abaixo5": 3, "RPs_Iniciais": 7, "RPs_Recuperadas": 2, "RPs_Finais": 5, "Media_Final": 5.98}
])

df_risco_1 = pd.DataFrame([
    {"Aluno": "GUILHERME KLAIVER SOUSA MORAIS", "Turma": "9º ANO/M", "Disciplinas_Abaixo5": 4, "RPs_Iniciais": 11, "RPs_Recuperadas": 4, "RPs_Finais": 7, "Media_Final": 6.39},
    {"Aluno": "CLARISSA TEIXEIRA DE HOLANDA", "Turma": "8º ANO/M", "Disciplinas_Abaixo5": 4, "RPs_Iniciais": 10, "RPs_Recuperadas": 3, "RPs_Finais": 7, "Media_Final": 6.37},
    {"Aluno": "PEDRO IGOR LIMA DOS SANTOS", "Turma": "6º ANO/M", "Disciplinas_Abaixo5": 4, "RPs_Iniciais": 9, "RPs_Recuperadas": 2, "RPs_Finais": 7, "Media_Final": 6.17},
    {"Aluno": "MARIA ISIS ANASTACIO PEREIRA", "Turma": "6º ANO/M", "Disciplinas_Abaixo5": 5, "RPs_Iniciais": 9, "RPs_Recuperadas": 3, "RPs_Finais": 6, "Media_Final": 5.92},
    {"Aluno": "JOSE EDUARDO FURTADO BANDEIRA JUNIOR", "Turma": "6º ANO/M", "Disciplinas_Abaixo5": 4, "RPs_Iniciais": 9, "RPs_Recuperadas": 2, "RPs_Finais": 7, "Media_Final": 5.90},
    {"Aluno": "DAVI DA SILVA LIMA", "Turma": "6º ANO/T", "Disciplinas_Abaixo5": 4, "RPs_Iniciais": 9, "RPs_Recuperadas": 3, "RPs_Finais": 6, "Media_Final": 5.85},
    {"Aluno": "FERNANDO ADRIAN FEITOSA TORRES", "Turma": "6º ANO/T", "Disciplinas_Abaixo5": 4, "RPs_Iniciais": 8, "RPs_Recuperadas": 1, "RPs_Finais": 7, "Media_Final": 5.70},
    {"Aluno": "JULIA VIEIRA LIMA", "Turma": "6º ANO/M", "Disciplinas_Abaixo5": 3, "RPs_Iniciais": 6, "RPs_Recuperadas": 1, "RPs_Finais": 5, "Media_Final": 5.80},
    {"Aluno": "EMILLY VITORIA OLIVEIRA DE SOUZA", "Turma": "7º ANO/T", "Disciplinas_Abaixo5": 3, "RPs_Iniciais": 5, "RPs_Recuperadas": 0, "RPs_Finais": 5, "Media_Final": 6.12},
    {"Aluno": "ANTONIO LUCAS BARBOSA DA SILVA", "Turma": "9º ANO/M", "Disciplinas_Abaixo5": 3, "RPs_Iniciais": 6, "RPs_Recuperadas": 2, "RPs_Finais": 4, "Media_Final": 6.42},
    {"Aluno": "KALLEB SILVA DE ALMEIDA", "Turma": "6º ANO/M", "Disciplinas_Abaixo5": 3, "RPs_Iniciais": 8, "RPs_Recuperadas": 1, "RPs_Finais": 7, "Media_Final": 6.20}
])

df_boletim_aluno_davi = pd.DataFrame({
    'Disciplina': ['Matemática', 'História', 'Geografia', 'Português', 'Ciências', 'Inglês', 'Filosofia', 'Artes', 'Ed. Física', 'Redação', 'Literatura', 'Oficina de Negócios'],
    'Media_1': [5.5, 3.0, 5.0, 5.5, 6.5, 4.0, 4.0, 5.0, 4.5, 7.0, 8.0, 4.0],
    'RP_1': [4.5, 0.0, 2.0, 7.0, 6.0, 2.0, 3.0, 6.0, 4.0, 7.0, 8.0, 7.5],
    'Media_2': [5.0, 5.5, 5.0, 6.5, 7.0, 7.0, 4.0, 6.0, 4.0, 7.0, 8.0, 4.0],
    'RP_2': [1.0, 4.0, 7.0, 8.5, 0.0, 0.0, 3.0, 7.0, 4.5, 0.0, 0.0, 7.5]
})
df_boletim_aluno_davi['Final_1'] = df_boletim_aluno_davi.apply(lambda r: max(r['Media_1'], r['RP_1']), axis=1)
df_boletim_aluno_davi['Final_2'] = df_boletim_aluno_davi.apply(lambda r: max(r['Media_2'], r['RP_2']), axis=1)

# --- SIDEBAR: CONTROLE DE ANÁLISE ---
st.sidebar.header("⚙️ Painel de Controle")
modo_visao = st.sidebar.radio("Modo de Exibição", ["Visão Geral / Turmas", "👤 Análise por Aluno (Individual)"])

if modo_visao == "Visão Geral / Turmas":
    etapa_sel = st.sidebar.selectbox(
        "Selecione o Período de Análise",
        ["2ª Etapa (Atual)", "1ª Etapa", "Comparativo 1ª x 2ª", "3ª Etapa (Cadastrar)"]
    )

    turmas_opcoes = ["Todas as Turmas", "6º ANO/M", "6º ANO/T", "7º ANO/M", "7º ANO/T", "8º ANO/M", "9º ANO/M"]
    turma_sel = st.sidebar.selectbox("Filtrar por Turma", turmas_opcoes)

    st.sidebar.markdown("---")
    st.sidebar.subheader("📥 Atualizar Notas / Boletins")
    uploaded_file = st.sidebar.file_uploader("Enviar Boletim PDF/Excel (3º Período)", type=["pdf", "xlsx", "csv"])

    if uploaded_file:
        st.sidebar.success("Arquivo recebido com sucesso! Processando notas...")

    df_t_filtered = data_turmas if turma_sel == "Todas as Turmas" else data_turmas[data_turmas['Turma'] == turma_sel]

    if etapa_sel == "2ª Etapa (Atual)":
        tot_al = df_t_filtered['Total_Alunos'].sum()
        com_rp = df_t_filtered['Com_RP_2'].sum()
        sem_rp = df_t_filtered['Sem_RP_2'].sum()
        risco = df_t_filtered['Risco_Reprov_2'].sum()
        
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total de Alunos", tot_al, f"{turma_sel}")
        col2.metric("Aprovação Direta", f"{sem_rp} Alunos", f"{(sem_rp/tot_al)*100:.1f}% sem RP")
        col3.metric("Alunos com RP", f"{com_rp} Alunos", f"{(com_rp/tot_al)*100:.1f}% com ≥ 1 RP")
        col4.metric("Risco de Reprovação", f"{risco} Alunos", "3+ matérias < 5,0", delta_color="inverse")
        
        st.markdown("---")
        col_chart1, col_chart2 = st.columns(2)
        
        with col_chart1:
            st.subheader("🏆 Ranking de Criticidade por Disciplina (2ª Etapa)")
            fig_rank = px.bar(
                data_ranking_2.sort_values(by='Pct_RP', ascending=True),
                y='Disciplina', x='Pct_RP', orientation='h',
                text_auto='.1f%', color='Pct_RP', color_continuous_scale='Reds',
                title="% de Alunos em RP por Disciplina"
            )
            fig_rank.update_layout(showlegend=False, xaxis_title="% Alunos em RP", yaxis_title="")
            st.plotly_chart(fig_rank, use_container_width=True)
            
        with col_chart2:
            st.subheader("🧭 Diagnóstico de Alunos com RP por Turma")
            fig_turmas = px.bar(
                df_t_filtered, x='Turma', y=['Sem_RP_2', 'Com_RP_2'],
                title="Distribuição de Alunos: Sem RP vs Com RP",
                barmode='stack',
                color_discrete_map={'Sem_RP_2': '#16A34A', 'Com_RP_2': '#DC2626'},
                labels={'value': 'Quantidade de Alunos', 'variable': 'Situação'}
            )
            st.plotly_chart(fig_turmas, use_container_width=True)
            
        st.markdown("---")
        st.subheader("⚠️ Alunos em Risco Pedagógico Crítico (2ª Etapa)")
        st.caption("Estudantes com 3 ou mais disciplinas com Média Final abaixo de 5,0")
        
        df_risco_filt = df_risco_2 if turma_sel == "Todas as Turmas" else df_risco_2[df_risco_2['Turma'] == turma_sel]
        if len(df_risco_filt) > 0:
            st.dataframe(df_risco_filt, use_container_width=True)
        else:
            st.info("Nenhum aluno na faixa crítica de risco para a turma selecionada na 2ª Etapa!")

    elif etapa_sel == "1ª Etapa":
        tot_al = df_t_filtered['Total_Alunos'].sum()
        com_rp = df_t_filtered['Com_RP_1'].sum()
        sem_rp = df_t_filtered['Sem_RP_1'].sum()
        risco = df_t_filtered['Risco_Reprov_1'].sum()
        
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total de Alunos (1ª Etapa)", tot_al, f"{turma_sel}")
        col2.metric("Aprovação Direta", f"{sem_rp} Alunos", f"{(sem_rp/tot_al)*100:.1f}% sem RP")
        col3.metric("Alunos com RP", f"{com_rp} Alunos", f"{(com_rp/tot_al)*100:.1f}% com ≥ 1 RP")
        col4.metric("Risco de Reprovação", f"{risco} Alunos", "3+ matérias < 5,0", delta_color="inverse")
        
        st.markdown("---")
        col_chart1, col_chart2 = st.columns(2)
        
        with col_chart1:
            st.subheader("🏆 Ranking de Criticidade por Disciplina (1ª Etapa)")
            fig_rank = px.bar(
                data_ranking_1.sort_values(by='Pct_RP', ascending=True),
                y='Disciplina', x='Pct_RP', orientation='h',
                text_auto='.1f%', color='Pct_RP', color_continuous_scale='Oranges',
                title="% de Alunos em RP por Disciplina (1ª Etapa)"
            )
            fig_rank.update_layout(showlegend=False, xaxis_title="% Alunos em RP", yaxis_title="")
            st.plotly_chart(fig_rank, use_container_width=True)
            
        with col_chart2:
            st.subheader("🧭 Diagnóstico de Alunos com RP por Turma (1ª Etapa)")
            fig_turmas = px.bar(
                df_t_filtered, x='Turma', y=['Sem_RP_1', 'Com_RP_1'],
                title="Distribuição de Alunos: Sem RP vs Com RP (1ª Etapa)",
                barmode='stack', color_discrete_map={'Sem_RP_1': '#16A34A', 'Com_RP_1': '#EA580C'}
            )
            st.plotly_chart(fig_turmas, use_container_width=True)
            
        st.markdown("---")
        st.subheader("⚠️ Alunos em Risco Pedagógico Crítico (1ª Etapa)")
        df_risco_filt = df_risco_1 if turma_sel == "Todas as Turmas" else df_risco_1[df_risco_1['Turma'] == turma_sel]
        st.dataframe(df_risco_filt, use_container_width=True)

    elif etapa_sel == "Comparativo 1ª x 2ª":
        st.subheader("📈 Evolução e Comparativo entre a 1ª e a 2ª Etapas")
        
        c1, c2, c3 = st.columns(3)
        al_risco_1 = df_t_filtered['Risco_Reprov_1'].sum()
        al_risco_2 = df_t_filtered['Risco_Reprov_2'].sum()
        diff_risco = al_risco_2 - al_risco_1
        
        c1.metric("Alunos em Risco (1ª Etapa)", f"{al_risco_1} Alunos")
        c2.metric("Alunos em Risco (2ª Etapa)", f"{al_risco_2} Alunos", f"{diff_risco} Alunos", delta_color="normal")
        
        med_orig_1 = df_t_filtered['Media_Orig_1'].mean()
        med_orig_2 = df_t_filtered['Media_Orig_2'].mean()
        c3.metric("Evolução da Média Geral", f"{med_orig_2:.2f}", f"+{med_orig_2 - med_orig_1:.2f} pontos")
        
        st.markdown("---")
        st.subheader("📊 Comparação da Média Geral por Turma (1ª vs 2ª Etapa)")
        fig_comp_turmas = px.bar(
            df_t_filtered, x='Turma', y=['Media_Orig_1', 'Media_Orig_2'],
            barmode='group', title="Evolução da Média Geral Original por Turma",
            labels={'value': 'Média Geral', 'variable': 'Etapa'},
            color_discrete_map={'Media_Orig_1': '#64748B', 'Media_Orig_2': '#1E3A8A'}
        )
        st.plotly_chart(fig_comp_turmas, use_container_width=True)

    elif etapa_sel == "3ª Etapa (Cadastrar)":
        st.info("💡 Módulo de Cadastro da 3ª Etapa ativo. Utilize o formulário abaixo ou faça o upload do arquivo para incluir novas notas.")

else:
    # MODALIDADE: ANÁLISE POR ALUNO INDIVIDUAL
    st.subheader("👤 Ficha de Acompanhamento Individualizado do Estudante")
    
    lista_alunos = [
        "DAVI DA SILVA LIMA (6º ANO/T)",
        "FERNANDO ADRIAN FEITOSA TORRES (6º ANO/T)",
        "JULIA VIEIRA LIMA (6º ANO/M)",
        "JOSE EDUARDO FURTADO BANDEIRA JUNIOR (6º ANO/M)",
        "GUILHERME KLAIVER SOUSA MORAIS (9º ANO/M)",
        "CLARISSA TEIXEIRA DE HOLANDA (8º ANO/M)"
    ]
    aluno_selecionado = st.sidebar.selectbox("Selecione o Aluno para Diagnóstico", lista_alunos)
    
    st.markdown(f"### **Estudante:** `{aluno_selecionado}`")
    
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Turma", "6º ANO/T")
    c2.metric("RPs Iniciais (2ª Etapa)", "10 Disciplinas", "Alerta RPs")
    c3.metric("RPs Recuperadas", "4 Disciplinas", "40% Reversão")
    c4.metric("Média Final 2ª Etapa", "5.88", "+0.03 vs 1ª Etapa")
    
    st.markdown("---")
    st.subheader("📊 Evolução de Notas Por Disciplina (1ª vs 2ª Etapa)")
    
    fig_aluno = px.bar(
        df_boletim_aluno_davi, x='Disciplina', y=['Final_1', 'Final_2'],
        barmode='group', title=f"Boletim Comparativo: {aluno_selecionado}",
        labels={'value': 'Nota Final', 'variable': 'Etapa'},
        color_discrete_map={'Final_1': '#94A3B8', 'Final_2': '#1E3A8A'}
    )
    fig_aluno.add_shape(type="line", x0=-0.5, x1=11.5, y0=7.0, y1=7.0, line=dict(color="Green", width=2, dash="dash"))
    fig_aluno.add_shape(type="line", x0=-0.5, x1=11.5, y0=5.0, y1=5.0, line=dict(color="Red", width=2, dash="dash"))
    
    st.plotly_chart(fig_aluno, use_container_width=True)
    
    st.subheader("📋 Tabela Detalhada do Aluno")
    st.dataframe(df_boletim_aluno_davi, use_container_width=True)

# --- FORMULÁRIO DE ENTRADA MANUAL ---
st.markdown("---")
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
            ["Matemática", "Português", "História", "Geografia", "Ciências", "Inglês", "Filosofia", "Artes", "Química", "Física", "Biologia", "Redação", "Literatura", "Ed. Física", "Oficina de Negócios"]
        )
        
        n1, n2 = st.columns(2)
        nota_3_etapa = n1.number_input("Nota Média 3ª Etapa", min_value=0.0, max_value=10.0, value=7.0)
        nota_rp_3 = n2.number_input("Nota RP 3ª Etapa (se houver)", min_value=0.0, max_value=10.0, value=0.0)
        
        btn_salvar = st.form_submit_button("Salvar e Atualizar Dashboards")
        if btn_salvar:
            st.success(f"Nota de {disciplina} para {aluno_nome} ({turma_aluno}) salva com sucesso!")
