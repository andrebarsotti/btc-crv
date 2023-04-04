import os
import pandas as pd

from dotenv import load_dotenv


load_dotenv()

def get_env_var(var_name):
    return os.getenv(var_name)

def verificar_dados_faltando(df):
    contagem_faltantes = df.isnull().sum()
    return contagem_faltantes[contagem_faltantes > 0].sort_values(ascending=False)

def converter_colunas_para_numericos(df, columns, com_tratamento=True):
    for col in columns:
        if com_tratamento:
            df[col]=df[col].str.replace('.','',regex=False).str.replace(',','.',regex=False).replace('[^0-9\.]+', '', regex=True)
        df[col]=pd.to_numeric(df[col])