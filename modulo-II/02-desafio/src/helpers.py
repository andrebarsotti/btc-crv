import os
import requests
import pandas as pd
import chardet
from urllib.parse import urlparse
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

########################################################################
# Codigos fornecido pelo Chat GPT
########################################################################
def ensure_folder_exists(file_path):
    abs_path = os.path.abspath(file_path)
    folder = os.path.dirname(abs_path)

    if not os.path.exists(folder):
        os.makedirs(folder)

def get_file_name_from_url(url):
    parsed_url = urlparse(url)
    file_name = os.path.basename(parsed_url.path)
    return file_name

def join_with_local_path(local_path, file_name):
    return os.path.join(local_path, file_name)

def save_file_as_utf8(content, local_path):
    # Detect the original encoding of the file content
    original_encoding = chardet.detect(content)['encoding']

    # Decode the content using the original encoding and encode it using UTF-8
    content_utf8 = content.decode(original_encoding).encode('utf-8')

    with open(local_path, 'wb') as file:
        file.write(content_utf8)

def download_and_save_file(url, local_folder):
    file_name = get_file_name_from_url(url)
    local_path = join_with_local_path(local_folder, file_name)
    
    response = requests.get(url)

    if response.status_code == 200:
        ensure_folder_exists(local_path)
        save_file_as_utf8(response.content, local_path)
    else:
        print(f"Error: Unable to download the file. Status code {response.status_code}")

    return file_name, local_path