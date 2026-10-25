FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir "dbt-core==1.10.13" "dbt-snowflake==1.10.2"

CMD ["dbt", "--version"]