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

## Lainnya

- Belajar lebih dalam struktural `docker-compose.yaml`
- Belajar lebih dalam struktural `init-multiple-databases.sh`
- Apa fungsi decorators `from airflow.decorators import task` yang diletakkan diatas setiap fungsi
- Belajar lebih dalam tentang bash script yang sering digunakan 

