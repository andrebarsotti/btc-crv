import os
import pandas as pd

from dotenv import load_dotenv


load_dotenv()

def get_env_var(var_name):
    return os.getenv(var_name)

def verificar_dados_faltando(df):
    contagem_faltantes = df.isnull().sum()
    return contagem_faltantes[contagem_faltantes > 0].sort_values(ascending=False)
