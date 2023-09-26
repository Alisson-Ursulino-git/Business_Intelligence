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
