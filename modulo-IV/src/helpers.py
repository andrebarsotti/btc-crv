import os
import requests
import pandas as pd
import chardet
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor
from tqdm.notebook import tqdm
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

    os.makedirs(folder, exist_ok=True)

def get_file_name_from_url(url):
    parsed_url = urlparse(url)
    file_name = os.path.basename(parsed_url.path)
    return file_name

def join_with_local_path(local_path, file_name):
    return os.path.join(local_path, file_name)

def save_file_as_utf8(content, local_path):
    original_encoding = chardet.detect(content)['encoding']
    content_utf8 = content.decode(original_encoding).encode('utf-8')

    with open(local_path, 'wb') as file:
        file.write(content_utf8)

def download_and_save_file(url, local_folder, chunk_size=8192):
    file_name = get_file_name_from_url(url)
    local_path = join_with_local_path(local_folder, file_name)

    response = requests.get(url, stream=True)

    if response.status_code == 200:
        total_size = int(response.headers.get('content-length', 0))
        progress_bar = tqdm(total=total_size, unit='B', unit_scale=True, desc=file_name)

        ensure_folder_exists(local_path)

        with open(local_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=chunk_size):
                if chunk:  # Filter out keep-alive new chunks
                    file.write(chunk)
                    progress_bar.update(len(chunk))

        file_extension = os.path.splitext(file_name)[1]
        if file_extension.lower() == ".txt" or file_extension.lower() == ".csv":
            save_file_as_utf8(open(local_path, 'rb').read(), local_path)
        progress_bar.close()
    else:
        print(f"Error: Unable to download the file. Status code {response.status_code}")

    return file_name, local_path

def download_files_in_parallel(file_urls, local_folder, max_workers=5):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = [executor.submit(download_and_save_file, url, local_folder) for url in file_urls]

    return [result.result() for result in results]