from __future__ import annotations

from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator


with DAG(
    dag_id="etl_example",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["example"],
) as dag:
    run_etl = BashOperator(
        task_id="run_etl",
        bash_command="python scripts/main.py --input data/sample_input.csv",
        cwd="data-engineering-project",
    )

