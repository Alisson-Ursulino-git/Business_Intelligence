import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
plt.style.use('dark_background')

#%% CARREGANDO E PREPARANDO DADOS
path = r'C:\Users\aliss\Google Drive\Documentos\Atuária\Business Intelligence\Atividades'
path_archive = r'\ds_salaries.csv'
df_dados = pd.read_csv(path+path_archive)#, encoding='ISO-8859-1',delimiter=';')

df_dados.isna().sum()


#%% CARREGANDO E PREPARANDO DADOS

st.header('Salários 2023')
st.markdown('Esse dashboard ilustra gráficos com informações sobre distintos salários e suas respectivas profissões em 2023')

# FILTROS

lista_jobs = df_dados['job_title'].dropna().unique()
lista_jobs = np.insert(lista_jobs, 0, 'Todas')

op_natureza = st.sidebar.selectbox('Trabalhos',lista_jobs)

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

# Salario por Companhia
st.write("Salário Médio por Tamanho da Companhia")
media_company = df_dados.groupby('company_size')['salary_in_usd'].mean()
st.bar_chart(media_company)

# Salario por Profissão
st.write("Salário Médio por Profissão")
media_company = df_dados.groupby('job_title')['salary_in_usd'].mean()
st.bar_chart(media_company)


# Salario por Nível de Experiência
st.write("Salário Médio por Nível de Experiência")
media_company = df_dados.groupby('experience_level')['salary_in_usd'].mean()
st.bar_chart(media_company)

# Salario por Localização
st.write("Salário Médio por Localização")
media_company = df_dados.groupby('company_location')['salary_in_usd'].mean()
st.bar_chart(media_company)

# Salario por Residência
st.write("Salário Médio por Residência")
media_company = df_dados.groupby('employee_residence')['salary_in_usd'].mean()
st.bar_chart(media_company)
