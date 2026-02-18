# Apa yang masih perlu ku pelajari lebih dalam?

## Airflow Architecture

- User
- webserver
- DAG directory
- metadata, database
- scheduler, executor
- queue
- worker

## Airflow Directories

- dags
- logs
- config
- plugins
- tests
- data
- include

## Docker

- apa bedanya ini `docker-compose up` ini `docker-compose up -d` ini `docker-compose up -d --build` dan juga ini `docker-compose build`

- Jika command ini dijalankan `docker-compose down`, dari logic yang aku tangkap, docker akan menjalankan sistem dengan perintah atau step dari `file.yaml`. jika nanti apabila ingin diberhentikan menggunakan `docker-compose down`, maka semua kontainer akan berhenti dan menghilang di docker, dan apabila ingin dijalankan lagi menggunakan docker compose up, maka akan berjalan.

## Data Warehouse

- BELAJAR MEMAHAMI SCHEMA CUKKK... OPO IKU STAGING, CORE, DKK
- Belajar kode di file `data_utils.py`
- Belajar alasan dan penggunaan fungsi `from airflow.providers.postgres.hooks.postgres import PostgresHook` dan `from psycopg2.extras import RealDictCursor`
- Belajar kode di file `data_loading.py`
- Belajar kode di file `data_modification.py`
- Belajar kode di file `data_transformation.py` di `https://developers.google.com/youtube/v3/docs/videos#contentDetails.duration`

## Lainnya

- Belajar lebih dalam struktural `docker-compose.yaml`
- Belajar lebih dalam struktural `init-multiple-databases.sh`
- Apa fungsi decorators `from airflow.decorators import task` yang diletakkan diatas setiap fungsi
- Belajar lebih dalam tentang bash script yang sering digunakan 

