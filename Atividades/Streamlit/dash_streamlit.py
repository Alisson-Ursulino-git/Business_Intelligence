import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
plt.style.use('dark_background')

#%% CARREGANDO E PREPARANDO DADOS
# path = r'C:\Users\aliss\Google Drive\Documentos\Atuária\Business Intelligence\Atividades'
# path_archive = r'\ds_salaries.csv'
path = 'https://raw.githubusercontent.com/Alisson-Ursulino-git/Business_Intelligence/main/Atividades/Streamlit/ds_salaries.csv'
df_dados = pd.read_csv(path)#, encoding='ISO-8859-1',delimiter=';')

df_dados.isna().sum()


#%% CARREGANDO E PREPARANDO DADOS

st.header('Salários 2023')
st.markdown('Esse dashboard ilustra gráficos com informações sobre distintos salários e suas respectivas profissões em 2023')

# FILTROS

lista_jobs = df_dados['job_title'].dropna().unique()
lista_jobs = np.insert(lista_jobs, 0, 'Todas')

op_natureza = st.sidebar.selectbox('Salário',lista_jobs)

if op_natureza != 'Todas':
    df_dados = df_dados[df_dados['job_title']==op_natureza]

lista_salarios = np.sort(df_dados['salary_in_usd'].unique())

salario_inicial, salario_final = st.sidebar.select_slider('Salário',lista_salarios,value=(df_dados['salary_in_usd'].min(),df_dados['salary_in_usd'].max()))

df_dados = df_dados[df_dados['salary_in_usd']<= salario_final]
df_dados = df_dados[df_dados['salary_in_usd']>= salario_inicial]

# FILTROS

st.dataframe(df_dados)

# Salários por Ano
#df_dados['work_year'] = pd.to_datetime(df_dados['work_year'], format="%Y")
fig_salario_por_ano = df_dados.groupby(df_dados['work_year'])['salary_in_usd'].mean().plot(kind='line')

st.write("Salário Médio por Ano")
fig_salario_por_ano.set_ylabel('# Salário Médio em Dólar')
fig_salario_por_ano.set_xlabel('Ano')

st.pyplot(fig_salario_por_ano.figure)
#df_dados.info()
#df_dados.groupby(df_dados['company_location'])['salary_in_usd'].mean()

# Salario por Tamanho da Companhia
st.write("Salário Médio por Tamanho da Companhia")
media_company = df_dados.groupby('company_size')['salary_in_usd'].mean()
st.bar_chart(media_company)

#%% Salario por Profissão
# Cria uma lista com todas as opções de profissão
job_titles = df_dados['job_title'].unique().tolist()
# Cria uma caixa de seleção com as opções de profissão
selected_jobs = st.multiselect('Selecione as profissões', job_titles, default=job_titles)
# Filtra os dados com base nas profissões selecionadas
filtered_data = df_dados[df_dados['job_title'].isin(selected_jobs)]
# Calcula a média salarial para as profissões selecionadas
media_jobs = filtered_data.groupby('job_title')['salary_in_usd'].mean()
# Exibe o resultado
st.write(f"Salário médio para as profissões {', '.join(selected_jobs)}: {media_jobs.mean()}")
st.bar_chart(media_jobs)
#%% Salario por Nível de Experiência
st.write("Salário Médio por Nível de Experiência")
media_company = df_dados.groupby('experience_level')['salary_in_usd'].mean()
st.bar_chart(media_company)

#%% Salario por Localização
# Cria uma lista com todas as opções de localização da companhia
company_locations = df_dados['company_location'].unique().tolist()
# Cria uma caixa de seleção com as opções de localização da companhia
selected_locations = st.multiselect('Selecione as localizações da companhia',
                                    company_locations, default=company_locations)
# Filtra os dados com base nas localizações da companhia selecionadas
filtered_data = df_dados[df_dados['company_location'].isin(selected_locations)]
# Calcula a média salarial para as localizações da companhia selecionadas
media_company = filtered_data['salary_in_usd'].mean()

# Exibe o resultado
st.write(f"Salário médio para companhias localizadas em {', '.join(selected_locations)}: {media_company}")
media_company = filtered_data.groupby('company_location')['salary_in_usd'].mean()
st.bar_chart(media_company)

#%% Salario por Residência
st.write("Salário Médio por Residência")
media_company = df_dados.groupby('employee_residence')['salary_in_usd'].mean()
st.bar_chart(media_company)
