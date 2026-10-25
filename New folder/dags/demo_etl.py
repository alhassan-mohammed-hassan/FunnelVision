from datetime import datetime
import csv

from airflow.sdk import dag, task


@dag(
    dag_id="simple_etl",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["etl", "taskflow"],
)
def simple_etl(): #dag_id

    @task
    def extract():

        data = []

        with open("/opt/airflow/dags/data/sales.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                data.append(row)

        print("Extracted data:")
        print(data)

        return data


    @task
    def transform(data):

        transformed_data = []

        for row in data:

            quantity = int(row["quantity"])
            price = float(row["price"])

            total = quantity * price

            transformed_data.append({
                "product": row["product"],
                "quantity": quantity,
                "price": price,
                "total": total,
            })

        print("Transformed data:")
        print(transformed_data)

        return transformed_data


    @task
    def load(data):

        output_file = "/opt/airflow/dags/data/sales_transformed.csv"

        with open(output_file, "w", newline="") as file:

            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "product",
                    "quantity",
                    "price",
                    "total"
                ]
            )

            writer.writeheader()
            writer.writerows(data)

        print(f"Data loaded into {output_file}")


    load(
        transform(
            extract()
        )
    )


simple_etl()