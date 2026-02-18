
- Masuk dulu ke container airflow worker
- Check apakah ada library soda-core-postgres di dalam container airflow-worker
```bash
pip show soda-core-progres
```

- Masukkan command ini untuk tes koneksi configuration 
```bash
soda test-connection -d '[nama-database]' -c /opt/airflow/include/soda/configuration.yml -V
soda test-connection -d pg_datasource -c /opt/airflow/include/soda/configuration.yml -V
```

- Masukkan command ini untuk menjalankan Quality Control pada data
```bash
soda scan -d pg_datasource -c /opt/airflow/include/soda/configuration.yml -v SCHEMA=core /opt/airflow/include/soda/checks.yml

soda scan -d pg_datasource -c /opt/airflow/include/soda/configuration.yml -v SCHEMA=core /opt/airflow/include/soda/checks.yml -V
```

