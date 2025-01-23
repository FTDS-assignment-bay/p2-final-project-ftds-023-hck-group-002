import pandas as pd
import numpy as np
from airflow import DAG
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.operators.python import PythonOperator
from elasticsearch import Elasticsearch
from datetime import datetime, timedelta
from sqlalchemy import create_engine


# deafult parameter
default_args = {
    'owner': 'Gallant',
    'retry': None,
    'start_date': datetime(2025, 1, 21)
}

def extract():
        database = "retail_store"
        username = "airflow"
        password = "airflow"
        host = "postgres"

        postgres_url = f"postgresql+psycopg2://{username}:{password}@{host}/{database}"

        engine = create_engine(postgres_url)
        conn = engine.connect()

        df = pd.read_sql_query('select * from retail_store', conn)

        df.to_csv('/opt/airflow/data/retail_store_inventory_raw.csv', index=False)

        # df.to_sql('data_customer', conn, index=False, if_exists='replace')
        # print("Success INSERT")

# function cleaning
def transform():
    # # ambil konteks task instance
    # ti = context['ti']

    # # ambil path data mentah
    # data_path = ti.xcom_pull(task_ids='extract_data', key='raw_data_path')

    # buka sebagai dataframe
    data_raw = pd.read_csv('/opt/airflow/data/retail_store_inventory_raw.csv')

    # cleaning
    data_raw = data_raw.dropna()  # Hapus baris dengan nilai NaN
    data_raw = data_raw.drop_duplicates()  # Hapus baris duplikat

        
    # perbaiki penulisan semua kolom yang ada
    data_raw.columns = data_raw.columns.str.strip()
    data_raw.columns = data_raw.columns.str.replace(' ', '_')
    data_raw.columns = data_raw.columns.str.lower()  

    # ganti kolom holiday/promotion menjadi promotion     
    if 'holiday/promotion' in data_raw.columns:
        data_raw.rename(columns={'holiday/promotion': 'promotion'}, inplace=True)

    # Konversi kolom 'date' ke tipe datetime
    if 'date' in data_raw.columns:
        try:
            data_raw['Date'] = pd.to_datetime(data_raw['date'], errors='coerce')  # Konversi ke datetime
            data_raw = data_raw.dropna(subset=['date'])  # Hapus baris dengan nilai 'date' yang tidak valid
        except Exception as e:
            print(f"Error converting 'date' column: {e}")


    # Simpan data setelah cleaning
    path = '/opt/airflow/dags/retail_store_inventory_cleaned.csv'
    data_raw.to_csv(path, index=False)

    # # export path data clean
    # context['ti'].xcom_push(key='clean_data_path', value=path)


# function load data
# def load(**context):
#     # ambil konteks task instance
#     ti = context['ti']

#     # ambil path data bersih
#     data_path = ti.xcom_pull(task_ids='transform_data', key='clean_data_path') 

#     # load jadi dataframe
#     data_clean = pd.read_csv(data_path)

#     # buat koneksi elasticsearch
#     es = Elasticsearch('http://elasticsearch:9200')
#     if not es.ping():
#         print('tidak terkonek')

#     # load data, per baris
#     for i, row in data_clean.iterrows():

#         doc = row.to_json()
#         res = es.index(index='finpro_hck023_group2', doc_type='doc', body = doc)
def insert_to_db():
    database = "retail_store"
    username = "airflow"
    password = "airflow"
    host = "postgres"

    postgres_url = f"postgresql+psycopg2://{username}:{password}@{host}/{database}"

    engine = create_engine(postgres_url)
    conn = engine.connect()

    df = pd.read_csv('/opt/airflow/dags/retail_store_inventory_cleaned.csv')

    df.to_sql('retail_store_cleaned', conn, index=False, if_exists='replace')
    print("Success INSERT")


# definisi dag
with DAG(
    'finpro_hck23',
    description = 'finpro_hck23', 
    # schedule_interval = '10,20,30 9 * * 6',
    default_args = default_args,
    catchup = False
) as dag:

    # task extract
    extract_data = PythonOperator(
        task_id = 'extract_data',
        python_callable = extract,
        provide_context=True
    )

    # task transform
    transform_data = PythonOperator(
        task_id = 'transform_data',
        python_callable = transform,
        provide_context = True
    )

    # task load
    load_data = PythonOperator(
        task_id = 'load_data',
        python_callable = insert_to_db,
        provide_context = True
    )

extract_data >> transform_data >> load_data
