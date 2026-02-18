## Unit Test 

- Check apakah ada library pytest di dalam container airflow-worker
```bash
pip show pytest
```

- Jalankan command ini di dalam container airflow-worker untuk melakukan testing
```bash
pytest -v tests/unit_test.py -k test_api_key
```

- Jalankan command ini di dalam container airflow-worker untuk melakukan testing
```bash
pytest -v -s tests/unit_test.py -k test_dags_integrity
```


## Integration Test

- Jalankan command ini di dalam container airflow-worker untuk melakukan testing
```bash
pytest -v tests/integration_test.py -k test_youtube_api_response
```

- Jalankan command ini di dalam container airflow-worker untuk melakukan testing
```bash
pytest -v tests/integration_test.py -k test_real_postgres_connection
```


## End to end Test 

- Kalau mau lihat atribut apa yang digunakan pada dags test
```bash
airflow dags test --help
```
```bash
airflow dags test produce_json
airflow dags test update_db
airflow dags test data_quality
```