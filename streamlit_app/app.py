import pandas as pd
import plotly.express as px
import streamlit as st

from queries import load_orders, load_marketing


st.set_page_config(
    page_title="FunnelVision Analytics",
    page_icon="📊",
    layout="wide",
)

st.title("FunnelVision")
st.subheader("E-Commerce Marketing & Sales Analytics")

try:
    orders = load_orders()
    marketing = load_marketing()

    orders["ORDER_CREATED_AT"] = pd.to_datetime(
        orders["ORDER_CREATED_AT"]
    )

    st.sidebar.header("Filters")

    min_date = orders["ORDER_CREATED_AT"].min().date()
    max_date = orders["ORDER_CREATED_AT"].max().date()

    date_range = st.sidebar.date_input(
        "Order Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
    )

    filtered_orders = orders.copy()

    if isinstance(date_range, tuple) and len(date_range) == 2:
        start_date, end_date = date_range

        filtered_orders = filtered_orders[
            filtered_orders["ORDER_CREATED_AT"].dt.date.between(
                start_date, end_date
            )
        ]

    sources = sorted(
        marketing["UTM_SOURCE"].dropna().unique().tolist()
    )

    selected_sources = st.sidebar.multiselect(
        "Traffic Source",
        options=sources,
        default=sources,
    )

    filtered_marketing = marketing[
        marketing["UTM_SOURCE"].isin(selected_sources)
    ]

    total_revenue = filtered_orders["ORDER_REVENUE_USD"].sum()
    total_orders = filtered_orders["ORDER_ID"].nunique()
    average_order_value = (
        total_revenue / total_orders if total_orders else 0
    )
    total_refunds = filtered_orders["TOTAL_REFUNDS_USD"].sum()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total Revenue", f"${total_revenue:,.2f}")
    c2.metric("Total Orders", f"{total_orders:,}")
    c3.metric("Average Order Value", f"${average_order_value:,.2f}")
    c4.metric("Total Refunds", f"${total_refunds:,.2f}")

    st.divider()

    st.subheader("Revenue Over Time")

    revenue_by_date = (
        filtered_orders.groupby(
            filtered_orders["ORDER_CREATED_AT"].dt.date
        )["ORDER_REVENUE_USD"]
        .sum()
        .reset_index()
    )

    revenue_by_date.columns = ["Order Date", "Revenue"]

    fig1 = px.line(
        revenue_by_date,
        x="Order Date",
        y="Revenue",
        title="Daily Revenue",
    )

    st.plotly_chart(fig1, use_container_width=True)

    left, right = st.columns(2)

    with left:
        st.subheader("Revenue by Traffic Source")

        source_revenue = (
            filtered_marketing.groupby("UTM_SOURCE", dropna=False)
            ["REVENUE_USD"]
            .sum()
            .reset_index()
        )

        fig2 = px.bar(
            source_revenue,
            x="UTM_SOURCE",
            y="REVENUE_USD",
            title="Revenue by Source",
        )

        st.plotly_chart(fig2, use_container_width=True)

    with right:
        st.subheader("Orders by Device")

        device_orders = (
            filtered_marketing.groupby("DEVICE_TYPE", dropna=False)
            ["ORDERS_COUNT"]
            .sum()
            .reset_index()
        )

        fig3 = px.bar(
            device_orders,
            x="DEVICE_TYPE",
            y="ORDERS_COUNT",
            title="Orders by Device",
        )

        st.plotly_chart(fig3, use_container_width=True)

    st.subheader("Sales Data")

    st.dataframe(
        filtered_orders.sort_values(
            "ORDER_CREATED_AT", ascending=False
        ),
        use_container_width=True,
    )

except Exception as exc:
    st.error("Unable to load the dashboard data.")
    st.exception(exc)