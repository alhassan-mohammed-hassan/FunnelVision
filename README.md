# FunnelVision
## Modern Data Stack Analytics Project

### 1. Project Overview
FunnelVision is an e-commerce analytics project designed to transform raw business data into analytics-ready datasets and present key business metrics through an interactive dashboard.

### 2. Technology Stack
- Snowflake: Cloud data warehouse and storage.
- dbt: Data transformation and data quality testing.
- Apache Airflow: Pipeline orchestration and scheduling.
- Streamlit: Interactive analytics dashboard.
- Docker: Containerization and execution environment.

### 3. Data Pipeline
1. Load raw e-commerce CSV data into Snowflake.
2. Transform raw data into staging models using dbt.
3. Build intermediate models for further transformations.
4. Generate analytical marts for reporting.
5. Execute dbt tests to validate data quality.
6. Orchestrate dbt execution and testing through Airflow.
7. Visualize analytical results through Streamlit.

### 4. dbt Models
The project contains 10 dbt models:
- 6 staging models.
- 2 intermediate models.
- 2 analytical mart models.

### 5. Data Quality
The dbt test execution completed successfully:
- 11 tests passed.
- 0 warnings.
- 0 errors.

### 6. Airflow Orchestration
The Airflow DAG `funnelvision_dbt_pipeline` executes:
1. `dbt_run`
2. `dbt_test`

The test task runs after the transformation task completes successfully.

### 7. Dashboard
The Streamlit dashboard presents key performance indicators, charts, and filters based on the project's analytical data.

### 8. Project Structure
- `dbt_project/`: dbt project and transformation models.
- `profiles/`: dbt connection profile.
- `airflow/dags/`: Airflow DAG definitions.
- `streamlit_app/`: Streamlit dashboard and dependencies.
- `data/`: Project data files.
- `docker-compose.yml`: Project container configuration.

### 9. Security
Credentials and secrets must be stored in environment variables and must not be committed to version control or included in screenshots.

### 10. Current Status
The core pipeline has been implemented, dbt models and tests have passed, the Airflow DAG has completed successfully, and the Streamlit dashboard is running.
