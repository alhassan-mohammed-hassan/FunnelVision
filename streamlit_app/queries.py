import os
import pandas as pd
import snowflake.connector
import streamlit as st


@st.cache_resource
def get_connection():
    return snowflake.connector.connect(
        account=os.environ["SNOWFLAKE_ACCOUNT"],
        user=os.environ["SNOWFLAKE_USER"],
        password=os.environ["SNOWFLAKE_PASSWORD"],
        warehouse="COMPUTE_WH",
        database="ECOMMERCE_DB",
        schema="ANALYTICS",
        role="ACCOUNTADMIN",
    )


@st.cache_data(ttl=300)
def load_orders():
    conn = get_connection()

    query = """
        SELECT
            ORDER_ID,
            ORDER_CREATED_AT,
            ORDER_REVENUE_USD,
            TOTAL_REFUNDS_USD,
            ESTIMATED_PROFIT_USD
        FROM ECOMMERCE_DB.ANALYTICS.FCT_ORDERS
    """

    return pd.read_sql(query, conn)


@st.cache_data(ttl=300)
def load_marketing():
    conn = get_connection()

    query = """
        SELECT
            UTM_SOURCE,
            UTM_CAMPAIGN,
            DEVICE_TYPE,
            SESSIONS_COUNT,
            ORDERS_COUNT,
            REVENUE_USD,
            CONVERSION_RATE,
            AVERAGE_ORDER_VALUE_USD
        FROM ECOMMERCE_DB.ANALYTICS.MART_MARKETING_PERFORMANCE
    """

    return pd.read_sql(query, conn)