from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="funnelvision_dbt_pipeline",
    description="Run FunnelVision dbt models and tests",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["funnelvision", "dbt", "snowflake"],
) as dag:
    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command=(
            "docker run --rm "
            "--env-file /opt/airflow/project/.env "
            "-v C:/FunnelVision/dbt_project:/app "
            "-v C:/FunnelVision/profiles:/root/.dbt "
            "funnelvision-dbt dbt run"
        ),
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command=(
            "docker run --rm "
            "--env-file /opt/airflow/project/.env "
            "-v C:/FunnelVision/dbt_project:/app "
            "-v C:/FunnelVision/profiles:/root/.dbt "
            "funnelvision-dbt dbt test"
        ),
    )

    dbt_run >> dbt_test
