WITH sessions AS (
    SELECT *
    FROM {{ ref('stg_website_sessions') }}
),

orders AS (
    SELECT
        website_session_id,
        order_id,
        order_revenue_usd
    FROM {{ ref('fct_orders') }}
),

session_metrics AS (
    SELECT
        s.website_session_id,
        s.utm_source,
        s.utm_campaign,
        s.device_type,
        COUNT(DISTINCT o.order_id) AS orders_count,
        COALESCE(SUM(o.order_revenue_usd), 0) AS revenue_usd
    FROM sessions AS s
    LEFT JOIN orders AS o
        ON s.website_session_id = o.website_session_id
    GROUP BY
        s.website_session_id,
        s.utm_source,
        s.utm_campaign,
        s.device_type
)

SELECT
    utm_source,
    utm_campaign,
    device_type,
    COUNT(*) AS sessions_count,
    SUM(orders_count) AS orders_count,
    SUM(revenue_usd) AS revenue_usd,
    SUM(orders_count) * 1.0 / NULLIF(COUNT(*), 0)
        AS conversion_rate,
    SUM(revenue_usd) / NULLIF(SUM(orders_count), 0)
        AS average_order_value_usd
FROM session_metrics
GROUP BY
    utm_source,
    utm_campaign,
    device_type