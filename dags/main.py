from airflow import DAG
import pendulum
from datetime import datetime, timedelta
from api.video_stats import get_playlist_id, get_video_id, extract_video_data, save_to_json

local_tz = pendulum.timezone("Asia/Jakarta")

default_args = {
    "owner": None,
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "email": None,
    # 'retries': 1,
    # 'retry_delay': timedelta(minutes=5),
    "max_active_runs": 1,
    "dagrun_timeout": timedelta(hours=1),
    "start_date": datetime(2025, 1, 1, tzinfo=local_tz),
    # 'end_date': datetime(2030, 12, 31, tzinfo=local_tz),
}