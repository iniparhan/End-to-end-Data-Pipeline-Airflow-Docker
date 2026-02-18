Pada x-airflow-common do docker-compose.yaml, adjust:
- Image jadikan ke `latest`, supaya bisa mengikuti berapa update yang ditentukan
- Comment pada bagian `env_file` dan isinya, karena setelah ini akan mengambil crudential data langsung dari repos github

Pada `services` -> `postgres`:
- Comment pada bagian `env_file` dan isinya, karena setelah ini akan mengambil crudential data langsung dari repos github
- Un-comment pada bagian `environtment`-nya