# FunnelVision

### E-Commerce Marketing Funnel Analytics | Modern Data Stack

FunnelVision is an end-to-end e-commerce analytics project that transforms raw business data into analytics-ready datasets and presents key business metrics through an interactive dashboard.

## Technology Stack

* **Snowflake:** Cloud data warehouse.
* **dbt:** Data transformation and data quality testing.
* **Apache Airflow:** Workflow orchestration.
* **Streamlit:** Interactive analytics dashboard.
* **Docker:** Containerization.
* **Python and SQL:** Application logic and data transformations.

## Data Pipeline

1. Load e-commerce CSV data into Snowflake.
2. Transform raw data using dbt staging models.
3. Build intermediate transformation models.
4. Generate analytical marts.
5. Validate data quality using dbt tests.
6. Orchestrate dbt execution and testing through Airflow.
7. Visualize analytical results through Streamlit.

## dbt Models

The project contains 10 dbt models:

* 6 staging models.
* 2 intermediate models.
* 2 analytical mart models.

### Data Quality Results

* 11 tests passed.
* 0 warnings.
* 0 errors.

## Airflow Pipeline

The DAG `funnelvision_dbt_pipeline` executes two sequential tasks:

1. `dbt_run`
2. `dbt_test`

## Dashboard

The Streamlit dashboard provides key performance indicators, charts, and filters for exploring e-commerce performance.

Dashboard evidence is available in [`evidence/dashboard/`](evidence/dashboard/).

## Architecture

See the [architecture diagram](docs/architecture/architecture.png).

## Repository Structure

```text
FunnelVision/
├── airflow/
│   └── dags/
├── data/
├── dbt_project/
│   └── models/
│       ├── staging/
│       ├── intermediate/
│       └── marts/
├── docker/
│   └── dbt/
├── docs/
│   └── architecture/
├── evidence/
│   ├── airflow/
│   ├── dashboard/
│   ├── dbt/
│   └── snowflake/
├── presentation/
├── streamlit_app/
├── docker-compose.yml
└── README.md
```

## Evidence and Presentation

* Screenshots documenting Airflow, dbt, Snowflake, and the dashboard are stored in `evidence/`.
* The project presentation is available at [`presentation/FunnelVision_Presentation.pptx`](presentation/FunnelVision_Presentation.pptx).

## Security

* Keep credentials and secrets in local environment files.
* Never commit `.env`, database passwords, or private connection profiles.
* Review files before pushing changes to a public repository.

## Project Status

The core pipeline has been implemented. The recorded dbt tests passed, the Airflow workflow completed successfully, and the Streamlit dashboard was running during project validation.
